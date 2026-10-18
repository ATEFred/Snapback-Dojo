#!/usr/bin/env python3
"""Snap Back Dojo — pre-generate the story narration in the approved cast voices.

Reads voicedemo/narration.json (tests/extract-narration.mjs — every line the
engine would read aloud, normalised the same way) and renders each unique
(persona, line) once into quest-audio/, keyed by "<persona>|<text>" in
quest-audio/manifest.json. The app plays a manifest hit instead of synthesising
and falls back to browser voices for anything missing.

Resumable: existing files are skipped. Rerun after editing voices or lines.

Usage:
  python3 gen_narration.py            # everything missing
  python3 gen_narration.py --limit 5  # smoke test
"""
import hashlib, json, subprocess, sys, time
from pathlib import Path
import gen_voices as V

OUT = V.HERE / "quest-audio"
LIST = V.HERE / "tests" / "narration.json"
MANIFEST = OUT / "manifest.json"

# persona -> how to voice it. clones ride a reference WAV + its .txt transcript;
# golden voices clone the take Fred approved (voicedemo/<v>-1.wav, anchor text
# = that take's line from the CAST sheet).
CLONES = {"narr": "british_narrator", "wren": "irene", "pet": "daddy", "refl": "maya",
          "qvoice": "mummy_long", "mv": "mummy", "mv2": "mummy", "dad": "daddy_clone"}
GOLDEN = ["echo", "gleam", "wisp", "pip", "pop", "mum"]

def normalize(path):
    """One loudness for the whole cast — the clones and designs arrive at wildly
    different levels (the Narrator is ~10x quieter than Wren)."""
    tmp = path.with_suffix(".norm.wav")
    try:
        subprocess.run(["ffmpeg","-y","-loglevel","error","-i",str(path),
                        "-af","loudnorm=I=-16:TP=-1.5:LRA=11","-ar","24000",str(tmp)], check=True)
        tmp.replace(path)
    except Exception:
        tmp.unlink(missing_ok=True)   # keep the raw take rather than lose audio

def anchor_text(voice):
    return next(c[3][0] for c in V.CAST if c[0] == voice)

def main():
    args = sys.argv[1:]
    limit = int(args[args.index("--limit") + 1]) if "--limit" in args else None
    lines = json.loads(LIST.read_text())
    OUT.mkdir(exist_ok=True)
    man = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    # personas that appear -> make sure their golden anchor is on the server
    need_gold = {l["v"] for l in lines} & set(GOLDEN)
    for v in sorted(need_gold):
        src = V.HERE / "voicedemo" / f"{v}-1.wav"
        assert src.exists(), f"golden anchor missing: {src}"
        if V.upload(f"snapback-golden-{v}.wav", src.read_bytes()):
            print(f"golden uploaded: {v}")
        else:
            sys.exit(f"golden upload failed for {v}; nothing rendered")
    todo = [l for l in lines if f'{l["v"]}|{l["t"]}' not in man]
    if limit: todo = todo[:limit]
    print(f"{len(lines)} unique lines, {len(todo)} to render")
    longest = max(lines, key=lambda l: len(l["t"]))
    print("longest line:", len(longest["t"]), "chars")
    n = 0
    for l in todo:
        key, text, voice = f'{l["v"]}|{l["t"]}', l["t"], l["v"]
        if voice in CLONES:
            audio = V.PRESET[CLONES[voice]]
            wf = V.clone_wf(text, audio, V.ref_text(audio), 4242,
                            f"qwen3_tts/narration/{voice}-{int(time.time()*1000)%10**9}")
        elif voice in GOLDEN:
            wf = V.clone_wf(text, f"snapback-golden-{voice}.wav", anchor_text(voice), 4242,
                            f"qwen3_tts/narration/{voice}-{int(time.time()*1000)%10**9}")
        else:
            continue
        f = V.render(wf, key[:60], retries=2)
        if not f:
            print(f"  ✗ gave up on {voice}: {text[:60]}")
            continue
        name = f"{voice}-{hashlib.sha1(text.encode()).hexdigest()[:12]}.wav"
        if V.download(f, OUT / name):
            normalize(OUT / name)
            man[key] = name
            MANIFEST.write_text(json.dumps(man, ensure_ascii=False))
            n += 1
            if n % 10 == 0 or n == len(todo):
                print(f"  … {n}/{len(todo)}")
        else:
            print(f"  ✗ download failed: {text[:60]}")
    print(f"rendered {n}, manifest now {len(man)} entries")

if __name__ == "__main__":
    main()
