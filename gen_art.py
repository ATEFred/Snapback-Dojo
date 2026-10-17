#!/usr/bin/env python3
"""Batch-paint the Unbothered Quest — ComfyUI + Qwen Image 2.1, LAN only.

Reads the visual asset register in story-visual-assets.md (asset id + content
brief) plus every `artPrompt` from the story pack, wraps them in the shared
style anchor, and writes quest-art/<id>.png
which the app picks up automatically. Resumable: existing images are skipped.

Usage:
  python3 gen_art.py                 # generate everything missing
  python3 gen_art.py --only ch1i3    # just one
  python3 gen_art.py --force         # regenerate even if it exists
  python3 gen_art.py --limit 3       # first three missing
Nothing leaves the LAN: it only talks to COMFY (below) and the filesystem.
"""
import hashlib, json, os, pathlib, re, sys, time, urllib.error, urllib.request

COMFY = "http://100.102.235.82:8188"
HERE  = pathlib.Path(__file__).parent
OUT   = HERE / "quest-art"

UNET = "qwen_image_2.1_bf16.safetensors"
CLIP = "qwen3vl_8b_w4a8.safetensors"      # Qwen3-VL encoder, type qwen_image
VAE  = "qwen_image_2.1_vae_bf16.safetensors"
WIDTH, HEIGHT, STEPS, CFG = 1152, 640, 28, 4.0

STYLE = ("Ornate Victorian dark storybook engraving: dense pen-and-ink crosshatch, indigo and slate ink "
         "washes with antique gold accents, twisted decorative vines curling through the borders, antique "
         "children's book plate, meticulous fine detail. "
         "Every element shares ONE unified antique etching treatment: characters shaded with pen hatching "
         "and ink wash, palette limited to indigo, slate, lavender and antique gold with a single muted "
         "sage-green accent, no flat modern colours, no plastic highlights. ")
WREN_CAT = ("Recurring characters — Wren: a Burton-style child about ten, long thin limbs, a slightly "
            "too-big ink-blue wool coat that hangs off her shoulders like she outgrew it, straight black "
            "bob, sage-green wellington boots; her face: big round eyes WIDE and alert with a small spark "
            "of nerves, composed closed mouth, quietly locked onto the strangeness like she cannot look "
            "away; her cat: a plump unimpressed grey tabby — a real, ordinary, four-pawed HOUSE CAT (and "
            "in scenes beyond the door it may have its mouth open mid-sentence, still a cat with no human "
            "features, upright or clothed). ")
CHARS = [  # (keywords in the content brief) → description, included ONLY when the brief calls for them
  (("echo", "patchwork"), "Echo the Mimic Imp: a small crooked PATCHWORK RAG imp with mismatched glass "
   "button eyes, stitched grin, fraying seams, blunt rag-doll head with floppy cloth ears, NO cat "
   "features; only he and Wren's grey tabby are ever imps/cats together"),
  (("wisp", "gazette", "courier"), "Wisp: a small nervous green-furred courier creature in a buttoned "
   "waistcoat, long ears, ink-stained fingers, enormous satchel"),
  (("duchess", "porcelain"), "the Duchess of HA: a tall stiff porcelain-faced woman in an antique gown "
   "with a big brass winding key between her shoulder blades"),
  (("toastbrig", "troll", "inspector"), "Toastbrig: an enormous plank-backed troll inspector with a "
   "whistling kettle for a helmet"),
  (("queen malvina", "crowned woman", "queen's portrait"), "Queen Malvina appears ONLY as described "
   "(usually a printed portrait on a notice): a tall crowned woman holding a little key on a chain"),
  (("paper bat",), "a paper bat wearing enormous spectacles"),
  (("mum", "dad", "parents", "family"), "Wren's ordinary parents: modern-dressed adults frozen mid "
   "breakfast, mid-gesture, gentle, unhurt"),
]
EXCLUDE = ("Only the characters named just above may appear in the scene. No other people, children, "
           "creatures, imps, dolls or travellers — if the description names no character beyond scenery, "
           "paint the object alone. ")

def cast_for(text):
    tl = text.lower()
    extra = [d for keys, d in CHARS if any(k in tl for k in keys)]
    return WREN_CAT + "; ".join(extra) + (". " if extra else ". ") + EXCLUDE

NEG   = ("photorealistic, photograph, 3d render, gore, blood, horror, sharp teeth, jump scare, "
         "terrified, screaming, menacing monster, truly scary, text, letters, watermark, signature, "
         "blurry, deformed hands, extra fingers, low quality, slack mouth, dopey, vacant stare, "
         "gormless, sleepy, bored, flat modern colours, plastic")

def api(path, data=None):
    req = urllib.request.Request(COMFY + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def grab(path):
    with urllib.request.urlopen(COMFY + path, timeout=600) as r:
        return r.read()

def prompts_from_assets():
    """Asset id → content brief from story-visual-assets.md (the visual register).
    Briefs are content-only by contract; the style anchor below is what paints them."""
    try:
        md = (HERE / "story-visual-assets.md").read_text()
    except FileNotFoundError:
        return []
    jobs = []
    for m in re.finditer(r'### `([a-z0-9_]+)`(.*?)(?=\n### `|\n## |\Z)', md, re.S):
        aid, sec = m.group(1), m.group(2)
        b = re.search(r'\*\*Content brief:\*\*\s*(.*?)(?=\n\n\*\*|\Z)', sec, re.S)
        if not b:
            continue
        brief = " ".join(b.group(1).split()).replace("**", "")
        jobs.append((aid, brief, True))
    return jobs

def prompts_from_pack():
    """Scan the QUESTS const for id → artPrompt pairs, in story order."""
    src  = (HERE / "index.html").read_text()
    body = src.split("<script>", 1)[1].split("</script>", 1)[0]
    end = next(body.index(mk) for mk in ("/* ---- v2 runner", "/* ---- runner") if mk in body)
    seg  = body[body.index("const QUESTS"): end]
    pairs, cur = [], None
    for m in re.finditer(r'(id|artPrompt):"((?:[^"\\]|\\.)*)"', seg):
        if m.group(1) == "id":
            cur = m.group(2)
        elif cur:
            pairs.append((cur, m.group(2)))
    return [(i, txt, False) for i, txt in pairs]

LETTER = (" Draw the specified lettering exactly as given: correct spelling, word order and "
          "arrow directions, clean legible antique serif capitals on the object. ")

def workflow(art_id, text, seed, want_text=False):
    return {
      "1": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET, "weight_dtype": "default"}},
      "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP, "type": "qwen_image"}},
      "3": {"class_type": "VAELoader",  "inputs": {"vae_name": VAE}},
      "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": STYLE + cast_for(text) + text +
            (LETTER if want_text else "")},
      },
      "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0],
            "text": NEG.replace("text, letters, ", "") if want_text else NEG}},
      "6": {"class_type": "EmptyLatentImage", "inputs": {"width": WIDTH, "height": HEIGHT, "batch_size": 1}},
      "7": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["4", 0],
            "negative": ["5", 0], "latent_image": ["6", 0], "seed": seed, "steps": STEPS,
            "cfg": CFG, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
      "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["3", 0]}},
      "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0],
            "filename_prefix": "snapback/" + art_id, "quality": "lossless"}},
    }

def generate(art_id, text, want_text=False):
    salt = os.environ.get("SEED_SALT", "")  # SEED_SALT=2 python3 gen_art.py --only X → a different take
    seed = int(hashlib.sha1((art_id + salt).encode()).hexdigest()[:8], 16)
    pid = api("/prompt", {"prompt": workflow(art_id, text, seed, want_text), "client_id": "snapback-dojo"})["prompt_id"]
    t0 = time.time()
    while time.time() - t0 < 900:
        time.sleep(2)
        hist = api("/history/" + pid)
        if pid in hist:
            entry = hist[pid]
            status = entry.get("status", {})
            if status.get("status_str") == "error":
                raise RuntimeError("comfy error: " + json.dumps(status)[:400])
            imgs = entry.get("outputs", {}).get("9", {}).get("images", [])
            if not imgs:
                raise RuntimeError("no output image in history")
            i = imgs[0]
            data = grab(f"/view?filename={i['filename']}&subfolder={i.get('subfolder','')}&type={i.get('type','output')}")
            dest = OUT / (art_id + ".png")
            dest.write_bytes(data)
            print(f"  ✔ {art_id}.png  ({len(data)//1024} KB, {time.time()-t0:.0f}s)", flush=True)
            return
    raise RuntimeError("timeout waiting for comfy")

def main():
    args = sys.argv[1:]
    force = "--force" in args
    only = args[args.index("--only") + 1] if "--only" in args else None
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else 0
    OUT.mkdir(exist_ok=True)
    jobs = prompts_from_assets() + prompts_from_pack()
    if only:
        jobs = [j for j in jobs if j[0] == only]
    print(f"{len(jobs)} art slots found (visual register + story pack)", flush=True)
    done = failed = skipped = 0
    for art_id, text, want_text in jobs:
        dest = OUT / (art_id + ".png")
        if dest.exists() and dest.stat().st_size > 0 and not force:
            skipped += 1
            continue
        if limit and done >= limit:
            break
        print(f"▸ {art_id}: {text[:70]}…", flush=True)
        try:
            generate(art_id, text, want_text)
            done += 1
        except (urllib.error.URLError, RuntimeError) as e:
            failed += 1
            print(f"  ✘ {art_id}: {e}", flush=True)
    print(f"finished — {done} painted, {skipped} already existed, {failed} failed", flush=True)

if __name__ == "__main__":
    main()
