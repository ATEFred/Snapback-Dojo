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
  (("echo", "patchwork"), "Echo the Mimic Imp: a soft knee-high rag doll sewn from brown "
   "and cream cloth patches, mismatched glass button eyes, a wide stitched grin, fraying seams, "
   "floppy cloth ears and a blunt cloth head, springing along with a puppet bounce"),
  # "wisp" alone is too eager: briefs mention him in the negative ("route later supplied by Wisp")
  (("wisp",), lambda tl: "wisp" in tl and any(k in tl for k in ("waistcoat","satchel","cart","bottle","press","gazette office",
   "pins his correction","ink-stained")) and "Wisp: a small nervous green-furred courier creature in a buttoned "
   "waistcoat, long ears, ink-stained fingers, enormous satchel"),
  (("courier",), lambda tl: "Wisp: a small nervous green-furred courier creature in a "
   "buttoned waistcoat, long ears, ink-stained fingers, enormous satchel"),
  (("duchess", "porcelain"), "the Duchess of HA: a tall stiff porcelain-faced woman in an antique gown "
   "with a big brass winding key between her shoulder blades"),
  (("toastbrig", "troll", "inspector"), "Toastbrig: an enormous plank-backed troll inspector with a "
   "whistling kettle for a helmet"),
  (("queen malvina", "malvina", "crowned woman", "queen's portrait"), "Queen Malvina appears ONLY as described "
   "(usually a printed portrait on a notice): a tall crowned woman holding a little key on a chain"),
  (("paper bat",), "a paper bat wearing enormous spectacles"),
  # The lake Reflection: a spotless silver-outlined imitation of the same girl.
  # Self-cancelling clause for briefs where the imitation became an ordinary reflection.
  (("~\\bimitation\\b", "~\\bsilver[- ]outlined?\\b"),
   "the Reflection: a picture-like magical imitation of the SAME girl — identical black bob and coat "
   "but spotlessly clean, polished boots, a thin silver outline and a rehearsed smile; the REAL girl is "
   "the one with muddy boots; exactly one real girl and one imitation when both appear; if the "
   "description says the imitation has become ordinary, paint only normal water reflections and NO "
   "silver outline"),
  # Pip & Pop: apple-wood usher puppets. Word-bounded names; the PIP & POP sign lettering alone must
  # not summon them into a shot the brief populates with nobody.
  (("~\\bpip\\b", "green-waistcoated", "square-headed", "square carved head"),
   lambda tl: ("royal ushers" not in tl) and ("Pip: the taller apple-WOOD puppet on a wheeled "
   "stage — square carved wooden head, visible hinged jaw, painted eyebrows, green waistcoat, one "
   "raised wooden finger in an officious presenting gesture; carved joints, NOT a real child")),
  (("~\\bpop\\b", "purple-waistcoated", "round-faced"),
   lambda tl: ("royal ushers" not in tl) and ("Pop: the shorter apple-WOOD puppet standing on a box — "
   "round carved wooden face, visible hinged mouth, lively painted eyebrows, purple waistcoat, one "
   "wooden hand mid-flourish; carved joints, NOT a real child")),
  # Chancellor Gleam and the parents. \bgleam\b skips the old "gleamed" briefs.
  ((r"~\bgleam\b",),
   "Chancellor Gleam: a tall hinged mirror in a polished silver frame with two thin brass arms and a "
   "small crown on his top rail, bowing politely at the hinge; butler-ish and officious; his glass "
   "shows ONLY ordinary reflections of the real scene — never an independent copy of the girl"),
  ((r"~\bmum\b",), "Wren's mum: a warm-looking parent in ordinary comfortable breakfast clothes, kind "
   "attentive face; a normal parent, no royal or magical costume"),
  ((r"~\bdad\b",), "Wren's dad: a kind parent in ordinary comfortable breakfast clothes with a jam "
   "knife nearby, curious listening face; a normal parent, no badges or uniforms"),
  (("mum", "dad", "parents", "family"), "Wren's ordinary parents: modern-dressed adults frozen mid "
   "breakfast, mid-gesture, gentle, unhurt"),
]
EXCLUDE = ("Only the characters named just above may appear in the scene. No other people, children, "
           "creatures, imps, dolls or travellers — if the description names no character beyond scenery, "
           "paint the object alone. Never duplicate a character: exactly one of each, unless the "
           "description explicitly asks for reflections or multiple views. ")

# Avatar plates are single-character portraits: no Wren anchor, no exclusion
# clause (both were smuggling Wren into every frame).
AVA_DESC = {
  "avatar_wren": "Wren: a Burton-style girl about ten, straight black bob, big round alert eyes with a "                 "small spark of nerves, composed closed mouth, slightly too-big ink-blue wool coat collar.",
  "avatar_cat": "A plump unimpressed grey tabby HOUSE CAT: slightly hooded eyes, one ear tilted as if "                "permanently unimpressed; a real four-pawed cat head, not anthropomorphic.",
  "avatar_echo": "Echo the Mimic Imp: a small crooked PATCHWORK RAG imp head, mismatched glass button "                 "eyes (one larger), stitched grin one stitch too wide, fraying seams, floppy cloth ears, "                 "no cat features.",
  "avatar_toastbrig": "Toastbrig: an enormous plank-faced troll with a broad gentle bureaucratic "                      "expression and a whistling kettle as a helmet.",
  "avatar_duchess": "The Duchess of HA: a tall porcelain-faced lady-doll head with a painted poised "                    "smile, jointed seams at the neck, a brass winding key rising behind one shoulder.",
  "avatar_wisp": "Wisp: a small green-furred courier creature head, long ears, ink-stained smudges, "                 "nervous hopeful expression, waistcoat collar and satchel strap at the frame edge.",
  "avatar_queen": "Queen Malvina the Magnificent: a tall imperious woman with an elaborate small crown, "                  "chin raised, holding a tiny key on a chain between two fingers; printed-poster quality.",
  "avatar_bush": "A leafy woodland bush with a tiny brass trumpet poking out and one wide cartoon eye "                 "peeking between the leaves; humorous, not creepy.",
  "avatar_reflection": "The lake's imitation of Wren: SAME face as the Wren portrait (straight black bob, big eyes) but an unnaturally neat coat collar, a rehearsed smug smile, and a thin silver outline around the figure with a sliver of gilt picture-frame at one side; overprepared, not frightening; no second girl.",
  "avatar_pip": "Pip the usher puppet: a tall SQUARE apple-WOOD head with visible hinged jaw and carved joints, neatly painted eyebrows, green waistcoat, one raised wooden finger; pleased with his own organisation; a carved puppet, not a real child.",
  "avatar_pop": "Pop the usher puppet: a ROUND apple-WOOD face with a visible hinged mouth and carved joints, lively painted eyebrows, purple waistcoat, one wooden hand poised for an unnecessary flourish; about to interrupt his partner; a carved puppet, not a real child.",
  "avatar_gleam": "Chancellor Gleam the court mirror: a handsome silver-framed hinged MIRROR with two "
                 "thin brass arms and a slightly-too-large little crown on his top rail; his reflective "
                 "glass face wears a politely smug expression; bowing posture; no girl in the glass.",
  "avatar_plain_mirror": "The portrait's SUBJECT is the object itself: a small plain hand mirror with a "
                 "simple wooden frame standing on a shelf, no crown, no forms, no ornament; its glass "
                 "shows only soft lamplight. The mirror is the whole portrait, upright, centred.",
  "avatar_mum": "Wren's mum: warm-looking parent, ordinary breakfast clothes, kind attentive smile "
                 "looking just past the viewer; cosy kitchen light; a normal parent, not royal.",
  "avatar_dad": "Wren's dad: kind parent, ordinary breakfast clothes, slightly curious gentle "
                 "expression, listening; crumbs of toast context possible; a normal parent, no badge.",
  "avatar_queen_after_key": "Queen Malvina AFTER the transfer: same theatrical portrait framing, crown "
                 "still on, dignified and cross; the chain at her neck dangles with an OPEN, EMPTY "
                 "clasp — her two hands rest folded, plainly showing nothing is held; comically "
                 "deflated, unhurt. Her hands hold nothing at all.",
}

HINTS = {  # composition guardrails the briefs earned in QC (content stays Fred's)
  "c5_lake_crossing": "ONE single wide scene (not panels, not a grid). The girl steps across wide stones while she and "
    "the cloth rag-doll imp study an open paper map; the grey tabby cat follows on the stones. The "
    "water carries only the girl's OWN reflection, matching her exactly. Three travelling companions, "
    "each seen once.",
  "c5_rehearsal_slates": "The girl and the imitation must be OBVIOUSLY different: the imitation has a "
    "glowing thin silver outline around her whole figure and a spotlessly clean coat; the real girl is "
    "muddy. Exactly one of each, nowhere else in frame.",
  "c6_route_markers": "ONE single wide scene (not panels, not a grid). The girl holds a paper map up against a wooden "
    "EAST ROAD arrow signpost. With her: ONE grey tabby cat, and the rag-doll imp sewn from brown and "
    "cream cloth patches with button eyes. Three companions, one of each, all clearly themselves.",
  "c6_clock_entrance": "The arriving party: the girl, her grey tabby cat, and the rag doll sewn from brown and cream "
    "cloth patches with mismatched button eyes — three companions, each appearing exactly once, all in "
    "their own colours.",
  "c6_mirror_welcome_hook": "A corridor of tall crowned mirrors on hinged bases; one mirror bows "
    "at its hinge — the FRAME bows, furniture, not a person. ONE real girl, her grey tabby cat and "
    "her cloth rag-doll imp walk the corridor together, all three visible. Each mirror glass holds "
    "one single image of the real girl, matching her pose; the crowned frames themselves bow."  "reward_c5": "COMPOSITION: one single girl stands on the bank, waving down at the water. Beside "
    "her ONLY her grey tabby cat. The water's surface mirrors the girl and the cat. The girl appears "
    "exactly ONCE above the waterline; any second image of her exists ONLY inside the water. No other "
    "person, child or figure stands on the bank.",
  "c7_mirror_court": "ONE single wide scene. The only travellers: the girl in the blue coat, her grey tabby cat (small, "
    "fur), and the rag-doll imp (knee-high, sewn from brown and cream cloth patches, button eyes) — "
    "three separate beings, each appearing exactly once. Every mirror shows only the ordinary "
    "reflection of the corridor and its three travellers. No figures stand inside or behind the glass.",
  "c7_audience_card": "The card is held forward by two thin brass mirror-arms; the girl, the cat and "
    "the rag imp stand opposite, one instance each.",
  "c8_clock_court": "The audience chairs are filled ONLY by FLAT PAINTED spectators on backdrop "
    "panels — nobody else stands in the room but the queen on her wheeled throne, the girl, her grey "
    "tabby cat and the small rag imp. Mirrored walls show ordinary reflections only.",
  "c8_key_presentation_worn": "The QUEEN is the tall crowned woman on the wheeled throne-stage: she "
    "lifts the chained key while the chain still hangs around HER neck, and the lectern cushion stays "
    "empty. The girl waits at the lectern's near side with empty hands, beside her grey tabby cat and "
    "the rag imp holding an open booklet. One queen, one girl, one key, on the queen's chain.",
  "c8_key_presentation_cushion": "The Minute Key lies on the lectern's purple cushion, glowing gently. "
    "On her stage behind, the QUEEN holds both hands out for applause; around her neck hangs a chain "
    "with an open, EMPTY clasp. The girl stands at the walkway with her grey tabby cat and the rag "
    "imp. Around the clock keyhole: a plain dark wall. One queen, one girl, one key on the cushion.",
  "c7_borrowed_words": "The only human in the picture is ONE girl standing on the near side of a tall "
    "doorway holding a paper diagram. On the far side of the doorway walk only animals: her grey tabby "
    "cat mid-meow with a little speech sparkle, and a rag-doll imp. Pawprints cross the threshold. "
    "Every figure appears exactly once.",
  "c8_queen_last_audience": "ONE single wide scene: the girl, her grey tabby cat and the rag imp seen "
    "from behind, walking down the service passage together; ahead, the queen alone on her stage "
    "reaching for the applause handle. Exactly one girl, standing, seen once.",
  "c8_homeward_map": "A folded paper map fills the frame, its glowing route ribbon winding through "
    "painted memory vignettes; the real girl, cat and imp walk small on the road; one girl.",
  "c8_doorway_goodbye": "The girl sitting on moss in a doorway holding ONLY her grey tabby cat; the "
    "hallway beyond is empty of people; no mirrors anywhere, one girl.",
  "c8_world_resumes": "LOW ANGLE at kitchen-floor level: a fallen spoon lying on the boards in the foreground, a pair of muddy green wellington boots and a grey tabby cat just stepping over the threshold in the middle distance, warm sunlit floorboards. In the soft-focus background hang a wall clock at 8:17 with its second hand sweeping and a window where a pigeon is mid-wingbeat. Torsos and heads of any other people stay out of frame above the shot; at most the hem of an apron and a trouser leg stand at the far edge.",
  "c8_home_table": "Breakfast-table hug: the girl, her mum, her dad and the cat, exactly those four "
    "living beings, warm ordinary light; no mirrors in the room.",
  "c8_paw_on_hand": "Close warm scene of a hand resting beside a breakfast plate with a cat's paw on "
    "it; the girl's face partly visible, calm; only one person.",
  "c8_last_page": "Bedroom at dusk: the girl writing in a notebook with the cat curled against her "
    "leg; a paper star tucked by the bedhead; no mirrors, one girl.",
  "reward_c8_queen": "The queen on her stage with an EMPTY chain at her neck, the empty lectern "
    "cushion beside her; two wooden hands giving a slow tiny clap; she is cross and comic, unhurt.",
  "reward_c8_home": "The girl hugging her grey tabby cat at the kitchen doorway, both boots muddy, "
    "family breakfast warm behind her; one girl, one cat.",  "c5_lake_wave": "Calm lakeside after the crossing. ONE real girl stands at the water's edge waving; her OWN "
    "reflection in the water waves back with her — same bobbed hair, blue coat, muddy boots. Her grey "
    "tabby cat sits at her feet. The girl exists exactly once in the air; the only second image of her "
    "is her water reflection.",
  "c5_perfect_frames": "Exactly three gilt-framed paintings on tall stands by the stone route. EVERY frame contains the "
    "SAME girl: black bobbed hair, blue coat. Frame one: she polishes a boot with a brush. Frame two: "
    "she stands alone under falling confetti holding a broom. Frame three: she holds an open compass "
    "ringed by contradictory arrows. Inside each frame there is one girl and nothing else; all three "
    "painted girls are her. On the path below the frames stand the real girl, her grey tabby cat, and "
    "the cloth rag-doll imp looking up at the paintings. Three frames total.",

}

def prompt_for(art_id, text):
    if art_id.startswith("avatar_"):
        desc = AVA_DESC.get(art_id, "")
        return STYLE + ("A single-character portrait, head and shoulders, the named subject's face and "                        "shoulders filling most of the frame, neutral dark background. No other "                        "characters, no girl, no child, no bystanders. ") + desc + " " + text
    return STYLE + cast_for(text) + text + (" " + HINTS[art_id] if art_id in HINTS else "")

def cast_for(text):
    tl = text.lower()
    extra = []
    for keys, d in CHARS:
        if not any((re.search(k[1:], tl) if k.startswith("~") else (k in tl)) for k in keys): continue
        d = d(tl) if callable(d) else d
        if d and d not in extra: extra.append(d)
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

EXTRA_PROMPTS = {
  # local plates requested by playtest, pending a register entry. When an id below
  # also exists in the register its brief is REPLACED here: the register's "two
  # scene variants" briefs are grid-makers — the model paints every variant at once
  # and duplicates the cast across panels.
  "c5_lake_crossing": "Calm shallow lake crossed by wide flat stepping stones. One girl in a blue "
    "coat stands mid-crossing holding an open paper map; the rag-doll imp sewn from brown and cream "
    "cloth patches stands on the next stone pointing at the map; a grey tabby cat follows along the "
    "stones. The still water carries each traveller's own reflection, matching them exactly. A dry "
    "path and an orchard track ahead, morning mist. No text.",
  "c5_lake_wave": "Calm lakeside after the crossing. The girl stands at the water's edge waving at "
    "the water; her own ordinary reflection waves back. The grey tabby cat sits at her feet watching "
    "the ripples. Beyond, the far bank and a path of apple trees in early leaf. Mist soft on the lake, "
    "morning light. No text.",
}

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
        if aid in EXTRA_PROMPTS: brief = " ".join(EXTRA_PROMPTS[aid].split())
        jobs.append((aid, brief, True))
    painted = {j[0] for j in jobs}
    for aid, brief in EXTRA_PROMPTS.items():
        if aid not in painted:
            jobs.append((aid, " ".join(brief.split()), True))
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
    W, H = (768, 768) if art_id.startswith("avatar_") else (WIDTH, HEIGHT)
    return {
      "1": {"class_type": "UNETLoader", "inputs": {"unet_name": UNET, "weight_dtype": "default"}},
      "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": CLIP, "type": "qwen_image"}},
      "3": {"class_type": "VAELoader",  "inputs": {"vae_name": VAE}},
      "4": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": prompt_for(art_id, text) +
            (LETTER if want_text else "")},
      },
      "5": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0],
            "text": NEG.replace("text, letters, ", "") if want_text else NEG}},
      "6": {"class_type": "EmptyLatentImage", "inputs": {"width": W, "height": H, "batch_size": 1}},
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
