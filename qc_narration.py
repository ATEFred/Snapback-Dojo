#!/usr/bin/env python3
"""Snap Back Dojo — narration QC: catch the lines where the model sang off-key.

Every line is cloned from the same reference, but the model occasionally pulls
an individual take off-identity. This fingerprints every rendered file against
its own character's median (fundamental frequency + seconds-per-character),
re-rolls the outliers with fresh seeds (best of 3), and drops entries whose
file went missing so the next gen_narration run fills them.

  python3 qc_narration.py          # scan + fix outliers
  python3 qc_narration.py --report # scan only, list suspects
"""
import json, subprocess, sys, time, wave, array
from pathlib import Path
import gen_voices as V
import gen_narration as N

OUT = V.HERE / "quest-audio"
MAN = OUT / "manifest.json"
F0_LO, F0_HI = 0.72, 1.38     # × persona median
DPC_LO, DPC_HI = 0.60, 1.75   # seconds-per-char × persona median
MAX_TRIES = 3

def f0(path, frames=8):
    try:
        w = wave.open(path); n = w.getnframes(); sr = w.getframerate()
        d = array.array("h", w.readframes(n)); w.close()
    except Exception:
        return 0
    ests = []
    step = max(len(d)//frames, 4096)
    for fi in range(frames):
        s0 = fi*step + step//4
        win = d[s0:s0+4096]
        if len(win) < 2048: continue
        if sum(x*x for x in win)/len(win) < 50000: continue
        best, bl = 0, 0
        for lag in range(int(sr/330), int(sr/70)):
            c = sum(win[i]*win[i+lag] for i in range(0, len(win)-lag, 2))
            if c > best: best, bl = c, lag
        if bl: ests.append(sr/bl)
    ests.sort()
    return ests[len(ests)//2] if ests else 0

def dur(path):
    try:
        w = wave.open(path); d = w.getnframes()/w.getframerate(); w.close(); return d
    except Exception:
        return 0

def render_line(voice, text, seed):
    if voice in N.CLONES:
        audio = V.PRESET[N.CLONES[voice]]
        wf = V.clone_wf(text, audio, V.ref_text(audio), seed,
                        f"qwen3_tts/qc/{voice}-{int(time.time()*1000)%10**9}")
    elif voice in N.GOLDEN:
        wf = V.clone_wf(text, f"snapback-golden-{voice}.wav", N.anchor_text(voice), seed,
                        f"qwen3_tts/qc/{voice}-{int(time.time()*1000)%10**9}")
    else:
        return False
    f = V.render(wf, f"qc {voice}", retries=2)
    if not f: return False
    name = MAN_obj[key_map[seed]] if False else None  # unused
    return f

def main():
    report = "--report" in sys.argv
    man = json.loads(MAN.read_text())
    rows = []
    for key, fname in sorted(man.items()):
        voice, text = key.split("|", 1)
        p = OUT / fname
        if not p.exists():
            rows.append((key, voice, fname, 0, 0, "missing"))
            continue
        d = dur(p)
        rows.append((key, voice, fname, f0(p), d/max(len(text), 1), None))
    # persona medians from the healthy middle of each cast
    med = {}
    for v in {r[1] for r in rows if not r[5]}:
        f0s = sorted(r[3] for r in rows if r[1] == v and not r[5] and r[3])
        dps = sorted(r[4] for r in rows if r[1] == v and not r[5] and r[4])
        if f0s and dps: med[v] = (f0s[len(f0s)//2], dps[len(dps)//2])
    suspects = []
    for key, v, fname, f_, dpc, err in rows:
        if err == "missing":
            suspects.append((key, fname, err)); continue
        mf, md = med.get(v, (0, 0))
        if not mf or not md: continue
        if not (F0_LO*mf <= f_ <= F0_HI*mf) or not (DPC_LO*md <= dpc <= DPC_HI*md):
            suspects.append((key, fname, f"f0={f_:.0f} vs {mf:.0f}Hz, {dpc:.1f} vs {md:.1f}ms/char"))
    print(f"{len(rows)} files, {len(suspects)} suspects")
    for key, fname, why in suspects:
        print(f"  ▸ {fname}  {key.split('|')[0]}: {why}  “{key.split('|',1)[1][:48]}”")
    if report or not suspects:
        return
    fixed = kept = 0
    for key, fname, why in suspects:
        voice, text = key.split("|", 1)
        mf, md = med.get(voice, (0, 0))
        if key in [k for k in man if not (OUT/man[k]).exists()]:
            man.pop(key); continue   # missing → next gen_narration run re-renders
        best = None
        for attempt in range(MAX_TRIES):
            seed = 4242 + (attempt+1)*1331
            wf = (V.clone_wf(text, V.PRESET[N.CLONES[voice]], V.ref_text(V.PRESET[N.CLONES[voice]]), seed,
                             f"qwen3_tts/qc/{voice}-{int(time.time()*1000)%10**9}")
                  if voice in N.CLONES else
                  V.clone_wf(text, f"snapback-golden-{voice}.wav", N.anchor_text(voice), seed,
                             f"qwen3_tts/qc/{voice}-{int(time.time()*1000)%10**9}"))
            f = V.render(wf, f"qc {voice} try {attempt+1}", retries=1)
            if not f: continue
            tmp = OUT/"_qc_try.wav"
            if not V.download(f, tmp): continue
            N.normalize(tmp)
            tf, td = f0(tmp), dur(tmp)/max(len(text), 1)
            score = abs(tf-mf)/mf if mf else 9
            if best is None or score < best[0]: best = (score, tf, tmp)
            else: tmp.unlink()
            if F0_LO*mf <= tf <= F0_HI*mf and DPC_LO*md <= td <= DPC_HI*md:
                break   # back in the band, take it
        if best:
            _, _, tmp = best
            tmp.replace(OUT/fname)
            fixed += 1
            print(f"  ✔ re-rolled into band: {fname}")
        else:
            kept += 1
            print(f"  ✗ could not fix: {fname}")
    MAN.write_text(json.dumps(man, ensure_ascii=False))
    print(f"done — {fixed} re-rolled, {kept} unfixable, manifest {len(man)}")

if __name__ == "__main__":
    main()
