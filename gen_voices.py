#!/usr/bin/env python3
"""Snap Back Dojo — cast voices on the 5090 ComfyUI box (Qwen3-TTS nodes).

Narrator: voice CLONE from a reference take (the "british_narrator" preset —
voice design could not hold a British accent, cloning can). Everyone else:
voice DESIGN from a written casting note.

Usage:
  python3 gen_voices.py              # every voice
  python3 gen_voices.py narr wren    # only these ids
  python3 gen_voices.py --retries 2

Outputs: voicedemo/<id>-<n>.wav + voicedemo/index.html (a listening playlist).
Nothing leaves the LAN. Model loading happens on the ComfyUI machine.
"""
import json, sys, time, urllib.error, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT  = HERE / "voicedemo"
COMFY = "http://fredhpc2:8188"

# The one preset that must match the WAV actually on the server's input/ folder.
PRESET = {
    "british_narrator": {
        "audio": "british-reference.wav",
        "text": ("I've been lucky enough to spend my life exploring the wild "
                 "places of our planet and making films about the creatures that "
                 "live there. In doing so, I've travelled widely around the globe."),
    },
}

# id, how-made, casting note (used as instruct for designs), lines to demo
CAST = [
    ("narr", "clone:british_narrator", None, [
        "At seventeen minutes past eight, Wren was looking for her other boot.",
        "The clock stopped ticking. A spoon stopped halfway to the floor.",
        "Wren looked back at the lake. Her real reflection had muddy boots, a crooked coat, and a map corner sticking out of her pocket.",
    ]),
    ("wren", "design", 'A little girl of about nine, a real child voice: small, light, high and clear, with childlike quick rhythm and easy, unpolished diction. Curious and warm, a touch cheeky; when she is being brave the little voice slows and steadies. A child, not a woman implying a child.', [
        "Why aren't we stopped? Why can you talk?",
        "Then I'm finding her. I want everyone back.",
        "That explains the smugness.",
    ]),
    ("pet", "design", 'An old, unflappable valet cat with a magnificent bass: extremely deep, resonant and full, a rich cello of a voice, as deep as an old butler can grow while staying calm. Slow, dry British delivery over imaginary spectacles; every sentence lands a shade flatter, like an eyebrow raised.', [
        "Excellent. A qualified cat.",
        "Or we could finish our walk. A neglected possibility.",
    ]),
    ("echo", "design", 'A small cave-dwelling creature: rasping, croaking, throaty little voice, wet and scratchy, hissing s sounds and sudden gleeful squeaks. Mutters and repeats the ends of its own sentences, slithery sing-song rhythm, itching with mischief.', [
        "Well? What have you got to say for yourself?",
        "You can't lose a contest you won't enter.",
    ]),
    ("refl", "design", "A young girl's voice gone wrong: the same child pitch, but stiff, rigid and unnaturally precise, every word set down with silver tongs. Glassy, cold, formal diction, a thin chill of contempt underneath, flat affect that never rushes. Unnervingly composed.", [
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
    ("qvoice", "design", "A fearsome queen heard echoing down a corridor: a woman's voice, high, thin and shrill, tightly wound with fury, snapping commands at furniture. Tense, jagged, scarlet with anger; the shrillness of someone who has not been obeyed in years.", [
        "Who put a clock in my clock room?",
        "Move the throne forward. A little more. No, I should be larger than the clock.",
    ]),
    ("mv", "design", "A fearsome ageing queen: a woman's shrill, high, brittle voice, angsty and quick to fury, threatening yet fraying at the edges. Grand announcements that crack into sharp anger; scary the way a rattlesnake is scary. Female, piercing, ungovernable.", [
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
    ("dad", "design", "An easygoing British dad: low, warm, gentle teasing always just under the "
        "surface, as if the whole morning were a small private joke shared with his daughter.", [
        "Quite a morning?",
    ]),
]

def _req(path, data=None, timeout=30):
    req = urllib.request.Request(COMFY + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()
    except Exception as e:
        return 0, str(e).encode()

def workflow(voice, line, seed):
    prefix = f"qwen3_tts/snapback/{voice}-{int(time.time())}"
    if voice == "narr":
        p = PRESET["british_narrator"]
        return {
            "1": {"class_type": "LoadAudio", "inputs": {"audio": p["audio"]}},
            "2": {"class_type": "Qwen3TTSVoiceClone", "inputs": {
                "reference_audio": ["1", 0], "reference_text": p["text"],
                "text": line, "language": "English", "seed": seed}},
            "3": {"class_type": "SaveQwen3TTSAudio", "inputs": {
                "audio_batch": ["2", 0], "filename_prefix": prefix,
                "number_candidates": False}},
        }, None
    note = next(c for c in CAST if c[0] == voice)[2]
    return {
        "1": {"class_type": "Qwen3TTSVoiceDesign", "inputs": {
            "text": line, "instruct": note, "language": "English",
            "candidate_count": 1, "seed": seed}},
        "2": {"class_type": "SaveQwen3TTSAudio", "inputs": {
            "audio_batch": ["1", 0], "filename_prefix": prefix,
            "number_candidates": False}},
    }, None

def render(voice, line, idx, retries=1):
    wf, _ = workflow(voice, line, 4242 + idx * 17)
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
            if "error" in entry or str(entry.get("status", "")) == "error":
                break
            outs = entry.get("outputs", {})
            for node in outs.values():
                for key in ("audio", "gifs", "audio_batch"):
                    for f in node.get(key, []) if isinstance(node.get(key), list) else []:
                        if f.get("filename"):
                            return f
            # a finished history entry with no audio means the node errored
            if entry.get("status", {}).get("completed"): break
        print(f"    ✗ no audio back for line {idx} (attempt {attempt+1})")
    return None

def download(f, dest):
    q = f"?filename={f['filename']}&subfolder={f.get('subfolder','')}&type={f.get('type','output')}"
    status, body = _req("/view" + q, timeout=60)
    if status == 200 and len(body) > 1000:
        dest.write_bytes(body); return True
    return False

def main():
    args = [a for a in sys.argv[1:] if a != "--retries"]
    retries = int(sys.argv[sys.argv.index("--retries")+1]) if "--retries" in sys.argv else 1
    wanted = set(args) or {c[0] for c in CAST}
    OUT.mkdir(exist_ok=True)
    made = {}
    for voice, how, note, lines in CAST:
        if voice not in wanted: continue
        print(f"▸ {voice} ({how}) — {len(lines)} line(s)")
        made[voice] = []
        for i, line in enumerate(lines):
            f = render(voice, line, i, retries)
            if not f: continue
            dest = OUT / f"{voice}-{i+1}.wav"
            if download(f, dest):
                made[voice].append((dest.name, line))
                print(f"    ✔ {dest.name}")
            else:
                print(f"    ✗ download failed for {f['filename']}")
    playlist(made)
    print(f"done — playlist at {OUT/'index.html'}")

def playlist(_made=None):
    # Build from everything on disk, not just this run, so a partial reroll
    # never drops the voices that were already approved on the machine.
    made = {}
    for voice, _how, _note, lines in CAST:
        clips = []
        for i in range(1, len(lines) + 1):
            name = f"{voice}-{i}.wav"
            if (OUT / name).exists(): clips.append((name, lines[i-1]))
        if clips: made[voice] = clips
    rows = []
    labels = {"narr":"Narrator","wren":"Wren","pet":"Noodles, the cat","echo":"Echo the Mimic Imp",
        "refl":"The Reflection","pip":"Pip","pop":"Pop","gleam":"Gleam",
        "qvoice":"The Queen (voice, unseen)","mv":"Queen Malvina","wisp":"Wisp",
        "mum":"Mum","dad":"Dad"}
    for voice, how, note, _ in CAST:
        if voice not in made: continue
        clips = "".join(
            f'<figure><audio controls preload="none" src="{name}?v={int((OUT/name).stat().st_mtime)}"></audio>'
            f'<figcaption>“{line}”</figcaption></figure>' for name, line in made[voice])
        note_h = (f'<details><summary>casting note</summary><p>{note}</p></details>' if note else
                  '<p><em>cloned from the british-reference.wav take (the one Attenborough-style '
                  'design could not reach)</em></p>')
        rows.append(f'<section id="{voice}"><h2>{labels[voice]} <small>{how}</small></h2>'
                    f'{note_h}{clips}</section>')
    (OUT/"index.html").write_text("""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Snap Back Dojo — cast voices</title><style>
body{background:#181620;color:#efeaf6;font-family:Georgia,serif;max-width:44em;margin:2em auto;padding:0 1em}
h1{font-size:1.5em}section{background:#211e2c;border-radius:12px;padding:1em 1.2em;margin:1em 0}
h2{margin:.2em 0}h2 small{color:#9f93bb;font-size:.55em;font-style:italic}
figure{margin:.9em 0}figcaption{color:#c7bde0;font-style:italic;margin-top:.3em}
audio{width:100%}details{color:#9f93bb}p{color:#c7bde0}
nav{font-size:.9em}nav a{color:#b79be8;margin-right:.7em}</style></head><body>
<h1>🥋 Snap Back Dojo — the voices, take one</h1>
<p>Everyone except the Narrator is <em>designed</em> from the casting notes; the Narrator is
<em>cloned</em> from the British reference. Tap through and pick who stays and who recast.</p>
<p class="nav">""" + " ".join(f'<a href="#{v}">{v}</a>' for v in made) + "</p>"
    + "".join(rows) + "</body></html>")

if __name__ == "__main__":
    main()
