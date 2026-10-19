#!/usr/bin/env python3
"""Snap Back Dojo — cast voices on the 5090 ComfyUI box (Qwen3-TTS nodes).

Three casting methods:
  clone:<preset>  — voice clone; the reference WAV lives in the server's
                    input/ folder, its transcript in <name>.txt next to it
                    (fetched automatically, empty falls back to timbre-only).
  design          — voice DESIGN from a written casting note.
  GOLDEN set      — design voices that must stay consistent across lines:
                    take 1 is designed once and becomes the golden anchor,
                    every other line is a CLONE of it (design invents a new
                    voice per request; cloning one golden take does not).

Usage:
  python3 gen_voices.py                 # every voice
  python3 gen_voices.py echo wren       # only these ids
  python3 gen_voices.py mv --alt 3      # three seed-rolled takes per line
  python3 gen_voices.py echo --reanchor # design a new golden take 1

Outputs: voicedemo/<id>-<n>[-aK].wav + voicedemo/index.html (playlist).
Nothing leaves the LAN. Model loading and generation happen on fredhpc2.
"""
import json, re as _re, sys, time, urllib.error, urllib.request, uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT  = HERE / "voicedemo"
COMFY = "http://fredhpc2:8188"

# Clone presets: the WAV in the server's input/ folder. Transcripts are read
# from <name>.txt next to it on the server ("" falls back to timbre-only).
PRESET = {
    "british_narrator": "british-reference.wav",
    "irene":      "irene-early-full-reference.wav",
    "maya":       "maya_clone_reference.wav",
    "daddy":      "daddy_sample2_clone_reference.wav",
    "mummy_long": "mummy-long-speaker-reference.wav",
    "mummy":      "mummy_clone_reference.wav",
    "daddy_clone": "daddy_clone_reference.wav",
}

# Designed voices that must not change accent/timbre between lines:
# take 1 becomes the golden anchor, later lines clone it.
GOLDEN = {"echo", "gleam", "wisp", "tb", "duch"}

CAST = [
    ("narr", "clone:british_narrator", None, [
        "At seventeen minutes past eight, Wren was looking for her other boot.",
        "The clock stopped ticking. A spoon stopped halfway to the floor.",
        "Wren looked back at the lake. Her real reflection had muddy boots, a crooked coat, and a map corner sticking out of her pocket.",
    ]),
    ("wren", 'clone:irene', None, [
        "Why aren't we stopped? Why can you talk?",
        "Then I'm finding her. I want everyone back.",
        "That explains the smugness.",
    ]),
    ("pet", 'clone:daddy', None, [
        "Excellent. A qualified cat.",
        "Or we could finish our walk. A neglected possibility.",
    ]),
    ("echo", "design", 'A small cave-dwelling creature: rasping, croaking, throaty little voice, wet and scratchy, hissing s sounds and sudden gleeful squeaks. Mutters and repeats the ends of its own sentences, slithery sing-song rhythm, itching with mischief.', [
        "Well? What have you got to say for yourself?",
        "You can't lose a contest you won't enter.",
    ]),
    ("refl", 'clone:maya', None, [
        "We could start again. This time, properly.",
        "Most of that was luck. Name one thing you've actually done right.",
    ]),
    ("pip", "design", "A pompous little wooden usher puppet: nasal, clipped and puffed up with "
        "self-importance, each word tapped out like a typewriter key. Desperately eager to be judged "
        "the clever one.", [
        "Pip. Royal usher. Lead performer.",
        "Another big hero who needs directions to a sign.",
    ]),
    ("pop", "design", "A rounder, jollier wooden puppet, half a step slower than his brother: warm, "
        "pleased with every contest, dimpled with laughter in the middle of sentences.", [
        "Pop. Royal usher. Better performer.",
        "No, let me guess. Follow the cat and hope?",
    ]),
    ("gleam", "design", 'A deeply ominous museum collector: very low, soft and unhurried, never raising the volume, with a dark, foreboding undercurrent. Quiet menace, amused cruelty, the kind of pleasant voice that makes the room go cold. British, measured, dangerous.', [
        "We have quite a collection.",
        "Only tradition. And a short acceptance speech.",
    ]),
    ("qvoice", 'clone:mummy_long', None, [
        "Who put a clock in my clock room?",
        "Move the throne forward. A little more. No, I should be larger than the clock.",
    ]),
    ("mv", 'clone:mummy', None, [
        "Queen Malvina the Magnificent. You may begin being impressed.",
        "You're supposed to be embarrassed.",
    ]),
    ("wisp", "design", 'A nervous courier creature with a very high, thin, scratchy squeak: fast, jittery, breathless, a raspy edge to the top notes, words tumbling over each other like papers from a satchel, quick to apologise and quicker to continue.', [
        "Oh! You're her. The girl in the headline.",
        "I can do directions. How newsworthy are they?",
    ]),
    ("mum", "design", "A warm British mother mid-morning: unhurried, kind, a small tired smile in "
        "every line, the voice of someone already late who still kneels down to say hello.", [
        "Morning, Wren. Found your other boot?",
        "Oh, love. Come here.",
    ]),
    ("tb", "design", "A big bluff bridge-troll wearing a guard's helmet two sizes too small: "
        "a booming, blustering bark of a voice, gravelly and loud, barking made-up rules like "
        "they are state affairs. Pompous but comic, never truly frightening; a British bully-boulder.", [
        "BOOT INSPECTION!",
        "HALT. Those boots aren't adventure boots.",
    ]),
    ("duch", "design", "A grandiose duchess who owns the stage: rich, drawling vowels, a purr of "
        "condescension, delighting in her own jokes before she tells them. Vain, showy, theatrical "
        "— as if the audience were a single reviewer she is determined to win over.", [
        "And now, my funniest joke!",
        "My reviews are excellent.",
    ]),
    ("dad", "clone:daddy_clone", None, [
        "Quite a morning?",
    ]),
]


def _req(path, data=None, timeout=30, raw=None, ctype="application/json"):
    headers = {"Content-Type": ctype} if data is not None or raw is not None else {}
    req = urllib.request.Request(COMFY + path, data=raw if raw is not None else
        (json.dumps(data).encode() if data is not None else None),
        headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return 0, str(e).encode()

_tr_cache = {}
def ref_text(audio_name):
    """Transcript of a reference take, from <name>.txt beside it on the server."""
    if audio_name in _tr_cache: return _tr_cache[audio_name]
    base = audio_name.rsplit(".", 1)[0]
    st, body = _req(f"/view?filename={base}.txt&type=input")
    txt = body.decode("utf-8", "replace").strip() if st == 200 else ""
    _tr_cache[audio_name] = txt
    return txt

def upload(name, data):
    """Put a golden anchor WAV into the server's input/ folder."""
    b = uuid.uuid4().hex
    body = (f"--{b}\r\nContent-Disposition: form-data; name=\"image\"; filename=\"{name}\"\r\n"
            f"Content-Type: audio/wav\r\n\r\n").encode() + data + f"\r\n--{b}--\r\n".encode()
    # ComfyUI's only input-upload route is /upload/image; it takes any file type
    st, resp = _req("/upload/image?overwrite=true", raw=body,
                    ctype=f"multipart/form-data; boundary={b}", timeout=60)
    return st == 200

def design_wf(line, note, seed, prefix):
    return {
        "1": {"class_type": "Qwen3TTSVoiceDesign", "inputs": {
            "text": line, "instruct": note, "language": "English",
            "candidate_count": 1, "seed": seed}},
        "2": {"class_type": "SaveQwen3TTSAudio", "inputs": {
            "audio_batch": ["1", 0], "filename_prefix": prefix,
            "number_candidates": False}},
    }

def clone_wf(line, audio, text, seed, prefix):
    return {
        "1": {"class_type": "LoadAudio", "inputs": {"audio": audio}},
        "2": {"class_type": "Qwen3TTSVoiceClone", "inputs": {
            "reference_audio": ["1", 0], "reference_text": text,
            "text": line, "language": "English", "seed": seed}},
        "3": {"class_type": "SaveQwen3TTSAudio", "inputs": {
            "audio_batch": ["2", 0], "filename_prefix": prefix,
            "number_candidates": False}},
    }

def render(wf, tag, retries=1):
    for attempt in range(retries + 1):
        status, body = _req("/prompt", {"prompt": wf, "client_id": "snapback-voices"})
        if status != 200:
            print(f"    ✗ submit failed ({status}): {body[:300]!r}")
            time.sleep(3); continue
        pid = json.loads(body)["prompt_id"]
        t0 = time.time()
        while time.time() - t0 < 420:
            time.sleep(2)
            s2, h2 = _req(f"/history/{pid}")
            if s2 != 200: continue
            hist = json.loads(h2)
            if pid not in hist: continue
            entry = hist[pid]
            outs = entry.get("outputs", {})
            for node in outs.values():
                for key in ("audio", "gifs", "audio_batch"):
                    lst = node.get(key) if isinstance(node.get(key), list) else []
                    for f in lst:
                        if f.get("filename"): return f
            if entry.get("status", {}).get("completed"): break
        print(f"    ✗ no audio back for {tag} (attempt {attempt+1})")
    return None

def download(f, dest):
    q = f"?filename={f['filename']}&subfolder={f.get('subfolder','')}&type={f.get('type','output')}"
    status, body = _req("/view" + q, timeout=60)
    if status == 200 and len(body) > 1000:
        dest.write_bytes(body); return True
    return False

def render_voice(voice, how, note, lines, alt=1, reanchor=False, retries=1):
    ok = 0
    seed0 = 4242
    if how.startswith("clone:"):
        audio = PRESET[how.split(":", 1)[1]]
        text = ref_text(audio)
        for i, line in enumerate(lines):
            for k in range(1, alt + 1):
                wf = clone_wf(line, audio, text, seed0 + i*17 + (k-1)*991,
                              f"qwen3_tts/snapback/{voice}-{i+1}-a{k}-{int(time.time())}")
                f = render(wf, f"{voice}-{i+1} roll {k}", retries)
                if f and download(f, OUT / (f"{voice}-{i+1}.wav" if k == 1 else f"{voice}-{i+1}-a{k}.wav")):
                    print(f"    ✔ {voice}-{i+1}" + (f"-a{k}" if k > 1 else "")); ok += 1
    elif voice in GOLDEN:
        golden = OUT / f"{voice}-1.wav"
        if reanchor or not golden.exists():
            wf = design_wf(lines[0], note, seed0, f"qwen3_tts/snapback/{voice}-anchor-{int(time.time())}")
            f = render(wf, f"{voice} anchor", retries)
            if not f or not download(f, golden):
                print("    ✗ golden anchor failed; skipping voice"); return 0
            print("    ✔ golden anchor redesigned")
        if not upload(f"snapback-golden-{voice}.wav", golden.read_bytes()):
            print("    ✗ golden upload failed"); return 0
        ok += 1
        for i, line in enumerate(lines[1:], start=1):
            for k in range(1, alt + 1):
                wf = clone_wf(line, f"snapback-golden-{voice}.wav", lines[0],
                              seed0 + i*17 + (k-1)*991,
                              f"qwen3_tts/snapback/{voice}-{i+1}-a{k}-{int(time.time())}")
                f = render(wf, f"{voice}-{i+1} roll {k}", retries)
                if f and download(f, OUT / (f"{voice}-{i+1}.wav" if k == 1 else f"{voice}-{i+1}-a{k}.wav")):
                    print(f"    ✔ {voice}-{i+1}" + (f"-a{k}" if k > 1 else "") + " (cloned from golden)"); ok += 1
    else:
        for i, line in enumerate(lines):
            for k in range(1, alt + 1):
                wf = design_wf(line, note, seed0 + i*17 + (k-1)*991,
                               f"qwen3_tts/snapback/{voice}-{i+1}-a{k}-{int(time.time())}")
                f = render(wf, f"{voice}-{i+1} roll {k}", retries)
                if f and download(f, OUT / (f"{voice}-{i+1}.wav" if k == 1 else f"{voice}-{i+1}-a{k}.wav")):
                    print(f"    ✔ {voice}-{i+1}" + (f"-a{k}" if k > 1 else "")); ok += 1
    return ok

LABELS = {"narr":"Narrator","wren":"Wren","pet":"Noodles, the cat","echo":"Echo the Mimic Imp",
    "refl":"The Reflection","pip":"Pip","pop":"Pop","gleam":"Gleam",
    "qvoice":"The Queen (voice, unseen)","mv":"Queen Malvina","wisp":"Wisp",
    "mum":"Mum","dad":"Dad",
    "tb":"Toastbrig (bridge troll · chapter 2)","duch":"The Duchess (chapter 3)"}

def playlist(_unused=None):
    # every take on disk, grouped per character, so alt rolls can be compared
    rows = []; order = []
    for voice, how, note, lines in CAST:
        files = sorted(OUT.glob(f"{voice}-*.wav"), key=lambda f: f.name)
        if not files: continue
        order.append(voice)
        clips = []
        for fp in files:
            mm = _re.match(rf"{voice}-(\d+)(?:-a(\d+))?\.wav", fp.name)
            if not mm: continue
            line = lines[int(mm.group(1)) - 1] if int(mm.group(1)) <= len(lines) else "?"
            roll = f' <span class="roll">take {mm.group(2)}</span>' if mm.group(2) else \
                   (' <span class="roll">golden anchor</span>' if voice in GOLDEN else "")
            clips.append(f'<figure><audio controls preload="none" src="{fp.name}?v={int(fp.stat().st_mtime)}"></audio>'
                         f'<figcaption>“{line}”{roll}</figcaption></figure>')
        if note:
            extra = " — take 1 is the golden anchor the other lines are cloned from" if voice in GOLDEN else ""
            note_h = f'<details><summary>casting note{extra}</summary><p>{note}</p></details>'
        else:
            note_h = f'<p><em>cloned from {PRESET[how.split(":",1)[1]]}'
            note_h += ' (no transcript — timbre-only)</em></p>' if not ref_text(PRESET[how.split(":",1)[1]]) else '</em></p>'
        rows.append(f'<section id="{voice}"><h2>{LABELS[voice]} <small>{how}</small></h2>'
                    f'{note_h}{"".join(clips)}</section>')
    (OUT/"index.html").write_text("""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Snap Back Dojo — cast voices</title><style>
body{background:#181620;color:#efeaf6;font-family:Georgia,serif;max-width:44em;margin:2em auto;padding:0 1em}
h1{font-size:1.5em}section{background:#211e2c;border-radius:12px;padding:1em 1.2em;margin:1em 0}
h2{margin:.2em 0}h2 small{color:#9f93bb;font-size:.55em;font-style:italic}
figure{margin:.9em 0}figcaption{color:#c7bde0;font-style:italic;margin-top:.3em}
.roll{font-style:normal;color:#e6b455;font-size:.85em}audio{width:100%}details{color:#9f93bb}p{color:#c7bde0}
nav{font-size:.9em}nav a{color:#b79be8;margin-right:.7em}</style></head><body>
<h1>🥋 Snap Back Dojo — the voices</h1>
<p>Cloned voices ride on a reference take + its transcript; designed voices follow a casting note.
Where several takes are offered, pick your favourite.</p>
<p class="nav">""" + " ".join(f'<a href="#{v}">{LABELS[v]}</a>' for v in order) + "</p>"
        + "".join(rows) + "</body></html>")

def main():
    args = sys.argv[1:]
    alt = int(args[args.index("--alt") + 1]) if "--alt" in args else 1
    reanchor = "--reanchor" in args
    wanted = {a for a in args if not a.startswith("--") and a != str(alt)} or {c[0] for c in CAST}
    OUT.mkdir(exist_ok=True)
    for voice, how, note, lines in CAST:
        if voice not in wanted: continue
        print(f"▸ {voice} ({how}{f', {alt} takes' if alt > 1 else ''})")
        render_voice(voice, how, note, lines, alt=alt, reanchor=reanchor)
    playlist()
    print(f"done — playlist at {OUT/'index.html'}")

if __name__ == "__main__":
    main()
