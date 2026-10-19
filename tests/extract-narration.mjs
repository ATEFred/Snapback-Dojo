// Extract every spoken story line exactly as the engine would voice it.
// Mirrors drawQuestBeat's read-aloud: say.lines, chal setup+pre+line; sfx skipped;
// SPK_VOICE aliases resolved; personas without a STORY_VOICES entry are left to
// the browser ("bully") and skipped here — except we record them for the tally.
import { readFileSync, writeFileSync } from "node:fs";

const src = readFileSync(new URL("../index.html", import.meta.url), "utf8");
const body = src.split("<script>")[1].split("</script>")[0];
const endMark = ["/* ---- v2 runner", "/* ---- runner"].map(m => body.indexOf(m)).filter(i => i >= 0)[0];
const seg = body.slice(body.indexOf("const QUESTS"), endMark);
const QUESTS = eval(seg + "; QUESTS");

const SPK_VOICE = {troll:"tb", woman:"duch", duchess:"duch", courier:"wisp", bat:"echo",
  tallfig:"pip", tallpup:"pip", roundfig:"pop", roundpup:"pop"};
// personas the browser can voice but the cast cannot (stay browser voices)
const BROWSER_ONLY = new Set(["queen","cvoice","vbush","pmirror"]);
const CAST = new Set(["narr","wren","pet","echo","wisp","pip","pop","gleam","qvoice","mv","mv2","mum","dad","refl","tb","duch"]);

const pp = t => String(t).replace(/\{pet\}/g, "Noodle");
const speakable = t => pp(t).replace(/[→←↑↓↔↕]/g," ").replace(/\s*·\s*/g,", ").replace(/\s+/g," ").trim()
                             .replace(/[\u201C\u201D]/g,'"');
const fold = t => String(t).replace(/[\u201C\u201D]/g,'"');

// Coach notes fall back to these canned lines when the AI adds no "why".
const QWHY_SRC = src.match(/const QWHY = \{[\s\S]*?\};/);
const QWHY = QWHY_SRC ? eval("({\n" + QWHY_SRC[0].replace(/^const QWHY = \{/, "").replace(/\}[;]?\s*$/, "}") + ")") : {};

const lines = [];
const push = (v, t, beat) => {
  const code = SPK_VOICE[v] || v;
  if (!CAST.has(code)) { if (t) lines.push({v:code, t:speakable(t), b:beat, browser:1}); return; }
  lines.push({v:code, t:speakable(t), b:beat});
};
for (const ch of QUESTS) {
  const walk = (list, phase) => list.forEach(b => {
    if (b.t === "say" && b.lines) b.lines.forEach(l => { if (l[0] !== "sfx") push(l[0], l[1], b.id); });
    if (b.t === "chal" || b.t === "btns") {
      if (b.setup) push("narr", b.setup, b.id);
      if (b.pre) b.pre.forEach(l => { if (l[0] !== "sfx") push(l[0], l[1], b.id); });
      if (b.line) {
        const tc = SPK_VOICE[b.spk] || b.spk || "";
        push(CAST.has(tc) ? tc : "bully", b.line, b.id);
      }
      if (b.lines) b.lines.forEach(l => { if (l[0] !== "sfx") push(l[0], l[1], b.id); });
    }
    // Feedback screens (fbSpeak): every canned string the engine can voice there.
    const tc = SPK_VOICE[b.spk] || b.spk || "";
    const vSpk = CAST.has(tc) ? tc : "bully";            // f.v wears the beat's villain
    const segs = arr => { if (Array.isArray(arr)) arr.forEach(l => { if (l[0] !== "sfx") push(l[0], l[1], b.id); }); };
    const w = b.win || {};
    segs(w.fb);
    ["senB","senOk","senFeel","senR","senSrc"].forEach(k => { if (w[k]) push("pet", w[k], b.id); });
    if (w.feelOnly){ segs(w.feelOnly.fb); if (w.feelOnly.c) push("pet", w.feelOnly.c, b.id); }
    segs(b.quietFb);
    if (b.pkgs) Object.keys(b.pkgs).forEach(k => {
      const pk = b.pkgs[k] || {};
      if (pk.stage) push("narr", pk.stage, b.id);
      if (pk.v) push(vSpk, pk.v, b.id);
      if (pk.c) push("pet", pk.c, b.id);
    });
    if (b.opts) b.opts.forEach(o => {
      segs(o.fb);
      if (o.out) push("narr", o.out, b.id);
      if (o.ech) push(vSpk, o.ech, b.id);
      if (o.wrn) push("wren", o.wrn, b.id);
      if (o.sen) push("pet", o.sen, b.id);
    });
    if (b.revLines) Object.keys(b.revLines).forEach(k => push("pet", b.revLines[k], b.id));
    if (b.duelRetry) push("pet", b.duelRetry, b.id);
    if (b.helpCue) push("pet", b.helpCue, b.id);
    segs(b.help);
    if (b.helpOut) push("narr", b.helpOut, b.id);
    if (b.helpSen !== undefined) push("pet", b.helpSen, b.id);
    if (b.borrowL) push("wren", b.borrowL, b.id);
    if (b.bestEx && b.bestEx[0]) push("wren", b.bestEx[0], b.id);  // spoken when borrowed
    if (b.altFbs) b.altFbs.forEach(arr => segs(arr));              // btns loop feedback
  });
  walk(ch.intro || [], "intro");
  (ch.scenes || []).forEach(sc => walk(sc.beats || [], "scene"));
  walk(ch.outro || [], "outro");
}
// Fixed engine lines (constants in qsSend / qsHelp / fbSpeak fallbacks).
push("pet", "Aim at the way she's using power, not a personal wound.", "engine");
push("pet", "The thinking-clock is resting. Your line is safe with me — send it again in a moment, or a grown-up can check it against the note below.", "engine");
push("pet", "Help is always allowed.", "engine");
push("pet", "You can do better than that — that reply gave him a reason to carry on.", "engine");
push("wren", "{pet}, help me with this?", "engine");
Object.keys(QWHY).forEach(k => push("pet", QWHY[k], "qwhy"));
const uniq = new Map();
for (const l of lines) if (!l.browser && l.t) uniq.set(l.v + "|" + l.t, l);
const browserSkips = lines.filter(l => l.browser).length;
writeFileSync(new URL("./narration.json", import.meta.url),
  JSON.stringify([...uniq.values()], null, 0));
const tally = {};
for (const l of uniq.values()) tally[l.v] = (tally[l.v]||0)+1;
console.log("unique cast lines:", uniq.size, "| browser-only lines:", browserSkips);
console.log(tally);
