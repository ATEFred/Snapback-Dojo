#!/usr/bin/env python3
"""Snap Back Dojo — narration QC: catch the lines where the model sang off-key.

Every line is cloned from the same reference, but the model occasionally pulls
an individual take off-identity. This fingerprints every rendered file against
its own character's median (fundamental frequency + seconds-per-character),
re-rolls the outliers with fresh seeds (best of 3), and drops entries whose
file went missing so the next gen_narration run fills them.

The fingerprint only catches pitch/pace drift; identity drift that the maths
can't hear goes to the audition page (voicedemo/audit.html) and Fred's ears.

  python3 qc_narration.py                       # scan + fix outliers
  python3 qc_narration.py --report              # scan only, list suspects
  python3 qc_narration.py --reroll "part of line"   # re-render named lines
"""
import json, sys, time, wave, array
from pathlib import Path
import gen_voices as V
import gen_narration as N

OUT = V.HERE / "quest-audio"
MAN = OUT / "manifest.json"
F0_LO, F0_HI = 0.85, 1.20      # × persona median — drift past ±15% is what jars
DPC_LO, DPC_HI = 0.60, 1.75    # seconds-per-char × persona median
MAX_TRIES = 3

def f0(path, frames=8):
    try:
        w = wave.open(str(path)); n = w.getnframes(); sr = w.getframerate()
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
        w = wave.open(str(path)); d = w.getnframes()/w.getframerate(); w.close(); return d
    except Exception:
        return 0

def anchor_f0(voices):
    """The F0 of each persona's APPROVED take — identity is anchored there,
    not to the batch median: when half the takes drift, the median drifts too.
    Golden take (voicedemo/<v>-1.wav) first, clone reference as the fallback."""
    out = {}
    for v in voices:
        wav = V.HERE/"voicedemo"/f"{v}-1.wav"
        if not wav.exists():
            ref = N.CLONES.get(v)
            if not ref: continue
            name = V.PRESET[ref]
            cache = OUT/("_anchor-"+name)
            if not cache.exists():
                st, body = V._req(f"/view?filename={name}&type=input")
                if st != 200: continue
                cache.write_bytes(body)
            wav = cache
        f = f0(wav)
        if f: out[v] = f
    return out

def centers(man, scanned=None):
    """Per persona: (pitch centre, pace centre, batch median pitch, anchor pitch).
    Pitch centres on the approved take; pace stays a median (tempo varies per line)."""
    rows = scanned if scanned is not None else []
    if scanned is None:
        for key, fname in man.items():
            v, text = key.split("|", 1)
            p = OUT/fname
            if p.exists(): rows.append((v, f0(p), dur(p)/max(len(text), 1)))
    anch = anchor_f0({r[0] for r in rows})
    out = {}
    for v in {r[0] for r in rows}:
        f0s = sorted(r[1] for r in rows if r[0] == v and r[1])
        dps = sorted(r[2] for r in rows if r[0] == v and r[2])
        if not f0s or not dps: continue
        mf, md = f0s[len(f0s)//2], dps[len(dps)//2]
        out[v] = (anch.get(v) or mf, md, mf, anch.get(v, 0))
    return out

def reroll(man, key, mf, md, tries=MAX_TRIES):
    """Re-render one line up to `tries` seeds; keep the take nearest the band."""
    voice, text = key.split("|", 1)
    fname = man[key]
    best = None
    for attempt in range(tries):
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
    if not best:
        print(f"  ✗ could not fix: {fname}")
        return False
    best[2].replace(OUT/fname)
    print(f"  ✔ re-rolled: {fname}")
    return True

def write_audit(man, med, top=25):
    """Rank every take by distance from its persona's centre and serve the
    oddest as a playlist — Fred's go/bounce call, not the maths'."""
    try:
        import math, html
        devs = []
        for key, fname in man.items():
            p = OUT/fname
            if not p.exists(): continue
            v, text = key.split("|", 1)
            c = med.get(v)
            if not c: continue
            mf, md = c[0], c[1]
            f_, dpc = f0(p), dur(p)/max(len(text), 1)
            if not f_: continue
            devs.append((abs(math.log(f_/mf)) + abs(math.log(dpc/md)), v, fname, text))
        devs.sort(reverse=True)
        items = "".join(
            f'<div class="t"><span class="v">{v}</span>'
            f'<audio controls preload="none" src="../quest-audio/{fname}"></audio>'
            f'<p>{html.escape(text[:140])}</p></div>'
            for _s, v, fname, text in devs[:top])
        (V.HERE/"voicedemo"/"audit.html").write_text(
            "<meta charset=utf-8><title>Odd takes — final ears</title>"
            "<style>body{font-family:system-ui;background:#141414;color:#eee;max-width:46em;margin:auto;padding:1em}"
            ".t{border-bottom:1px solid #333;padding:.6em 0}.v{color:#ffb;font-weight:bold;margin-right:.6em}"
            "audio{height:2em;vertical-align:middle}p{margin:.3em 0 0;color:#aaa;font-size:.9em}</style>"
            f"<h2>The {min(top,len(devs))} oddest takes after QC</h2>"
            "<p>Sorted furthest from each voice's comfort zone. If one still sounds like a different person, "
            "say its name — <code>python3 qc_narration.py --reroll \"part of the line\"</code> re-rolls it.</p>"
            + items)
        print(f"audition page: voicedemo/audit.html ({len(devs)} takes ranked)")
    except Exception as e:
        print("audit page skipped:", e)

def main():
    man = json.loads(MAN.read_text())
    if "--reroll" in sys.argv:      # --reroll "persona|exact text" | "any words" [...]
        pats = sys.argv[sys.argv.index("--reroll")+1:]
        targets = [k for k in man if any((p in k if "|" not in p else k == p) for p in pats)]
        if not targets:
            print("no manifest key matches:", pats); return
        med = centers(man)
        for k in targets:
            print(f"re-rolling: {k.split('|')[0]}: “{k.split('|',1)[1][:70]}”")
            c = med.get(k.split("|")[0])
            reroll(man, k, c[0] if c else 0, c[1] if c else 0)
        # filenames never change here, only their bytes — no manifest write,
        # so this stays safe to run while gen_narration is filling the batch.
        return
    report = "--report" in sys.argv
    rows = []
    for key, fname in sorted(man.items()):
        voice, text = key.split("|", 1)
        p = OUT / fname
        if not p.exists():
            rows.append((key, voice, fname, 0, 0, "missing"))
            continue
        d = dur(p)
        rows.append((key, voice, fname, f0(p), d/max(len(text), 1), None))
    # centres: approved-take pitch where we have it, batch median pace
    med = centers(man, [(r[1], r[3], r[4]) for r in rows if not r[5]])
    for v, (cf, cd, mf_, af) in sorted(med.items()):
        drift = f"  (batch median {mf_:.0f}Hz)" if af and abs(af-mf_) > 0.08*af else ""
        print(f"  {v}: centre {cf:.0f}Hz" + (f" from approved take{drift}" if af else " (no anchor — batch median)"))
    suspects = []
    for key, v, fname, f_, dpc, err in rows:
        if err == "missing":
            suspects.append((key, fname, err)); continue
        c = med.get(v)
        if not c: continue
        mf, md = c[0], c[1]
        if not (F0_LO*mf <= f_ <= F0_HI*mf) or not (DPC_LO*md <= dpc <= DPC_HI*md):
            suspects.append((key, fname, f"f0={f_:.0f} vs {mf:.0f}Hz, {dpc*1000:.0f} vs {md*1000:.0f}ms/char"))
    print(f"{len(rows)} files, {len(suspects)} suspects")
    for key, fname, why in suspects:
        print(f"  ▸ {fname}  {key.split('|')[0]}: {why}  “{key.split('|',1)[1][:48]}”")
    if report:
        write_audit(man, med)
        return
    fixed = kept = 0
    missing = {k for k in man if not (OUT/man[k]).exists()}
    for key, fname, why in suspects:
        if key in missing:
            man.pop(key); continue   # missing → next gen_narration run re-renders
        if reroll(man, key, med[key.split("|")[0]][0], med[key.split("|")[0]][1]): fixed += 1
        else: kept += 1
    MAN.write_text(json.dumps(man, ensure_ascii=False))
    write_audit(man, med)
    print(f"done — {fixed} re-rolled, {kept} unfixable, manifest {len(man)}")

if __name__ == "__main__":
    main()
