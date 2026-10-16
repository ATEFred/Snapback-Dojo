#!/usr/bin/env python3
"""Batch-paint the Unbothered Quest — ComfyUI + Qwen Image 2.1, LAN only.

Reads every `artPrompt` from the story pack in index.html (chapter, scene and
beat level), wraps it in the shared style anchor, and writes quest-art/<id>.png
which the app picks up automatically. Resumable: existing images are skipped.

Usage:
  python3 gen_art.py                 # generate everything missing
  python3 gen_art.py --only ch1i3    # just one
  python3 gen_art.py --force         # regenerate even if it exists
  python3 gen_art.py --limit 3       # first three missing
Nothing leaves the LAN: it only talks to COMFY (below) and the filesystem.
"""
import hashlib, json, pathlib, re, sys, time, urllib.error, urllib.request

COMFY = "http://100.102.235.82:8188"
HERE  = pathlib.Path(__file__).parent
OUT   = HERE / "quest-art"

UNET = "qwen_image_2.1_bf16.safetensors"
CLIP = "qwen3vl_8b_w4a8.safetensors"      # Qwen3-VL encoder, type qwen_image
VAE  = "qwen_image_2.1_vae_bf16.safetensors"
WIDTH, HEIGHT, STEPS, CFG = 1152, 640, 24, 4.0

STYLE = ("Storybook gothic-whimsy illustration in a Tim Burton-adjacent style: elongated crooked "
         "shapes, melancholy but gentle, deep twilight indigo and charcoal palette with soft "
         "mint-green and lavender accents, delicate crosshatch texture, matte painterly finish, "
         "charming whimsy, absolutely not scary, no text, no lettering, no watermark. ")
CAST  = ("Recurring characters — Wren: a calm unbothered ten-year-old girl with a straight black "
         "bob, pale round face, long ink-blue coat and bright green boots; her cat: a grumpy plump "
         "grey tabby; Echo the Mimic Imp: a small crooked patchwork-fabric imp with mismatched "
         "button eyes, a lopsided stitched smile and fraying threads. Scene: ")
NEG   = ("photorealistic, photograph, 3d render, gore, blood, horror, sharp teeth, jump scare, "
         "menacing monster, scary, text, letters, watermark, signature, blurry, deformed hands, "
         "extra fingers, low quality")

def api(path, data=None):
    req = urllib.request.Request(COMFY + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

def grab(path):
    with urllib.request.urlopen(COMFY + path, timeout=600) as r:
        return r.read()

def prompts_from_pack():
    """Scan the QUESTS const for id → artPrompt pairs, in story order."""
    src  = (HERE / "index.html").read_text()
    body = src.split("<script>", 1)[1].split("</script>", 1)[0]
    seg  = body[body.index("const QUESTS"): body.index("/* ---- runner ---- */")]
    pairs, cur = [], None
    for m in re.finditer(r'(id|artPrompt):"((?:[^"\\]|\\.)*)"', seg):
        if m.group(1) == "id":
            cur = m.group(2)
        elif cur:
            pairs.append((cur, m.group(2)))
    return pairs

def workflow(art_id, text, seed):
    return {
      "1": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET, "weight_dtype": "default"}},
      "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP, "type": "qwen_image"}},
      "3": {"class_type": "VAELoader",  "inputs": {"vae_name": VAE}},
      "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": STYLE + CAST + text}},
      "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": NEG}},
      "6": {"class_type": "EmptyLatentImage", "inputs": {"width": WIDTH, "height": HEIGHT, "batch_size": 1}},
      "7": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["4", 0],
            "negative": ["5", 0], "latent_image": ["6", 0], "seed": seed, "steps": STEPS,
            "cfg": CFG, "sampler_name": "euler", "scheduler": "simple", "denoise": 1.0}},
      "8": {"class_type": "VAEDecode", "inputs": {"samples": ["7", 0], "vae": ["3", 0]}},
      "9": {"class_type": "SaveImage", "inputs": {"images": ["8", 0],
            "filename_prefix": "snapback/" + art_id, "quality": "lossless"}},
    }

def generate(art_id, text):
    seed = int(hashlib.sha1(art_id.encode()).hexdigest()[:8], 16)
    pid = api("/prompt", {"prompt": workflow(art_id, text, seed), "client_id": "snapback-dojo"})["prompt_id"]
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
    jobs = prompts_from_pack()
    if only:
        jobs = [j for j in jobs if j[0] == only]
    print(f"{len(jobs)} art slots found in the story pack", flush=True)
    done = failed = skipped = 0
    for art_id, text in jobs:
        dest = OUT / (art_id + ".png")
        if dest.exists() and dest.stat().st_size > 0 and not force:
            skipped += 1
            continue
        if limit and done >= limit:
            break
        print(f"▸ {art_id}: {text[:70]}…", flush=True)
        try:
            generate(art_id, text)
            done += 1
        except (urllib.error.URLError, RuntimeError) as e:
            failed += 1
            print(f"  ✘ {art_id}: {e}", flush=True)
    print(f"finished — {done} painted, {skipped} already existed, {failed} failed", flush=True)

if __name__ == "__main__":
    main()
