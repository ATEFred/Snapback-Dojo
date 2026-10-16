#!/usr/bin/env python3
"""Re-embed index.html into dom-test.mjs while keeping the existing test blocks.

dom-test.mjs stores the app as one JS string literal:
  document.body.innerHTML = '<markup>'; const APP = '...'; const BODY = '<tests>';
This script re-extracts the markup + script from index.html and replaces the
APP literal (and the markup), leaving BODY — the actual assertions — untouched.

Usage:  python3 tests/regen.py
Then:   deno run --allow-read --allow-env --allow-net tests/dom-test.mjs
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
APP_DIR = HERE.parent


def scan_lit(s, i):
    """i points at an opening quote; return (decoded_string, index_after_close)."""
    q = s[i]; out = []; i += 1
    while True:
        c = s[i]
        if c == "\\":
            nxt = s[i + 1]
            if nxt == "x":
                out.append(chr(int(s[i + 2:i + 4], 16))); i += 4; continue
            if nxt == "u":
                out.append(chr(int(s[i + 2:i + 6], 16))); i += 6; continue
            out.append({"n": "\n", "t": "\t", "r": "\r", "\\": "\\", "'": "'", '"': '"'}.get(nxt, nxt))
            i += 2; continue
        if c == q:
            return "".join(out), i + 1
        out.append(c); i += 1


def find_lit_after(s, marker):
    i = s.index(marker) + len(marker)
    while s[i] in " \t":
        i += 1
    return scan_lit(s, i)


def main():
    test_file = HERE / "dom-test.mjs"
    cur = test_file.read_text()
    body, _ = find_lit_after(cur, "const BODY =")

    src = (APP_DIR / "index.html").read_text()
    app = src.split("<script>", 1)[1].split("</script>", 1)[0]
    markup = src.split("<body>", 1)[1].split("<script>", 1)[0]

    # surface boot errors inside the harness instead of swallowing them
    old_boot = 'if (!DB.active) showPicker();\n})();'
    if old_boot in app:
        app = app.replace(old_boot,
            old_boot[:-3] + '().catch(e=>console.log("BOOT FATAL:", e && e.stack ? e.stack : String(e)));')

    head = cur.split("document.body.innerHTML = ", 1)[0]
    tail = (';\ntry { new Function(APP + BODY)(); }\n'
            'catch(e){ console.log("FATAL:", e && e.stack ? e.stack.split("\\n").slice(0,6).join("\\n") : e); }')
    test_file.write_text(
        head + "document.body.innerHTML = " + repr(markup)
        + ";\nconst APP = " + repr(app)
        + ";\nconst BODY = " + repr(body) + tail)
    print("dom-test.mjs re-embedded from index.html (test blocks kept)")


if __name__ == "__main__":
    main()
