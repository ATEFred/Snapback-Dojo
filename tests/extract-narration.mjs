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
const BROWSER_ONLY = new Set(["tb","duch","queen","cvoice","vbush","pmirror"]);
const CAST = new Set(["narr","wren","pet","echo","wisp","pip","pop","gleam","qvoice","mv","mv2","mum","dad","refl"]);

const pp = t => String(t).replace(/\{pet\}/g, "Noodle");
const speakable = t => pp(t).replace(/[→←↑↓↔↕]/g," ").replace(/\s*·\s*/g,", ").replace(/\s+/g," ").trim()
                             .replace(/[\u201C\u201D]/g,'"');
const fold = t => String(t).replace(/[\u201C\u201D]/g,'"');

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
  });
  walk(ch.intro || [], "intro");
  (ch.scenes || []).forEach(sc => walk(sc.beats || [], "scene"));
  walk(ch.outro || [], "outro");
}
const uniq = new Map();
for (const l of lines) if (!l.browser && l.t) uniq.set(l.v + "|" + l.t, l);
const browserSkips = lines.filter(l => l.browser).length;
writeFileSync(new URL("./narration.json", import.meta.url),
  JSON.stringify([...uniq.values()], null, 0));
const tally = {};
for (const l of uniq.values()) tally[l.v] = (tally[l.v]||0)+1;
console.log("unique cast lines:", uniq.size, "| browser-only lines:", browserSkips);
console.log(tally);
