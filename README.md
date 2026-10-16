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

## 📖 The Unbothered Quest (story mode)

A separate, fictional adventure — deliberately **not** school-flavored, so the corridor never echoes in it.
Eight chapters (Chapter 1 ships, the rest land as they're written) of over-the-top monsters with sad little
problems, Tim-Burton-adjacent in mood: gothic-twilight but never scary, every villain funnier than they are
mean. Wren the Unboothered walks the Gloomwood with the dojo pet at her side; Sensei narrates.

- **Battles = 3 taunts, no failure state.** An approved line (Sensei `okish` or `best`) chips the Gloom meter.
  A wrong answer is never a loss — the villain gets *funnier* and you retry the same taunt. Two misses reveal a
  free 🪄 lifeline. There are no walls and no costs for borrowing.
- **Progressive difficulty:** Chapter 1 is all multiple choice; typed answers fade in from Chapter 2, by the
  finale everything is typed (with the lifeline forever available).
- Every defeated villain becomes a page in **The Little Book of Former Weirdos** (sticker wall) + a trophy.
- **Story pack export / import / restore** in the parent panel: the entire story (text, taunts, options, coach
  lines, ComfyUI `artPrompt`s) is JSON with stable ids — edit it, import it back, restore anytime. Story
  *progress* is separate and survives story edits and progress resets.
- **Art hooks:** each scene references `quest-art/<id>.png`; drop images there (later, via your ComfyUI batch)
  and they appear automatically. The story runs happily on emoji art until then.

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

- [ ] Quest chapters 2–8 (arc fully mapped in design notes)
- [ ] ComfyUI scene-art pipeline (`COMFY_BASE` + batch script + `artPrompt` fields, already in the story JSON)
- [ ] Witness scenarios — what changes when friends are watching (audience-aware drills)
- [ ] Two-kid scenarios (the pair dynamic that matches the real situation at school)
- [ ] Voice-note roleplay: the app speaks the taunt, she answers out loud, ASR + Sensei grade spoken delivery

**Housekeeping**
- [ ] Pick a license for the code (content is personal either way)
- [ ] Split `index.html` into modules only if it keeps growing; prefer readability over structure

---

*Built by a parent, for one specific kid, on a kitchen-server called hades. If the corridor taught her anything
first, let it be this: you are allowed to be the one who ends it.*
