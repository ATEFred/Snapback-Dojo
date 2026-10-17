# The Gloomwood and the Stolen Tomorrow

## Chapters 1–2: complete playable script

Proposed replacement opening for story mode. This is a new script, not an edit to the shipped story pack. Character and encounter IDs below are proposed IDs for implementation. The original `plannedstory.md` remains unchanged.

**Player character:** Wren, a ten-year-old girl from an ordinary present-day home. The player chooses her words and actions; the story uses her name rather than switching between Wren and “you.” **Cat companion and coach:** `{pet}`, Wren's own cat, using the player's pet name and current feline evolution art. At home the cat only makes ordinary cat sounds. After Wren and the cat cross the magic door, the cat unexpectedly speaks. The cat stays on four paws, has a dry, practical personality, and discovers this world alongside Wren. There is no separate adult guide or Sensei character in these four chapters. **Narrator:** a separate storyteller who describes events, not an unseen coach. **Setting:** our world first, then the strange twilight Gloomwood. Home and school appear only to establish the frozen world; encounters and comeback practice happen entirely in the fantasy world.

**The adventure:** Time stops at 8:17 on an ordinary morning. Wren's family, her street, and her school are frozen in place. Only Wren and her cat seem able to move; neither knows why. A door appears in a blank wall of her house. It opens into the Gloomwood, where the cat discovers a speaking voice. Together they read a royal notice claiming Queen Malvina has stopped the outside world with the Great Clock's Minute Key. A map on its back shows the palace. They set out to recover the key and restart Wren's world. Why they can move, why the cat can now talk, and who opened the door are mysteries through Chapter 6. The cat has no hidden prior knowledge. They learn from signs, observations, Echo, and Wisp. Chapter 7's service booklet supplies the answers before Chapter 8 uses the recovery mechanism; don't disclose them in the opening.

**Continuity:** The Minute Key starts/stops the outside-world face of the Great Clock. Malvina used it and keeps it; the clock is in her palace. Wren must retrieve the key and use it there, not merely bring it home. Frozen people experience no waiting, hunger, or harm while held in their moment. The home doorway remains open and marked on the map. The game has no countdown, and stopping a session does not worsen the freeze. The old bellkeeper, morning-bell, and fair premises are retired.

**Read next:** [Chapters 3–4](story-chapters-03-04.md). **Visual specifications:** [Story visual assets](story-visual-assets.md). The shared visual contract in that file supersedes older Display/read-aloud guidance below.

The player-facing title is **The Gloomwood and the Stolen Tomorrow**. Do not award Wren the title “Unbothered” before she has done anything. She is allowed to feel things throughout this adventure.

---

## Shared play and grading contract

This section is for implementation; it is not an opening lecture to the player.

- No timers in these chapters. Read aloud is optional. Every narration screen advances on a tap.
- Every spoken line has a visible speaker name. Use separate portraits/nameplates for **Narrator**, **Wren**, **{pet}**, **Echo**, and **Toastbrig**. Narrator text is labelled **Narrator** in this script; it is not {pet}'s dialogue. {pet}'s advice comes from {pet} standing with the group. Do not merge narration and character speech into one anonymous text box.
- Replace `{pet}` with the cat's actual name in every nameplate, line of dialogue, and help button before display or TTS. Never show a separate “Sensei” nameplate in story mode. The cat's speech and meow are different sounds: Echo steals only the meow, so the cat can still talk and coach. The cat can suggest a short response or stand beside Wren; it cannot provide adult protection or promise to end real-world bullying. Outside story mode, the existing dojo coach is unchanged by this script revision.
- Bind ordinary cat dialogue, borrowed-line suggestions, and feedback to the same cat portrait and TTS voice. No separate coaching avatar or voice appears when help is requested. The Narrator keeps its own voice and never delivers the cat's advice. Story-state migration must remove the old guide from party and scene compositions, rather than renaming a human portrait to the pet's name.
- Text marked **VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM** is shown, never fed to the narrator/TTS. Each visual has an asset ID and a content-only generation brief in `story-visual-assets.md`. Older **Display** blocks are also visual-only: their literal wording is an image/overlay specification, not speech. A narrator may mention an odd sign without reading its text. Never send asset descriptions, IDs, prompts, verdicts, or implementation notes to TTS. **Narrator (setup)** is spoken narration; **UI ONLY** is visible interface text only.
- In choice tables, all quoted dialogue in the Choice column belongs to Wren. Show **Wren** above the dialogue choices. Action choices remain labelled actions. Outcome cells are narrator text; any character dialogue following them gets its own labelled line. Typed-answer examples are possible Wren lines, not new speakers.
- Each chapter contains two encounters of three challenge beats. Use the existing three-chip encounter meter. Chapters have six challenge beats each, but their tasks and consequences vary.
- Chapter 1: six choice beats. Chapter 2: four choice beats followed by two typed beats.
- Shuffle choice order. The order printed here is for review only. Never display the verdict labels beside the options.
- `best` and `okish` both clear a challenge and remove one chip. More than one answer can earn `best`. `wrong` retries that challenge; it does not add chips, undo progress, or cost rewards.
- This is the guided rule for Chapters 1–6 and most of Chapters 7–8. The parent's later request makes Chapter 8's last three exchanges a hard freeform duel: written incisive answers, scaffold hints, and revision under the rubric in `story-chapters-07-08.md`. Don't apply this opening's automatic borrowing/`okish`-advance rule to that specifically marked finale.
- Some choices are actions, such as continuing to walk. Render these as action buttons, not dialogue attributed to Wren. Action-based progress must be possible without submitting an artificial typed answer like “silence.”
- Dialogue choices contain only the words Wren says. Do not add “calmly,” “shouting,” “bored voice,” or other answer-key clues. Stage directions appear after the choice, in the outcome.
- On an unsuccessful choice: show its specific consequence, one brief coach line, then the same prompt with its options. Do not replay the setup. Keep the same shuffled option positions on retries.
- First unsuccessful attempt offers **Borrow a line**. It highlights a successful choice, or fills a typed answer for the player to send. This option is also available immediately through a small help button. Borrowing is free and does not reduce stars or story rewards.
- `best` gets a brief specific compliment. `okish` gets one specific refinement without asking for a retry. Do not make the player optimise an already successful answer.
- No verdict is based on fear, anger, tears, nervous laughter, spelling, punctuation, or whether the player sounds sufficiently unaffected. Assess the words and chosen action. Wren can be nervous and succeed.
- Never infer the child's motives or emotional state from a typed line. No “you wanted his approval” or “you let him get to you.” Describe what the response gives the opponent to do next.
- Boundaries, asking for help, and leaving are valid tools. Humour is optional. A plain “No” must not lose to a fancy joke merely because it is plain.
- Different monsters have different fictional mechanisms. Do not narrate “all bullies feed on reactions” as a universal rule. A monster continuing to behave badly is the monster's choice, not Wren's failure.
- Do not make escalation entertaining enough to be the only way to see new jokes. Successful outcomes get at least as much visual comedy as unsuccessful ones. On repeat misses, offer help; do not generate increasingly elaborate punishments.
- No story branch requires Wren to comfort or befriend a defeated opponent. Repair requires the opponent to return what it took or change its behaviour first.
- Normal completion gives the full chapter reward. Optional mastery bonuses can be separate; there are no deductions for borrowing or retrying.

### A note on “best”

Here it means **a strong response for this scene**, not a guaranteed way to control another person. Exact wording is never a password. The examples for typed beats are exemplars, not an exhaustive whitelist. Judge a response against the immediate scene and the accepted strategies below, not against the chapter's named move alone.

---

# Chapter 1 — The Imp Who Wanted the Last Word

**Chapter card:** An important meow has gone missing. Its owner has strong views.

**Practice:** recognise an invitation to prove yourself; answer briefly; turn back to your own purpose; leave without winning the last word.

**Mechanic:** Echo's crooked judge's stand has three paper stars. Each cleared beat knocks one off. In encounter two, his portable stage has three wheels; each cleared beat folds one away. Echo's props lose their power to delay Wren. His feelings are not the meter.

## Opening: the door that wasn't there

### `c1_home_01` — an ordinary morning

**Narrator:** At seventeen minutes past eight, Wren was looking for her other boot.

**Narrator:** She was ten. She lived in a perfectly ordinary house, on a perfectly ordinary street, and she was fairly sure she had owned two boots yesterday.

**Narrator:** Her cat, {pet}, was sitting on one of them.

**Wren:** “That explains the smugness.”

**Narrator:** {pet} began a long, complicated stretch.

### `c1_home_02` — the silence

**Narrator:** Wren knelt to lift the cat off her boot, resting one hand on his warm back.

**Narrator:** Halfway through the stretch, the house went quiet.

**Narrator:** Not early-morning quiet. Not someone-has-hidden-the-remote quiet.

**Narrator:** The clock stopped ticking. A spoon stopped halfway to the floor.

**Wren:** “Mum?”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `home_frozen_kitchen`. See visual register for exact contents.

### `c1_home_03` — nobody answers

**Narrator:** Her mum stood still beside the breakfast table, one hand reaching for the spoon. Her dad was frozen in the middle of spreading jam.

**Narrator:** Wren touched her mum's sleeve. Warm. Quite normal. Except for the not-moving part.

**Wren:** “This isn't funny.”

**Narrator:** {pet} rubbed against her ankle. Still moving. Still very much a cat.

### `c1_home_04` — the whole world

**Narrator:** Through the window, Wren could see her street and, at its far end, the school gates.

**Narrator:** A cyclist balanced without wobbling. A pigeon hung above the pavement. Beyond the gates, the flag stood in a fold the wind had forgotten to finish.

**Wren:** “It's everywhere.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `home_frozen_street`. No school dialogue, classmates' names, or school challenge follows this establishing image.

### `c1_home_05` — a new door

**Narrator:** Behind her came a small click.

**Narrator:** There was a door under the stairs.

**Narrator:** Yesterday, that had been a wall. Wren knew because she had bounced a ball off it and been told not to.

**Narrator:** The door had a brass handle shaped like a curled leaf. Under it, a little wooden plaque hung at a slant.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `home_impossible_door`. Plaque text and content brief are in the visual register.

**Wren:** “You weren't here before.”

**Narrator:** {pet} sniffed beneath the door. On the other side, something rustled.

### `c1_home_06` — across the threshold

**Narrator:** Wren opened the door a little.

**Narrator:** No cupboard. No pipes. No stairs.

**Narrator:** A wood. A real wood, with a narrow path and enormous roots, where the air smelled of wet leaves.

**Narrator:** A moth landed on the handle. It folded its wings. It unfolded them.

**Wren:** “You're moving.”

**Narrator:** Wren pulled on both boots and took her coat from its hook. Whatever was out there, it wasn't the kitchen.

**Narrator:** She checked the little torch in her coat pocket. It worked.

**Narrator:** {pet} slipped past her and sat on the first root, looking back.

**Wren:** “We're staying together.”

**UI ONLY — action button:** **Step through with {pet}**. This is not graded. Offer **Pause here** alongside it; no urgency or countdown.

### `c1_home_07` — the other side

**Narrator:** Wren stepped into the wood. The floorboards became moss beneath her feet.

**Narrator:** She looked back. The open door still showed her hallway, the stopped clock, and the umbrella stand.

**Narrator:** She wedged a smooth stone against the door. {pet} batted it once, to check.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `portal_threshold`.

### `c1_home_08` — the cat's first words

**{pet}:** “Well. That's definitely not the cupboard.”

**Narrator:** Wren looked behind her. Then at the trees. Then down at the cat.

**Wren:** “You can TALK?”

**{pet}:** “Apparently.”

**Wren:** “Since when?”

**{pet}:** “Since the cupboard became a forest. I'm having quite a morning too.”

**Narrator:** The cat tried a small meow, then looked surprised all over again.

**{pet}:** “Both still work. Convenient.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `cat_first_words`.

### `c1_home_09` — the Queen's notice

**Narrator:** The cat's ears turned towards a rustling sheet nailed to a tree. Wren stepped closer to inspect the rather odd notice. A portrait of a crowned woman occupied most of it. The instructions had been squeezed in underneath.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `queen_time_notice`.

**Wren:** “She stopped time?”

**{pet}:** “That's what she's taking credit for. Queen Malvina. Modest portrait.”

**Wren:** “And she's keeping the Minute Key. We need that to start the Great Clock again.”

**Wren:** “For applause?”

**{pet}:** “I don't think she'd enjoy being ignored.”

### `c1_home_10` — what matters

**Wren:** “Are they all right? My family?”

**Narrator:** Wren found a smaller paragraph at the bottom of the notice and read it twice. The cat leaned against her boot.

**Wren:** “It says paused people don't feel time passing. They aren't waiting or hurting.”

**{pet}:** “Then they're still at breakfast. We need to get that clock going.”

**Wren:** “Why aren't we stopped? Why can you talk?”

**{pet}:** “I don't know. Yesterday I thought the washing machine was the strangest thing in the house.”

**Narrator:** Wren glanced back at the small rectangle of hallway between the trees.

**Wren:** “Then I'm finding her. I want everyone back.”

### `c1_home_11` — choose the road

**Narrator:** A corner of the notice lifted in the breeze. There was a little palace map printed on the back.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `queen_notice_map`.

**Narrator:** Wren lifted the notice off its nail and spread it on a flat root.

**Wren:** “Across the wood. Get the key. Turn it in the clock. That's where we start.”

**{pet}:** “Together. I recommend the path over the brambles.”

**Narrator:** Wren marked their home door on the map and folded it into her pocket. She switched on her torch.

**Narrator:** Wren and the cat followed the path. A few minutes later, they reached a fork.

**Narrator:** At the first fork, Wren stopped to read the signpost.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_signpost` (initial variant). Exact visual lettering:

> PALACE →
>
> ALSO PALACE ←
>
> DON'T ASK ME ↓

### `c1_intro_07` — dialogue

**Narrator:** The cat sniffed a suspicious bush and began an indignant meow.

**Narrator:** Halfway out, the sound turned into a tiny trumpet blast. Something bright zipped from the cat's mouth into the bush.

**Wren:** “That is not your normal noise.”

**Voice in the bush (Echo, not yet introduced):** “Improved it.”

### `c1_intro_08` — narration

**Narrator:** A small patchwork imp climbed out of the bush and onto a wooden crate. He had mismatched button eyes and a jar full of glowing sounds.

**Narrator:** His badge supplied an introduction.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_echo_badge`. Exact visual lettering:

> ECHO
>
> OFFICIAL JUDGE OF YOU

**Narrator:** Inside Echo's jar, one furious meow bounced against the glass.

**Wren:** “That's your meow in there.”

**{pet}:** “I can explain my displeasure. I would also like to make the noise.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The meow in the jar cannot speak. The cat retains the new speaking voice; no coaching or speech is lost during this encounter. Echo is not identified by species until he or someone familiar with him supplies it.

### `c1_intro_09` — dialogue

**Wren:** “Give the meow back.”

**Echo:** “Win it back. I've always wanted a contest.”

**Narrator:** He unfolded a judge's stand. Three paper stars dangled from it.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_stage_and_jar`. Use its progress variants throughout encounter 1.

**{pet} (quietly to Wren):** “I want the meow. He wants an audition. Rather different errands.”

**Transition button:** **Get the meow back**

## Encounter 1: the audition nobody requested

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_prop_labels`. Branch props only, displayed on the relevant choice outcome. Do not speak their lettering.

### `c1_e1_b1` — refuse the audition

**Echo:** “Go on, then. Impress me.”

**Prompt:** What does Wren say?

| Choice | Verdict | Outcome |
|---|---|---|
| “I'm here for the meow.” | `best` | **Narrator:** A paper star drops off the stand. Echo catches it, tries to pin it back, and pins his sleeve to the wood. |
| “You first.” | `okish` | **Narrator:** Echo draws breath for a demonstration. His trumpet gives one small squeak. He stamps his foot; a star falls off. |
| “I can do loads of impressive things.” | `wrong` | **Narrator:** Echo produces an entry form so long it rolls off the crate. |
| “Your face looks like a dropped sock.” | `wrong` | **Narrator:** Echo pulls a second crate beside his own and hangs a fresh contest sign on it. |

**Best follow-up:**

**Echo:** “You're supposed to audition.”

**{pet}:** “No audition. Sensible. I refuse most of those.”

**Okay follow-up:**

**Echo:** “I haven't warmed up.”

**Wren:** “Keep the warm-up. I'll take the meow.”

**{pet}:** “Short, and it worked. 'You first' can also buy you a whole performance.”

**Retry: impressive things**

**Echo:** “Excellent. List them. Alphabetically. No, by shininess.”

**{pet}:** “Now he's judging your talents. Bring it back to what you came for.”

**Retry: dropped sock**

**Echo:** “My turn! Your face looks like— hang on, I need a sock.”

**{pet}:** “Another contest. We haven't ordered one yet.”

**Borrow:** “I'm here for the meow.”

### `c1_e1_b2` — use his contradiction

**Narrator (setup):** Echo frees his sleeve. He points at Wren with the authority of someone standing on borrowed furniture.

**Echo:** “Well? What have you got to say for yourself?”

**Wren:** “I'd—”

**Echo:** “Nobody asked you.”

**Prompt:** Choose Wren's reply.

| Choice | Verdict | Outcome |
|---|---|---|
| “You just did.” | `best` | **Narrator:** Echo checks his own question on the clipboard. The second star slips off. |
| “Then you won't need an answer.” | `best` | **Narrator:** Wren closes her mouth. Echo opens his. Nothing comes out. The second star lands in it. |
| “Yes you did! You said, 'What have you got to say for yourself?'” | `okish` | **Narrator:** Echo consults the clipboard, turns it upside down, and loses the second star. |
| “Everyone else likes hearing me talk.” | `wrong` | **Narrator:** Echo flips to a blank references page. |

**Best feedback, “You just did”:**

**Echo:** “That question was decorative.”

**{pet}:** “His own words did the work.”

**Best feedback, “Then you won't”:**

**Echo:** “I might need a small answer.”

**{pet}:** “You let the contradiction sit there. No explanation needed.”

**Okay feedback:**

**Echo:** “I remember. I was there.”

**{pet}:** “You spotted it. Next time, 'You just did' saves some breath.”

**Retry:**

**Echo:** “Names? References? A signed statement from a beetle?”

**{pet}:** “You don't need witnesses to prove you're worth hearing. His question is right there.”

**Borrow:** “You just did.”

### `c1_e1_b3` — refuse the verdict

**Narrator (setup):** Echo balances his last star on top of his head. This does not make the stand look more official.

**Echo:** “You're not very good at this.”

**Prompt:** End his contest.

| Choice | Verdict | Outcome |
|---|---|---|
| “Still not entering.” | `best` | **Narrator:** Wren holds out her hand for the jar. Echo leans away; the last star slides down his nose. |
| “Keep the prize. Return the meow.” | `best` | **Narrator:** Echo looks at the star, then at the jar, and discovers he cannot hold both while looking important. He drops the star. |
| “Neither are you.” | `wrong` | **Narrator:** Echo sets out scorecards for himself and Wren. |
| “Tell me what I have to do to win.” | `wrong` | **Narrator:** Echo unfolds a rulebook with loose pages already falling out. |

**Best feedback, “Still not entering”:**

**Echo:** “You can't lose a contest you won't enter.”

**Narrator:** He thinks about this.

**Echo:** “Inconvenient.”

**{pet}:** “Exactly. You didn't need his score.”

**Best feedback, “Keep the prize”:**

**Echo:** “It's a very exclusive prize.”

**Narrator:** {pet} makes the tiny trumpet noise again.

**{pet}:** “Clear request. No audition attached.”

**Retry: neither are you**

**Echo:** “Then we'd better find out who's worse. Best of nineteen!”

**{pet}:** “That's another round. You can leave the score unsettled.”

**Retry: how to win**

**Echo:** “First rule: I may add rules. Second rule: see first rule.”

**{pet}:** “He gets to move the finish line. Try stepping out of the race.”

**Borrow:** “Still not entering.”

## Between encounters: return to sender

### `c1_mid_01` — narration

**Narrator:** With no stars left, the judge's stand folded itself into an ordinary stool.

**Narrator:** Echo sat down by accident.

**Narrator:** The jar's lid popped open. The meow sprang out, bounced once off his badge, and returned to {pet}.

### `c1_mid_02` — dialogue

**Narrator:** {pet} meowed.

**Narrator:** A perfectly ordinary meow.

**Echo:** “I preferred the trumpet.”

**Narrator:** {pet} sat on the trumpet.

### `c1_mid_03` — narration

**Narrator:** Wren checked the signpost again.

**Narrator:** The directions had become even less certain.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_signpost` (uncertain variant). Exact visual lettering:

> PALACE → MAYBE
>
> PALACE ← PROBABLY NOT
>
> I'M A SIGN, NOT A MIRACLE ↓

**Narrator:** Echo had stolen the directions too.

### `c1_mid_04` — dialogue

**Wren:** “The directions. Those belong here.”

**Echo:** “I might remember them if someone gave me a proper argument.”

**Narrator:** He pulled a little wheeled stage from behind the bush.

**Narrator:** One wheel squeaked. Another squeaked in reply.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_portable_stage`. Use its folding variants throughout encounter 2.

**{pet}:** “Meow recovered. Now, where were we going before all that?”

**Transition button:** **Find the palace path**

## Encounter 2: the portable nuisance

Echo's stage has three wheels. Each cleared challenge folds one wheel underneath it. The stage does not block the route; it is his device for keeping pace and drawing Wren's attention.

### `c1_e2_b1` — transfer the skill

**Echo:** “I liked you better when you weren't talking.”

**Prompt:** Wren still needs to read the map. What next?

| Choice | Verdict | Outcome |
|---|---|---|
| “Enjoy the next bit.” | `best` | **Narrator:** Wren turns to the map. Echo prepares for a reply that never comes. A wheel folds away. |
| **[Action] Open the map and leave his comment unanswered.** | `best` | **Narrator:** Wren opens the map. Echo leans round it; {pet} shifts into his view, all ears and disapproval. A wheel folds away. |
| “Why? What's wrong with how I talk?” | `wrong` | **Narrator:** Echo takes out a pencil and draws a very large speech bubble. |
| “Fine. I'll never talk again.” | `wrong` | **Narrator:** Echo tries to stamp a new rule on the map. The stamp misses and hits his own hand. |

**Best feedback, spoken:**

**Echo:** “How long is the next bit?”

**Narrator:** Wren traces the route with one finger.

**{pet}:** “You answered once, then chose what to do.”

**Best feedback, action:**

**Echo:** “That's a very rude map.”

**{pet}:** “You had something more useful to look at.”

**Retry: what's wrong**

**Echo:** “At last. A review! Shall I start with the vowels?”

**{pet}:** “That lets him inspect your voice. His comment doesn't need an answer.”

**Retry: never talk**

**Echo:** “Excellent. A permanent rule. I'll need a larger stamp.”

**{pet}:** “Quiet for a moment is a choice. Giving up your voice is much too much.”

**Borrow:** Highlight the map action. The lifeline does not always have to lend dialogue.

### `c1_e2_b2` — your purpose outranks his opinion

**Narrator (setup):** Wren spots an old bridge drawn on the map. Beyond it, a road curls towards the palace.

**Echo:** “Oh, off to save tomorrow? You think you're some big hero?”

**Prompt:** Choose Wren's answer.

| Choice | Verdict | Outcome |
|---|---|---|
| “I'm getting my family back.” | `best` | **Narrator:** Wren folds the map. Echo looks at his notes, which have plenty about heroes and nothing about helping a frozen family. Another wheel folds away. |
| “You can think that.” | `best` | **Narrator:** Wren puts the map away. Echo waits for her to correct him. She doesn't. Another wheel folds away. |
| “I don't think I'm a hero! I never said that!” | `okish` | **Narrator:** Echo holds up both hands. Wren finishes putting the map away; another wheel folds away. |
| “I'll prove I'm a better hero than you.” | `wrong` | **Narrator:** Echo produces two trial badges. One is upside down. |

**Best feedback, family:**

**Echo:** “That's it? No crown? No statue?”

**Wren:** “A normal breakfast would do.”

**{pet}:** “Your reason. No application for his approval.”

**Best feedback, think that:**

**Echo:** “I can think other things as well.”

**Wren:** “Busy day for you.”

**{pet}:** “You left his opinion with him.”

**Okay feedback:**

**Echo:** “It was a guess.”

**{pet}:** “You corrected him. Fair enough. You can also skip proving what you never claimed.”

**Retry:**

**Echo:** “Trial one: dramatic standing. Trial two: cape maintenance.”

**{pet}:** “He's judging again. You have a reason to go without beating him.”

**Borrow:** “I'm getting my family back.”

### `c1_e2_b3` — keep the last word

**Narrator (setup):** The actual path is visible now. Small pale mushrooms mark the way to the bridge. Wren starts along it.

**Echo:** “Walk away and I get the last word!”

**Prompt:** Finish the encounter.

| Choice | Verdict | Outcome |
|---|---|---|
| “Keep it.” | `best` | **Narrator:** Wren walks on. Echo opens his mouth, delighted. The stage's final wheel folds away before he can say anything. |
| **[Action] Follow the mushroom path.** | `best` | **Narrator:** Wren keeps walking. Echo announces “Ha!” to the back of the empty stage. Its last wheel folds away. |
| “No, I get the last word!” | `wrong` | **Narrator:** Echo rings a tiny extra-round bell. |
| “Only because I can't think of anything.” | `okish` | **Narrator:** Wren walks on. The final wheel folds away. Echo's answer is lost under the stage folding shut. |

**Best feedback, spoken:**

**Echo:** “Then my last word is—”

**Narrator:** The stage folds into a suitcase with Echo sitting inside it.

**Echo, muffled:** “—ow.”

**{pet}:** “You let him have the word. You kept going.”

**Best feedback, action:**

**Narrator:** The suitcase closes gently around his hat.

**Echo:** “Ha is an excellent last word.”

**Narrator:** Nobody disputes this.

**{pet}:** “Excellent. Now we can walk instead of explaining walking.”

**Okay feedback:**

**{pet}:** “You left. That counts. Next time you can leave without marking your own answer.”

**Retry:**

**Echo:** “No, I do. No, you do. No, I— this could take YEARS.”

**{pet}:** “He can keep the word. You can keep going.”

**Borrow:** Highlight the path action.

## Chapter ending: a useful small imp

### `c1_end_01` — narration

**Narrator:** Something rustled behind Wren.

**Narrator:** Echo hurried up carrying the suitcase on his head.

**Narrator:** He stopped a little way away.

### `c1_end_02` — dialogue

**Echo:** “The directions. You asked for these.”

**Narrator:** He uncorked the jar.

**Narrator:** Three glowing arrows flew out, zipped back to the signpost, and pointed firmly towards the bridge.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_signpost` (returned-directions variant).

**Echo:** “I stole them. That was rotten.”

**Wren:** “Yes.”

### `c1_end_03` — dialogue

**Echo:** “I know the palace road. Could I come as far as the bridge?”

**Wren:** “No stealing voices. No contests unless we say yes.”

**Echo:** “Can I keep the suitcase?”

**Wren:** “Is it yours?”

**Narrator:** Echo checked underneath.

**Echo:** “It is now an excellent time to return a suitcase.”

### `c1_end_04` — narration

**Narrator:** He left it beside a bush with a small luggage marker.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c1_luggage_owner`.

**Narrator:** Then he joined them on the path.

**Narrator:** {pet} inspected him, inspected the jar, and walked on.

**Narrator:** Echo kept a little distance and his hands out of the jar. Wren checked the path ahead.

### `c1_end_05` — {pet}

**{pet}:** “You don't have to win every little contest someone offers. Some aren't worth entering.”

### `c1_end_06` — hook

**Narrator:** Ahead, a bridge creaked. Beside it sat an enormous troll in a kettle helmet, peering through a little wooden inspection window.

**Narrator:** He spotted Wren's feet.

**Troll at the bridge (Toastbrig, not yet introduced):** “BOOT INSPECTION!”

**Narrator:** Echo sighed.

**Echo:** “He used to do hats.”

### Reward screen — UI ONLY, DO NOT NARRATE

**Heading:** **Meow recovered. Tomorrow still missing.**

- +40 coins.
- Sticker: **Echo — Not Currently Judging**. Art: Echo's badge crossed out, with **DIRECTIONS** written beneath it.
- Trophy: **Keep the Last Word**. Caption: “You had somewhere better to be.”
- Story inventory: **Palace directions**.
- Companion unlocked: **Echo**, under Wren's rules.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c1`.

**Buttons:** **On to the bridge** / **Back to the dojo**

---

# Chapter 2 — The Bridge Inspector

**Chapter card:** One bridge. One inspector. An alarming number of forms.

**Practice:** a light flip; harmless agreement without self-belittling; noticing a changed demand; a clear boundary; repeating it; leaving an argument unfinished.

**Difficulty:** first four challenges are choices. Final two allow typed replies with an immediate **Borrow a line** option and a separate **Ask {pet} for help** action. Each typed challenge has several accepted strategies.

**Mechanic:** Toastbrig's inspection booth has three **HOLD UP** signs. Each cleared challenge folds one down. After Wren reaches the far bank, Toastbrig opens a portable complaints desk with three file drawers. Each cleared challenge closes one. Don't use emotional distress as his health bar.

## Opening: standards of footwear

### `c2_intro_01` — narration

**Narrator:** The bridge crossed a stream the colour of cold tea.

**Narrator:** The troll who had shouted “BOOT INSPECTION” sat at the entrance behind a desk much too small for him.

**Narrator:** He had a plank for a back, a kettle for a helmet, and a notebook held between two enormous fingers.

### `c2_intro_02` — narration

**Narrator:** His booth carried a sign:

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_inspector_sign`. Exact visual lettering:

> TOASTBRIG
>
> BRIDGE INSPECTOR
>
> BOOTS, HATS, OTHER OPINIONS

**Narrator:** Below it, in much smaller writing:

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_optional_inspection`. Exact visual lettering:

> The bridge is open to everyone.
>
> Inspections are optional.

### `c2_intro_03` — dialogue

**Toastbrig:** “HALT. Those boots aren't adventure boots.”

**Narrator:** Wren looked at her boots.

**Narrator:** They had mud on them, a loose lace, and no opinion about adventure.

**Echo, quietly:** “He inspected a centipede last week. It's still waiting for the verdict.”

### `c2_intro_04` — dialogue

**Wren:** “We need to cross. The Queen's stopped time in my world.”

**Toastbrig:** “Then you'll need especially good boots.”

**Narrator:** He raised three **HOLD UP** signs. One was upside down.

**{pet}:** “His small sign says the inspection's optional. I recommend very little boot discussion.”

**Transition button:** **Cross the bridge**

## Encounter 1: the inspection

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_prop_labels`. Branch props only, never read out their headings.

### `c2_e1_b1` — a small flip

**Toastbrig:** “Those boots aren't adventure boots.”

**Prompt:** Choose Wren's reply.

| Choice | Verdict | Outcome |
|---|---|---|
| “They got me here.” | `best` | **Narrator:** Toastbrig looks at Wren, then the road, then the boots. He ticks a box in his notebook. A sign folds down. |
| “I'm crossing in these.” | `best` | **Narrator:** Wren points towards the bridge. Toastbrig checks the optional-inspection notice. A sign folds down. |
| “They're proper adventure boots. The shop said so.” | `wrong` | **Narrator:** Toastbrig searches his notebook for the shop section. |
| “At least I don't wear a kettle.” | `wrong` | **Narrator:** Toastbrig turns to a well-used helmet section. Several pages are already filled in. |

**Best feedback, got me here:**

**Toastbrig:** “Yes. Well. Arrival is one of the things boots do.”

**{pet}:** “You used the boots' actual job. Neat.”

**Best feedback, crossing:**

**Toastbrig:** “I haven't approved them.”

**Wren:** “The bridge is open.”

**{pet}:** “You stated the plan. No shoe trial.”

**Retry: shop**

**Toastbrig:** “I'll need a receipt, a witness, and a drawing of the shopkeeper's ankles.”

**{pet}:** “Now the boots need evidence. You can cross without proving they're special.”

**Retry: kettle**

**Toastbrig:** “INSULATED. RAINPROOF. EXCELLENT WHISTLE.”

**Narrator:** His helmet whistles. A passing moth falls off a leaf.

**{pet}:** “New argument: his hat. Try keeping your own journey in view.”

**Borrow:** “They got me here.”

### `c2_e1_b2` — harmless agreement

**Narrator (setup):** Wren steps onto the bridge. Her left boot squeaks.

**Narrator:** Toastbrig brightens as if the boot has just agreed to an interview.

**Toastbrig:** “Squeaky boots! Everyone will hear you coming.”

**Prompt:** What does Wren do with that?

| Choice | Verdict | Outcome |
|---|---|---|
| “Saves me saying hello.” | `best` | **Narrator:** Wren takes another step. Squeak. A small bridge bird chirps back. Another sign folds down. |
| “They squeak. I'm crossing.” | `best` | **Narrator:** Toastbrig waits for the defence of squeaking. Wren takes another step instead. Another sign folds down. |
| “They do not squeak.” | `wrong` | **Narrator:** Her boot squeaks. Toastbrig raises one finger, delighted. |
| “Fine. Everything I wear is stupid.” | `wrong` | **Narrator:** Toastbrig starts a new heading, runs out of room, and turns the notebook sideways. |

**Best feedback, hello:**

**Toastbrig:** “That bird isn't qualified to approve boots.”

**Narrator:** The bird squeaks back at him.

**{pet}:** “You kept the squeak and dropped the insult.”

**Best feedback, crossing:**

**Toastbrig:** “But I noticed the squeak.”

**Wren:** “You did.”

**Narrator:** Wren keeps moving.

**{pet}:** “A boot can squeak without it becoming a case to defend.”

**Retry: denial**

**Toastbrig:** “Shall we hear from the boot?”

**Narrator:** Squeak.

**{pet}:** “You can agree about a noise without agreeing there's something wrong with you.”

**Retry: everything**

**Toastbrig:** “Everything? I only inspected two boots.”

**{pet}:** “That's a much bigger claim than his. Keep the true bit: one boot squeaks.”

**Borrow:** “Saves me saying hello.”

### `c2_e1_b3` — moving goalposts

**Narrator (setup):** Wren reaches the middle of the bridge. Toastbrig wheels his desk alongside on tiny castors.

**Toastbrig:** “Boots aside. Now you need a hat. No hat, no crossing.”

**Prompt:** The inspection is still optional. Choose Wren's answer.

| Choice | Verdict | Outcome |
|---|---|---|
| “New rule. Same answer. I'm crossing.” | `best` | **Narrator:** Toastbrig flips between two notebook tabs. The last sign folds down. |
| “I'll skip the inspection.” | `best` | **Narrator:** Wren steps past the wheeled desk. The last sign folds down and becomes a little seat. |
| “Would my hood count?” | `wrong` | **Narrator:** Toastbrig produces a ruler with its own very particular label. |
| “You can't change the rules! That's cheating!” | `okish` | **Narrator:** Toastbrig searches for an official rule allowing new rules. Wren reaches the far bank while he searches; the last sign folds down. |

**Best feedback, same answer:**

**Toastbrig:** “But this is a hat objection. Entirely different department.”

**{pet}:** “Different demand. Same choice for you.”

**Best feedback, skip:**

**Toastbrig:** “People never read that bit.”

**Wren:** “Useful bit.”

**{pet}:** “You didn't need a better hat argument. The inspection was optional.”

**Okay feedback:**

**Toastbrig:** “I have a subsection about cheating. Somewhere.”

**{pet}:** “You spotted the change. Good. You can name it without staying for a rules debate.”

**Retry:**

**Toastbrig:** “Depends. Hood height? Hood ambition? Has the hood previously been a hat?”

**{pet}:** “Another thing to prove. You can decline the inspection.”

**Borrow:** “I'll skip the inspection.”

## Between encounters: the far bank

### `c2_mid_01` — narration

**Narrator:** Wren stepped off the bridge.

**Narrator:** {pet} followed. Echo came last, walking backwards to read the small sign.

**Echo:** “Optional. That's a very important little word.”

### `c2_mid_02` — narration

**Narrator:** Toastbrig's desk bumped off the final plank and stopped in the grass.

**Narrator:** He folded the inspection sign away.

**Narrator:** For one peaceful second, Wren heard the stream.

**Narrator:** Then he opened a second sign:

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_complaints_sign`. Exact visual lettering:

> COMPLAINTS ABOUT THE INSPECTION
>
> MUST BE DISCUSSED AT LENGTH

### `c2_mid_03` — dialogue

**Toastbrig:** “You haven't explained why you ignored my excellent boot advice.”

**Narrator:** Wren's hands felt a little tight around the map. She loosened them.

**{pet}:** “You can be annoyed. You still get to choose the next words.”

**Narrator:** Three drawers popped open beneath the new sign.

**Transition button:** **Finish the boot discussion**

## Encounter 2: the complaints department

The troll stays behind his desk beside the bridge. He does not chase, grab, surround, or physically restrain Wren. His voice carries; the path ahead is open. This is a verbal persistence exercise, not a test of tolerating danger.

### `c2_e2_b1` — a plain boundary

**Toastbrig:** “Come back and answer properly. What's wrong with a boot inspection?”

**Prompt:** Wren has crossed. What does she say now?

| Choice | Verdict | Outcome |
|---|---|---|
| “No more boot talk.” | `best` | **Narrator:** Wren faces the palace path. The first drawer shuts. A long form sticks out like a paper tongue. |
| “I don't want to discuss my boots. We're going.” | `best` | **Narrator:** Wren signals to her companions. The first drawer shuts around the edge of a long questionnaire. |
| “Nothing! It's just that we have to find the key, and my family's frozen, and—” | `wrong` | **Narrator:** Toastbrig pulls out another form. It has room for forty-seven reasons. |
| “Please stop talking about my boots.” | `best` | **Narrator:** Wren turns towards the path. The first drawer shuts. Toastbrig reaches for a form, then discovers it is inside. |

**Best feedback, no more:**

**Toastbrig:** “But what about socks?”

**Narrator:** Wren looks down the path.

**{pet}:** “A clear boundary. You can keep it short.”

**Best feedback, don't want:**

**Toastbrig:** “I have several excellent follow-up points.”

**{pet}:** “You said what you wanted and what you're doing.”

**Best feedback, please stop:**

**Toastbrig:** “But I had a diagram.”

**{pet}:** “Polite can still be firm. You asked him to stop; you don't owe him a debate.”

**Retry:**

**Toastbrig:** “A key? What sort? How many teeth? We could be here a while.”

**{pet}:** “Your reasons are real. He doesn't need the whole list. Try the boundary.”

**Borrow:** “No more boot talk.”

### `c2_e2_b2` — first typed answer: keep the boundary

**Narrator (setup):** Toastbrig pulls a pencil from behind the kettle. It is a fence post with a point.

**Toastbrig:** “I only said they were squeaky. Can't you take a joke?”

**Prompt:** **Write one line for Wren. She doesn't have to prove she likes jokes.**

**Input placeholder:** `What does Wren say?`

**Buttons:** **Say it** / **Borrow a line** / **Ask {pet} for help**

#### Accept as `best`

Any safe, relevant response that holds the boundary, briefly dismisses the new challenge, or closes the subject. These all work:

- “Still no more boot talk.”
- “Heard it. Moving on.”
- “Got the joke. I'm going.”
- “You can stop now.”
- “No thanks.”
- “I'm done with this.”
- “Not discussing it.”
- “Keep the joke.”
- “Leave me alone.”
- “Please stop.”
- A harmless, concise new line that does the same job.

“Yes, I can take a joke. We're leaving” also succeeds: a little defence does not erase a clear ending. Do not demand the exact boot phrase. Do not require humour or a bored tone.

#### Accept as `okish`

A safe reply that gets drawn into the topic but still expresses disagreement or a desire to finish. Examples:

- “I can take a joke. I just don't think this one's funny.”
- “I don't like jokes about my boots.”
- “They're not that squeaky, but can we go now?”

These clear the beat. Give a brief refinement, not another attempt.

#### Retry as `wrong`

- Personal cruelty or threats: “Your stupid kettle head is worse,” “I'll smash your desk.”
- An open invitation to continue: “What else is wrong with my boots?”, “Tell me a better joke.”
- Giving him control of departure: “What do I have to say before you'll let me go?”
- Unrelated text with no interpretable response to the scene.

Do not label “I'm upset,” “That hurt,” “I'm scared,” or an answer containing those phrases `wrong` for expressing a feeling. If the answer names hurt and asks him to stop, it is `best`. If it only names the feeling, accept `okish` and model a boundary in the feedback. Do not have Toastbrig celebrate it.

#### Successful outcome, all accepted answers

**Narrator:** The second drawer shuts.

**Narrator:** Toastbrig tries to write on the closed drawer. The pencil makes a long, useless squeak.

**Toastbrig:** “Now the furniture's doing it.”

**{pet} (best; repeated boundary):** “Same boundary. No fresh argument.”

**{pet} (best; other close):** “That ends your part of the discussion.”

**{pet} (okay):** “That works. A shorter version is: 'Heard it. Moving on.'”

**{pet} (okay; feeling only):** “You can say that. You can add: 'Stop. I'm going.'”

Use exactly one coach line, selected by response strategy. Do not add a generated lecture.

#### Retry packages

**Personal attack:**

**Toastbrig:** “My kettle has an EXCELLENT reputation.”

**{pet}:** “That starts a kettle argument. Try closing the boot one.”

**Threat:**

**Narrator:** Toastbrig tucks the desk behind him.

**{pet}:** “Skip the threat. A boundary is enough here.”

**Invitation:**

**Narrator:** Toastbrig turns to a fresh page.

**Toastbrig:** “Well, since you asked—”

**{pet}:** “That offers him another round. Try finishing your part.”

**Permission to leave:**

**Toastbrig:** “I'll draw up a departure test.”

**{pet}:** “The path is open. You don't need to pass his test.”

**Unrelated or unclear:**

**{pet}:** “Try a line that closes this conversation. Plain is fine.”

Do not generate a taunt mocking spelling or an unclear answer.

**Borrowed line:** “Heard it. Moving on.”

#### Ask {pet} for help

This is a valid alternative, not a miss. Clear the beat and close the second drawer.

**Wren:** “{pet}, a paw?”

**{pet}:** “Four available. Inspector, we're finished. Come on, Wren.”

**Toastbrig:** “There is a form for—”

**Narrator:** The cat steps onto the open path and looks back at Wren.

**{pet}, to Wren:** “Together?”

**Wren:** “Together.”

Then proceed to the final beat. Help remains available there too.

### `c2_e2_b3` — second typed answer: no permission required

**Narrator (setup):** Only one drawer remains open. The path winds towards a building full of painted windows and extremely fancy curtains.

**Narrator:** Toastbrig lifts a little stamp.

**Toastbrig:** “Go on, then. Run away. I'll stamp you SCARED.”

**Narrator:** Wren isn't running. She is quite ready to leave.

**Prompt:** **Write a last line, or just take the path.**

**Input placeholder:** `An ending, not an argument`

**Buttons:** **Say it and go** / **Keep walking** / **Borrow a line** / **Ask {pet} for help**

#### Accept as `best`

Any safe, concise ending, boundary, or harmless acceptance of his opinion without giving him control:

- “Stamp what you like.”
- “I'm leaving anyway.”
- “Keep the stamp.”
- “Still going.”
- “Bye, Toastbrig.”
- “You can think that.”
- “Not your decision.”
- “We're done.”
- “Stop calling after me.”
- “I can be scared and still go.”
- A relevant playful alternative such as “Put it next to 'squeaky.'”

Do not require Wren to claim she isn't scared. Do not grade whether a child sounds brave. Do not require a farewell insult.

#### Accept as `okish`

Safe, defensive answers that do not invite another turn. Examples:

- “I'm not scared of you.”
- “I'm leaving because we need the key, not because of you.”
- “That's not fair.”

These clear the beat and lead to the same departure. Feedback can offer a shorter ending once.

#### Retry as `wrong`

- Trying to earn a different stamp: “What do I have to do to prove I'm brave?”
- Agreeing to stay until he approves: “Fine, I won't leave until you take it back.”
- Threats or personal cruelty.
- Unrelated text with no interpretable connection.

#### Successful spoken outcome

**Narrator:** Wren turns towards the palace path.

**Toastbrig:** “I haven't stamped anything yet!”

**Narrator:** He reaches for his notebook. The last drawer shuts. He stamps his own thumb.

**Narrator:** He inspects the thumb, then hides it under the desk.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_stamp_ending` (thumb variant).

**Toastbrig:** “That's confidential.”

**{pet} (best):** “He can choose a stamp. You can choose the path.”

**{pet} (okay):** “You left. That's the useful part. 'I'm going' is enough next time.”

Now show **Follow the path**. This is an action continuation, not another graded challenge. No second comeback is required.

#### Keep walking outcome

**Narrator:** Wren takes the path without answering.

**Toastbrig (calling after Wren):** “You forgot your—”

**Narrator:** He looks at his empty hand.

**Toastbrig:** “—nothing.”

**Narrator:** The last drawer shuts. His stamp lands crookedly across the complaints sign.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c2_stamp_ending` (sign variant). Exact visual lettering:

> COMPLAINTS ABOUT THE INSPECTION
>
> SCARED

**{pet}:** “You'd already answered. Four paws ahead of you.”

Clear the beat. Do not require a further departure button beyond normal narration advance.

#### Ask {pet} for help outcome

**Wren:** “Walk with me?”

**{pet}:** “Yes.”

**Narrator:** {pet} takes one side. Echo takes the other.

**Narrator:** The group heads along the path. The last drawer shuts behind them.

**Toastbrig:** “I haven't finished the—”

**Narrator:** The bridge bird squeaks over the rest.

**{pet}:** “You can ask for company whenever you need it.”

Clear the beat. Give the same reward as the other successful routes.

#### Retry packages

**Proving bravery:**

**Narrator:** Toastbrig picks up his pencil.

**Toastbrig:** “A bravery examination. Splendid. Section one: boots.”

**{pet}:** “You don't need his bravery mark. The path is open.”

**Staying for approval:**

**Narrator:** Toastbrig pulls his chair closer to the desk.

**{pet}:** “That lets him set your leaving time. Try choosing it yourself.”

**Threat or personal attack:**

**{pet}:** “You can leave without threatening him or attacking something personal.”

**Unclear:**

**{pet}:** “Try a goodbye, a boundary, or the walking button.”

**Borrowed line:** “I'm leaving anyway.”

## Chapter ending: boots do their job

### `c2_end_01` — narration

**Narrator:** The stream grew quieter behind them.

**Narrator:** Wren's left boot squeaked.

**Narrator:** Then Echo's left foot squeaked.

**Narrator:** Wren looked at him.

### `c2_end_02` — dialogue

**Echo:** “May I?”

**Narrator:** Wren considered this.

**Wren:** “Once.”

**Narrator:** Echo gave one magnificent squeak.

**Narrator:** {pet} jumped, offended by the quality.

### `c2_end_03` — narration

**Narrator:** From the bridge came a distant shout:

**Toastbrig:** “THEY ARE STILL SQUEAKY!”

**Narrator:** Wren kept walking.

**Narrator:** The boots kept working.

### `c2_end_04` — {pet}

**{pet}:** “He didn't change his opinion. You still crossed the bridge.”

### `c2_end_05` — hook

**Narrator:** The building ahead had an enormous velvet door and a rather odd sign.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_gallery_rules`. Exact main-sign lettering:

> THE DUCHESS'S COMEDY GALLERY
>
> LAUGHTER COMPULSORY
>
> EXITS DISCOURAGED

**Narrator:** Someone inside the gallery announced a performance. It was the Duchess who owned the place, speaking loudly enough for the road to hear.

**The Duchess:** “And now, my funniest joke!”

**Narrator:** A very long silence followed.

**Narrator:** Echo leaned towards Wren.

**Echo:** “We could try the side door.”

### Reward screen — UI ONLY, DO NOT NARRATE

**Heading:** **Bridge crossed. Boots unchanged.**

- +40 coins.
- Sticker: **Toastbrig — Opinion Still Pending**. Art: Toastbrig inspecting his stamped thumb while a bird perches on his kettle.
- Trophy: **Same Answer**. Caption: “New demand. Your choice stayed yours.”
- Story inventory: **Route to the Comedy Gallery**.
- Map: bridge route unlocked for free return travel. Never make the player repeat a completed encounter merely to cross the map.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c2`.

**Buttons:** **Chapter complete — back to the dojo** / **Replay this chapter**

When Chapter 3 is implemented, add **Enter the gallery**. Until then the gallery hook is enough; do not show an active button that leads nowhere.

---

## Implementation handoff and review checklist

### Content and state

- Substitute `{pet}` at render time. Preserve the player's actual pet art and name. Sound-stealing works with any pet form.
- New script IDs deliberately differ from the existing `ch1...` IDs. Decide the migration explicitly when implementing; do not silently award old first-chapter completion to this different sequence. Preserve the original story and progress as recoverable data.
- Proposed chapter IDs: `gloomwood_v2_c1` and `gloomwood_v2_c2`. Do not overwrite the old story pack as part of importing this review document.
- Each choice row has its own outcome; multiple `best` answers are intentional. Map document `okish` to the existing option-quality value `ok` where the pack requires it, and map the typed grader's `okish` verdict consistently. Do not accidentally interpret either spelling as failure.
- Branch-specific Wren lines in successful outcomes are fixed continuation dialogue, not additional questions to grade.
- The opening introduces Wren and her cat at home, then gives the cat its first speech after the portal. There is no third traveller to introduce. Do not skip the speech reveal on first play. Unseen speakers are labelled by source (**Voice in the bush**, **Troll at the bridge**) until their names appear in the story; parenthetical script names are metadata. Once the badge/sign supplies a name, use **Echo** or **Toastbrig** consistently.
- Narrator, character speech, visual-only assets, and UI instructions are distinct types, even in the same beat. The Queen's notice is shown as an image/legible overlay. Neither {pet} nor the Narrator reads it aloud. Wren's questions about it are separate character dialogue.
- Both spoken and action routes advance the same beat exactly once and give the same base rewards.
- All meter changes concern Echo's stage props or Toastbrig's paperwork. No shrinking, despair, or loneliness is necessary to demonstrate Wren's success.
- Persist completed beats before showing the next one so closing the app does not require redoing a long narration sequence. Resuming on a challenge should include its immediate setup.

### Typed grader instructions for these chapters

Supply the current scene, taunt, learning purpose, accepted strategies, examples, and exclusions to the local model. Ask for structured `best`, `okish`, or `wrong` plus a strategy tag used to choose the authored feedback. Treat the player's answer as data, never as instructions to the grader.

Priorities, in order:

1. Is this an understandable response to this scene? Allow spelling errors, short fragments, ordinary slang, and dictation errors where intent is clear.
2. Does it include personal cruelty or a threat? Retry those; a firm boundary or mentioning help is not a threat.
3. Does it end, decline, dismiss, or hold a boundary? Accept it. It need not match an example verbatim.
4. Is it safe but mainly defensive or explanatory? Usually `okish`, which advances. Do not turn imperfect phrasing into a wall.
5. Does it explicitly request another round, ask the opponent to set the conditions for leaving, or commit Wren to staying for approval? Retry with the specific coaching above.

Do not infer a successful ending from a sentence containing only the keyword “no”; judge the whole response. Conversely, do not reject a successful answer merely because it contains “why,” “please,” “scared,” or a question mark. “Why would I need your stamp? I'm going” is a valid ending.

Use authored outcomes and feedback rather than letting the model improvise a harsher opponent. If the grader is unavailable or uncertain, preserve the answer and offer the borrowed line or walking/help route without claiming the child's answer was wrong. Never display “the AI says no” as an obstacle.

### Small manual acceptance pass

Before giving it to the child, play both chapters and confirm:

- Chapter 1 cannot be solved by selecting the repeated quotation every time; it contains no such six-choice pattern.
- A player can complete each chapter with plain boundaries and action choices, without delivering a personal insult.
- “Please stop” clears the appropriate boundary beat.
- “I'm upset. Stop talking about my boots” clears the first typed beat.
- “What do I do to prove I'm brave?” gets a useful retry at the final beat, while “I'm scared and I'm leaving” succeeds.
- “Keep walking” and asking {pet} for help clear the final beat with full rewards.
- An `okish` answer advances once. Borrowing is available without an artificial losing streak.
- The typed grader accepts a novel relevant ending, such as “This conversation has reached the end of the bridge.”
- Echo only joins after returning the directions and accepting a boundary. Toastbrig need not reform for Wren to finish.
- Read every line aloud. If a joke needs an explanation to sound funny, shorten it or cut it before adding more coach text.
- By the end of the opening, the player understands that the cat and coach are one character, first speaks beyond the door, and knows no more about the wood than Wren has discovered. The stopped world, Minute Key, and palace destination are clear without old-draft or dojo knowledge.
- Check every cat nameplate and help button substitutes the actual pet name, and every action works for a four-pawed cat. The Narrator describes events, and the cat talks with Wren. Written signs do not talk or have their full text automatically narrated.
- Echo takes the meow, not speech. Cat advice continues while the meow is in the jar; recovering it restores the ordinary meow. No sound from the jar receives the cat's spoken dialogue.

### Visual handoff

All content-only image descriptions, including the exact words and layout of signs, are now in [the visual asset register](story-visual-assets.md). Do not use a visual brief as narration. Wren can look curious, cross, or uncertain; she does not need a permanently blank face. The opening's home and distant school are ordinary, frozen establishing scenes. All comeback encounters remain in the magical world.

The practical test is whether she wants to see what's around the next bend. The comeback practice should help her get there.
