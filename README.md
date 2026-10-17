# 🥋 Snap Back Dojo

A small, self-hosted web app that trains a child to answer a bully's jab with **one short line that ends the
moment** — instead of freezing, spiralling, or escalating. Built for a real 10-year-old, runs entirely on the
home LAN, and grades her typed answers with a local LLM. No cloud, no accounts, no data leaving the house.

The training goal is deliberately narrow: not "win the argument", but **end the scene**. The app drills reflexes
(the line has to be available in under three seconds) and wraps the whole thing in a silly, generous reward
game so it feels like a game she happens to learn from — never like homework about the bad thing at school.

---

## The idea

Insults thrown at kids work because the target either goes quiet or gets upset — both are the reaction the
instigator came for. A comeback that's *playful, flat, or simply closing* gives the attack nothing to land on
and ends the moment in front of the audience. That's a trainable reflex, and like any reflex it needs reps, not
lectures. Snap Back Dojo is the safe room where the reps happen: her device, our machine, at her pace.

## Training modes

| Mode | What happens |
|---|---|
| 📜 **Learn the Moves** | 10 named moves ("forms") with the psychology, example lines, and a say-it-out-loud checklist |
| 🎯 **Daily Drill** | Scenario cards: pick the line that ends it — or type your own and have the AI Sensei grade it |
| ⚡ **Rapid Fire** | The taunt is read aloud; you have ~3 seconds to react. Reflex over analysis. Combos. |
| 👹 **Boss Spars** | Gauntlets against the three villain archetypes (Copycat, Announcer, Gossip) |
| 📕 **Close the Book** | End-of-day ritual: one line about today, one line for next time, then 60 seconds of pure nonsense bubbles so the session *ends* |

## The curriculum (what "good" means)

Ten moves, split into **Fangs** (end the moment) and **Shields** (hold the line when it persists):

- **Fangs:** Parrot · Fog Wall · Flip · Rewrite · Yawn · Pity · Dismissal
- **Shields:** The Loop · The Reporter *(situational)* · The Exit

Plus **The Nuclear Question** quiz: when the "best" lines are the *wrong* ones — fair target vs foul target
(never body, never family, never in front of power, daily targeting is evidence not an audience).

### Sensei grading doctrine

The AI coach ("Sensei") grades typed answers by a strict, opinionated philosophy — this is the soul of the repo:

- **`best`** — the reply ends the scene: replays her own words back, dismisses, delivers a bored verdict,
  playfully flips her attack, or agrees until the insult falls flat. Short. Out loud. Done.
- **`okish`** — safe but doesn't close the door (polite, foggy-but-vague, long). She'll be back in five minutes.
- **`wrong`** — counter-insults (especially body/family), pleading, tattle-threats, or genuinely curious
  "why did you say that?" questions (they hand her the floor back).
- Replies that **concede** the insult are never suggested as improvements.
- Playful mean-bite that flips *her own words* is praised, with the cost noted — it's the real hierarchy of the
  corridor, taught honestly rather than sanitized.
- Tone: sharp, dry, funny **coach** — never therapist voice, never a lecture. A rules-based grader is the
  offline fallback; the AI verdict always overrides it.

50 built-in scenario cards (4-option multiple choice + typed answers), each pinned to a move and a villain
archetype, all hand-reviewed by the model itself for "would this actually land at 10 years old".

## Making it a game (not homework)

- **🪙 Coins** for every answer — even wrong ones (effort pays; wrong answers get a joke, never a red shame-X)
- **🎉 Belt ceremonies** — crossing a rank fires a full-screen confetti celebration with a silly rank line
- **🥚 Prize eggs** after drills, bosses and the book: stickers, rare titles, coin showers
- **🪙 Treasure Grotto** — spend coins on silly titles (shown by her belt), full dojo colour skins, and a
  sticker collection wall
- **🏅 Trophies** — 10 achievements (First Snap, Lightning Tongue, Coin Dragon…) that pay out coins
- **🐱 → 🐅 The dojo pet** — everyone starts with a kitten; every belt evolves it through 8 stages
  (Kitten → Cheeky → Sass → Grin → Cool → Shadow → Tiger-in-Training → **THE TIGER** 👑). Renameable, pettable,
  and its personality changes as it gets more tiger
- **🧒 Ninjas (accounts)** — a picker at launch; each ninja gets their own belt, coins, trophies, streak and
  pet. Progress lives server-side so any device remembers everyone. Legacy single-user data auto-migrates.

## 🌗 The Gloomwood and the Stolen Tomorrow (story mode)

A separate, fictional adventure — deliberately **not** school-flavored, so the corridor never echoes in it.
At seventeen minutes past eight, Queen Malvina stopped Wren's whole world with the Great Clock's Minute Key
and keeps it at her palace. An impossible door (brass leaf handle, plaque: *this was not here yesterday*)
appeared under Wren's stairs; her family is frozen mid-breakfast. Wren and her cat walk through — and on the
other side, **the cat can suddenly talk**. Dry, practical, four paws, zero hidden knowledge: `{pet}` is the
companion *and* the coach (the dojo's 🦉 Sensei stays in the dojo and is untouched by the story). Nobody —
not Wren, not the cat, not anyone they meet — knows why the two of them still move, why the cat speaks, or
who opened the door. Those mysteries stay unexplained by contract. The route and the clock facts come from
signs, the Queen's notice, Echo and Wisp — never from unexplained cat knowledge. Wren's goal is honest:
**get her family back**, not win anyone over.
Over-the-top monsters with sad little problems, Tim-Burton-adjacent in mood: gothic-twilight but never scary,
every villain funnier than they are mean. Frozen people feel no waiting and no harm; there is no countdown.

**The whole book ships — eight chapters to breakfast and back**: Echo the Mimic Imp, Toastbrig the Bridge
Inspector, the Duchess of HA (Comedy Gallery), Wisp and the Royal Copy (Midnight Gazette), the Reflection
at Mirror Lake, Pip & Pop's orchard double act, Chancellor Gleam's Hall of Mirrors, and Queen Malvina's
Last Audience — transcribed from `story-chapters-01-02-rewrite.md`, `story-chapters-03-04.md`,
`story-chapters-05-06.md` and `story-chapters-07-08.md`. The party is Wren, the cat, and (from Chapter 1's
end) Echo. The script names the cat **Noodles** in the finale; every nameplate, mention and button binds
to the player's own pet name. Chapter 8 ends with the spoon falling, breakfast resuming, and one small
ordinary cat chirrup — SOUND ONLY, a caption, never spoken aloud. (The earlier bellkeeper premise and the
path-guide version of the opening remain recoverable in git history.)

- **Every voice wears a nameplate, a face and a voice** — Narrator included. Bubbles carry a painted
  portrait (`quest-art/avatar_*.png`, square, cropped into the circle; emoji fallback until painted), and
  each speaker gets their **own browser voice** (`STORY_VOICES`: Wren high and young, the cat low and dry,
  Toastbrig a rumble, Wisp quick and squeaky… chosen from installed en-GB voices by family, with pitch and
  speed shaping the character even when the machine only has one voice). The read-aloud queues **every
  line** of a beat, not just the last.
- **VISUAL ONLY means visual only.** Signs, notices, badges, prop labels and maps (`story-visual-assets.md`)
  appear on screen — as painted plate when available, as a lettering card otherwise — and are **never**
  narrated or TTS'd; spoken lines merely refer to them ("a rather odd sign"). Branch-specific props and the
  signpost's changed states stay honest lettering cards (asset-id `noimg` / `NOIMG` set), because exact
  lettering must never be left to chance.
- **No failure state.** Every beat advances on a tap. An approved line (grader `okish` or `best`, or an
  action choice like *keep walking*) ticks the villain's **prop meter** — his stars, his wheels, his drawers,
  his casting shutters — never his feelings. A miss shows that choice's specific consequence + one coach
  line, then the same prompt returns in the same shuffled order. No punishments, no escalating rounds of shame.
- **Walking away is always legal:** every encounter carries an ungraded *Leave with {pet}* / *Pause / back
  to map* button (chapters 5–8 put it on every typed beat too, and the finale's quiet bench and doorway
  beats carry it as well); progress saves and the map waits. Choices
  like *take the garden path*, *decline the quote* or *take the palace path* clear beats exactly like words.
- **Two speakers, one answer (chapters 5–6):** Pip and Pop share the bait in labelled bubbles, in order,
  before the answer box opens — they never interrupt her mid-line and nothing reacts to typing speed.
  Answering just one of them is a fine answer. The Reflection is its own speaker: its own nameplate, its
  own over-rehearsed voice, its own silver-outlined portrait — never a diagnosis of Wren.
- **A hurt answer meets kindness, not a bigger attack:** self-belittling lines ("nothing, I'm useless")
  get the quiet accepted branch — the cat sits beside her and the slate turns over gently. Feeling-only
  replies in Chapter 6 skip the puppets' comic bit entirely; borrowed words are hers.
- **Help is free and always on the table, in two stages:** 🐾 *Ask {pet} for help* once and the cat models a
  line — *"You could try: … Or say it your way"* — while the moment stays open and the draft she typed is
  kept; ask again and the cat steps in and walks her through it. 🪄 *Borrow a line* fills the box in one go.
  All routes clear the beat and cost nothing; after the cat has modelled a line, rambling is graded gently.
  Chapters 5–6 use Fred's single-branch version straight from the script: Wren asks, the cat gives the
  beat's exact help cue, Wren speaks the borrowed line, the accepted outcome plays and clears once with
  full reward and no extra coach chatter. Stars are a flourish, not a wage. In story mode the cat is the
  only coach; the dojo's 🦉 Sensei lives outside the book.
- **Freeform answers get heard, not just waved through:** the exact line she wrote comes back on screen as
  Wren's bubble, and the cat adds one short line about *why* it landed (or what to try instead) — the AI's
  note when online, the cat's own book of reasons when offline.
- **The typed grader is lenient by doctrine:** feelings never lose, plain "No" never loses, one useful source
  question ("Who is everyone?") is a *best*, spelling is invisible, and when the AI is offline the fallback
  pattern-grader errs gentle — it never calls an answer wrong on a hunch. Threats and handing the monster
  control of the exit get a funny retry, never a verdict.
- **Kind words with strings (Chapter 7):** Chancellor Gleam's compliments arrive with invoices — a
  statement to sign, a ceremony that "free" gifts come with, a gratitude debt, an apology script to
  learn. "Thank you, but no" is a *best*; a plain kind thank-you to the small plain mirror (who asks
  nothing) is a *best*; agreeing to sign something untrue, or booking her afternoon for approval, is the
  only kind of wrong — answered with Gleam's scripted sputter and the same prompt back. Sitting on the
  bench "a little longer" loops gentle ambience on a button and grades nothing.
- **The hard freeform finale (Chapter 8):** the Queen's last three exchanges are typed-only — no Borrow
  a line, no prewritten choices, no auto-clear after hints. Each line is scored on three things a grown-up
  can read on screen: does it answer *this* taunt, does it make a cutting point, does Wren keep control
  (clear needs a real cutting point plus 5 of 6). A feeling, a bare "Bye", a plain boundary all get
  *revise*: her draft survives on screen for editing and the cat gives one concrete next target — never
  mockery, never a red X, no extra punishment. 🐾 hints scaffold without writing the line; 👂 replays the
  Queen's taunt; a resting model says so honestly and keeps the draft rather than inventing a verdict.
  Clearing turns the key, folds the painted applause, and the long way home plays ungraded — Echo's paper
  star, the world mid-motion again, +80 coins, both farewell stickers, the trophy *The Morning Is Ours*
  and the **Clockstarter** ribbon on the storybook map.
- A bookmark saves mid-story; reopening a chapter resumes exactly where the book was closed.
- Every crossed villain becomes a page in **The Little Book of Former Weirdos** (sticker wall) + a trophy.
- **Story pack export / import / restore** in the parent panel: the entire story (text, taunts, options, coach
  lines, ComfyUI `artPrompt`s) is JSON with stable ids — edit it, import it back, restore anytime. Story
  *progress* is separate and survives story edits and progress resets.
- **Art:** `gen_art.py` paints the **visual asset register** (`story-visual-assets.md` → `quest-art/<asset-id>.png`,
  gitignored, reproducible) plus any `artPrompt` fields via ComfyUI with **Qwen Image 2.1**
  (`qwen_image_2.1_bf16` + Qwen3-VL encoder), shared style anchor + a **per-brief cast** (only characters the
  brief actually names appear; no uninvited guests, no duplicates). The register's *Extra plates* section adds
  scene backdrops for most screens and square avatar faces for every speaker. LAN only, resumable:
  `python3 gen_art.py` (skips existing) · `--only c1_signpost` · `--force` (add `SEED_SALT=2` for a different
  take). The app probes each plate and falls back to card/emoji automatically when a file is missing.

## Grown-up panel (⚙)

- AI / voice settings, capability probe for the local model
- **Add a real phrase** — paste what's actually being said; it becomes a drill card immediately
- **Card editor** — edit taunt/answers/lesson of any card (overlay layer, revert restores the original)
- **Pack export/import (JSON)** — export all 50+ cards, curate them in any text editor, import back
  (matching `id` edits, new `id` adds)
- **Ninjas** — rename/delete accounts; **reset progress** keeps the card pack and settings,
  **reset everything** wipes the dojo
- **Export dojo (all ninjas)** for backup

## Running it

```bash
python3 server.py 8081        # stdlib only — then open http://<host>:8081
```

| Env var | Default | Purpose |
|---|---|---|
| `HALO_BASE` | `http://halo-server:8080` | any OpenAI-compatible endpoint |
| `HALO_CHAT_MODEL` | `Qwen3.8 Flash Next` | Sensei grading model |
| `HALO_TTS_MODEL` / `HALO_ASR_MODEL` | `qwen3-tts` / `qwen3-asr` | optional voice upgrade |

Everything works with no AI configured ("practice mode", rules-based grading). The app **probes capabilities on
boot** and upgrades itself when the endpoint appears: taunts switch from browser `speechSynthesis` to the local
TTS voice (cached per line), and typed answers gain mic dictation via local ASR. The proxy injects
`thinking: {"type": "disabled"}` so grading stays fast (~1 s).

## Architecture

```
index.html   the entire app: content, curriculum, state machine, UI, styles (no build step, no deps)
server.py    stdlib static server + AI proxy + JSON persistence + capability probe
tests/       happy-dom regression suite (see below)
```

- **State** lives in `snapback-data.json` (written atomically with a `.bak` rotation). Shape:
  `{ accounts: { "<name>": { emoji, state } }, active: "<name>" }` — the browser holds it in memory and
  localStorage, and debounces PUTs to the server. First run on an old flat file migrates it into a "Ninja"
  account automatically.
- **No framework** is a deliberate choice: one readable file a parent can fully own and edit.

## Tests

A regression suite runs the real app in [happy-dom](https://github.com/capricorn86/happy-dom) under Deno —
boot, navigation, timers-vs-TTS, AI fallback, grading doctrine, card editor, pack import, coins/shop/ceremony,
pet evolution, accounts and resets (70+ assertions):

```bash
deno run --allow-read --allow-env --allow-net tests/dom-test.mjs
```

The test file embeds a snapshot of `index.html`; after changing the app, refresh it with:

```bash
python3 tests/regen.py        # re-embeds the app, keeps existing test blocks
```

## Privacy

Designed to run on a LAN with no internet access. Progress, custom scenarios (which may contain real phrases
from a real school) and settings never leave the house — and `snapback-data.json` is gitignored precisely so
it can't. The AI, if configured, is your own local model.

## Next steps

**Voice**
- [ ] Register Qwen3-TTS / ASR on the inference server — the app already auto-detects and upgrades
- [ ] Interim fallback: Web Speech API `SpeechRecognition` for dictation where the browser supports it

**App**
- [ ] PWA: installable + offline service worker so it survives router outages and lives on her laptop dock
- [ ] Subtle WebAudio SFX (coin, crack, roar) with a mute toggle
- [ ] A weekly parent digest: stuck scenes, streaks, what to talk about at breakfast
- [ ] Optional PIN lock on the grown-up panel
- [ ] Cyberbullying pack: replies for group-chat / comment-section jabs (same doctrine, typed rather than spoken)

**Content**

- [x] Gloomwood chapters 3–4 (Comedy Gallery + Midnight Gazette — live, per `story-chapters-03-04.md`)
- [x] Chapters 5–6: Mirror Lake + the orchard double act (live, per `story-chapters-05-06.md`)
- [x] Chapters 7–8: the Hall of Mirrors + Her Majesty's Last Audience, the hard freeform finale and the
      Noodles homecoming (live, per `story-chapters-07-08.md`) — the book is finished and replayable
- [x] Re-paint pass: every plate QC'd on sheets; weak ones rerolled with `--force` / `SEED_SALT`, and
      `HINTS` in `gen_art.py` now guards compositions the briefs earned (one real Wren, no uninvited cast)
- [ ] Pre-generated narration: batch-render per-beat TTS audio (quest-audio/<beat-id>), pick per-character
      voices, ship the files; live browser TTS stays the fallback
- [ ] Witness scenarios — what changes when friends are watching (audience-aware drills)
- [ ] Two-kid scenarios (the pair dynamic that matches the real situation at school)
- [ ] Voice-note roleplay: the app speaks the taunt, she answers out loud, ASR + Sensei grade spoken delivery

**Housekeeping**
- [ ] Pick a license for the code (content is personal either way)
- [ ] Split `index.html` into modules only if it keeps growing; prefer readability over structure

---

*Built by a parent, for one specific kid, on a kitchen-server called hades. If the corridor taught her anything
first, let it be this: you are allowed to be the one who ends it.*
