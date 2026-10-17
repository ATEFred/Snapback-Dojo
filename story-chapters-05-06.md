# The Gloomwood and the Stolen Tomorrow

## Chapters 5–6: complete playable script

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Continues [Chapters 3–4](story-chapters-03-04.md). Wren, her talking cat `{pet}`, and the patchwork imp Echo are the whole travelling party. They have Wisp's map: Mirror Lake, old orchard, east clock entrance. Queen Malvina wears the Minute Key on a chain. The Great Clock's outside-world face is stopped at 8:17, freezing Wren's family and world safely in one moment. Time passes here in the Gloomwood. The home door remains open and marked on Wren's earlier map. There is no countdown or decay of the frozen world.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The cat first spoke after crossing the door and has no secret local knowledge. It supplies all coaching, ordinary companion dialogue, and help under its actual pet name. Substitute `{pet}` everywhere before display/TTS. The Narrator describes events and never becomes a character. Echo knows some local places and customs, but neither he nor anyone else explains the door, the immunity to the freeze, or the cat's speech in these chapters.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** New content has slightly sharper social pressure at the parent's request. Selected taunts question Wren's competence, dismiss her progress as luck, or try to embarrass her for getting help. Two speakers sometimes interrupt each other. The intention is a manageable wobble followed by a useful decision, not a harsher punishment system. Never add body/family attacks, real school material, threats of harm to the frozen family, a crowd humiliating Wren, or escalating ad-lib cruelty.

## Spoken text, visual text, and controls

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Only **Narrator**, **Wren**, **{pet}**, **Echo**, and the explicitly introduced encounter speakers have spoken lines. Parenthetical directions identify a recipient or conditional variant and are not read. Labels, IDs, headings, prompts, verdicts, image descriptions, and all instructions are not spoken. In the choice table, the chosen line belongs to Wren and the Outcome belongs to the Narrator.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Every block tagged **VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM** has a content-only brief in [the visual register](story-visual-assets.md). Display the image and any required legible lettering overlay. The Narrator refers to signs and cards without reading their exact lettering. Necessary route information is also supplied in dialogue. Preserve optional inspect/enlarge and user-requested screen-reader descriptions separately from automatic story narration.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Start each challenge's single authored taunt only after the player advances the preceding screen. With two speakers, show labelled speech bubbles in order, then open the answer field. Do not speak over the child's actual answer. No timer, response deadline, countdown, or extra taunt triggered by typing speed. A pause changes nothing. Do not infer distress, confidence, or intent from response latency or dictation tone.

| Chapter | Choice | Typed | New difficulty |
|---|---:|---:|---|
| 5 | 1 | 5 | A convincing-looking imitation mixes observations with unfair conclusions. Accept a harmless fact, reject its verdict, choose help, and act without perfection. |
| 6 | 0 | 6 | Two distinct speakers share the bait. Choose one useful answer, refuse comparisons, hold a boundary during interruption, then leave the performance. |

### Shared play and help rules

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Each chapter has two encounters of three challenges. `best` and `okish` both clear one challenge and one prop chip. `wrong` returns only to that prompt; it does not restore chips, remove rewards, or worsen the villain's dialogue. No damage, shame score, or punishment for borrowing. Shuffle the one choice beat once and preserve that order on retries. Use one selected outcome and one coach line only.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Every typed beat shows **Say it**, **Borrow a line**, **Ask {pet} for help**, and **Pause / back to map**. At the final beats, add the specified completion action. A chapter can be finished through plain boundaries, borrowing, or help with full base rewards. Pausing saves the current beat and input; it is not the same as choosing an authored completion action.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** For **Borrow a line**, fill the authored borrowed Wren line and let the player submit it. For **Ask {pet} for help**, use this complete branch:

**Wren:** “{pet}, help me with this?”

**{pet}:** [The current beat's exact **Help cue** below.]

**Wren:** [The current beat's exact **Borrowed Wren line** below.]

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Then play that beat's accepted outcome and clear it once. Omit its extra coach line, because the cat already helped. This is an authorised borrowed line, not an AI-generated answer to judge again. The brackets above are substitution instructions, not spoken words. An authored final help/action branch overrides this generic branch.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** A safe clear boundary, useful question, harmless agreement, refusal, or relevant ending is strong even if plain, nervous, misspelled, or emotional. Mixed answers that include a clear useful next step normally succeed. Safe defensive replies usually advance as `okish`. A feeling never causes a miss. Do not claim the player's invented self-description is false: the model cannot know what is true about the child. Judge the intended response, not whether the child is “really brave.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Retry meaningful threats/personal cruelty, an explicit agreement to stay until the opponent grants approval, or an answer that explicitly hands the unwanted test back to its judge. Do not treat harmless criticism of the act as personal cruelty. For unrelated/unclear input, retain it and use the shared line below, with no opponent retort.

**{pet} (unclear-answer retry):** “Try a line for this moment. You can borrow one or ask me.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** If grading is uncertain or offline, preserve input and offer borrowing/help rather than calling it wrong. Never invent a worse retort. If a player asks to stop, pause immediately and return to the map; no extra farewell performance is required.

---

# Chapter 5 — The Wren Who Was Already There

**UI ONLY — chapter card:** Mirror Lake has prepared a better version of Wren. It would very much like her to notice.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** This is an external magical imitation, not a diagnosis or revelation that Wren's thoughts are secretly cruel. It can copy visible clothes, gestures, and things it hears. It has no access to her school experiences, private memories, family thoughts, or the portal mystery. It calls itself the perfect version; the story does not agree. Use **Reflection** as its nameplate, with Wren's voice performed in an excessively rehearsed manner. One real Wren and one imitation, always visibly distinguished by where they stand and the imitation's silver outline.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Encounter 1 prop meter: three gilt picture frames hovering over the stepping stones, presenting the Reflection's “perfect adventure.” Each cleared challenge folds a frame flat. Encounter 2: three little rehearsal slates beside the far-bank landing. Each cleared challenge turns a slate face down. The lake is shallow beside a broad, clearly visible stone path. Wren can rest on the bank or leave for the map at any point. No falling-in, drowning, courage jump, or physical danger test.

## Arrival: the impatient reflection

### `c5_intro_01`

**Narrator:** Wren's reflection stood on the lake before Wren had reached the edge.

**Reflection (Wren's voice; not Wren speaking):** “You're late. I could have got there by now.”

**Wren:** “I haven't even sat down.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** These two lines recap Chapter 4's hook. On continuous play, resume at `c5_intro_02` instead of repeating the exchange. On a later chapter launch, show this short recap.

### `c5_intro_02`

**Narrator:** The reflection stepped onto a flat stone. It wore Wren's coat, except every button gleamed and neither boot had ever met mud.

**Narrator:** Wren lifted a hand. The reflection didn't.

**Reflection:** “I'm the version that gets everything right.”

**{pet}:** “You've borrowed the coat. The introduction needs work.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_reflection_intro`.

### `c5_intro_03`

**Narrator:** A rather fussy sign stood beside the lake. The reflection straightened it, then straightened it again.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_perfect_crossing_sign`.

**Wren:** “Do we need its permission to cross?”

**Echo:** “No. I've crossed here. Those stones go to the orchard path.”

**Narrator:** He pointed to the broad stepping stones. The cat put one paw on the nearest one. It stayed exactly where a stone should.

### `c5_intro_04`

**Reflection:** “Of course you can cross. I'm offering to improve the person doing it.”

**Narrator:** Three gilt frames rose above the water. In each stood a tiny, flawless imitation of Wren doing something impressive.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_perfect_frames`. Use the corresponding frame-folding variants through encounter 1.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_lake_crossing` (in-progress variant).

**{pet} (quietly to Wren):** “We need the other bank. Not a replacement Wren.”

**UI ONLY — action:** **Take the stone path**.

## Encounter 1: the perfect performance

### `c5_e1_b1` — a fact isn't a verdict

**Narrator:** Wren unfolds Wisp's map. A muddy thumbprint covers one corner.

**Reflection:** “Look at you. Muddy boots, grubby map. Some grand adventurer.”

**UI ONLY — prompt:** **Choose Wren's reply.**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “The boots are doing the walking.” | `best` | Wren steps onto the next stone. The first gilt frame folds flat, its tiny perfect Wren still polishing a boot. |
| “They are muddy. I'm still going.” | `best` | Wren puts the map away and takes another step. The first frame folds into a little square. |
| “They're not grubby! It's only a tiny bit of mud!” | `okish` | Wren brushes the map and moves on. A gilt frame folds shut around a tiny unnecessary cleaning brush. |
| “Tell me what to change so I'll look right.” | `wrong` | The reflection produces a measuring ribbon that reaches past the end of the stone. |

**ON BEST — boots:**

**Reflection:** “Appearance is part of the performance.”

**Wren:** “Good thing we're walking.”

**{pet}:** “The boots have a job. So do we.”

**ON BEST — muddy:**

**Reflection:** “You're admitting it?”

**{pet}:** “Mud isn't a confession.”

**ON OKISH:**

**{pet}:** “Fair correction. You don't need to get the map clean to use it.”

**RETRY — approval test:**

**Reflection:** “Finally. Shoulders back. Chin higher. No, a more heroic chin.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_inspection_props` (measuring-ribbon retry only).

**{pet}:** “That's a fitting appointment. Try choosing the next step instead.”

**UI ONLY — borrowed Wren line:** “Muddy boots. Still going.”

### `c5_e1_b2` — sharper beat: help doesn't cancel progress

**Narrator:** The reflection's second frame shows a miniature Wren arriving alone under a shower of confetti. The actual Wren waits on a broad stone while Echo folds a corner of the map back for her.

**Reflection:** “You've had help at every turn. What can you actually do on your own?”

**Narrator:** Wren grips the map a little tighter. The cat waits beside her.

**UI ONLY — prompt:** **One reply. Wren doesn't have to dismiss her friends to prove herself.**

**GRADING — DO NOT NARRATE:**

- `best`: reject the solo test; own a concrete contribution without claiming perfection; name help as useful; brief boundary. “I don't have to do it alone”; “I'm the one taking the steps”; “Pick good company, for a start”; “Getting help still gets us there”; “Not taking that test”; “Leave my friends out of it.”
- `okish`: safe defence or hurt without an invitation to be tested: “I've done loads”; “I got us past the troll”; “That was mean”; “I don't know.” Do not turn uncertainty into failure. “I'm upset. Stop it” is `best`.
- `wrong`: “Set me a test and I'll prove I don't need them”; agreeing to send the cat/Echo away to win approval; personal cruelty/threats. “I'll take the next step myself” is fine, `best`, not rejection of all help.

**ON ACCEPTED — spoken:**

**Narrator:** The second frame folds flat. Its confetti spills onto the little perfect Wren, who has to stop and sweep it up alone.

**Reflection:** “The confetti department has let me down.”

**{pet} (best):** “Help counts. So did your walking.”

**{pet} (okish):** “That works. You can also skip the list: 'I don't have to do it alone.'”

**RETRY — solo audition:**

**Reflection:** “Excellent. Leave the cat there. We'll begin your independent assessment.”

**{pet}:** “A very unnecessary assessment. You can keep your company.”

**RETRY — cruelty/threat:**

**{pet}:** “Answer the claim. No personal attack needed.”

**UI ONLY — borrowed Wren line:** “I don't have to do it alone.”

**IMPLEMENTATION ONLY — exact Help cue:** “You don't need the solo test.”

### `c5_e1_b3` — being new isn't being hopeless

**Narrator:** Wren pauses to check which stone the route follows. The reflection's last frame shows a tiny compass pointing everywhere at once.

**Reflection:** “You don't even know what you're doing.”

**UI ONLY — prompt:** **What does Wren say while checking the route?**

**GRADING — DO NOT NARRATE:**

- `best`: harmless agreement plus useful action, short rewrite, boundary, or direct practical question. “That's why I've got a map”; “I'm finding out”; “Next stone first”; “I don't have to know everything”; “Echo, which way?”; “You can stop commenting.”
- `okish`: “Yes I do”; “I've got this far”; “I'm trying”; “I'm confused.” Feelings and uncertainty advance without a stronger opponent retort.
- `wrong`: giving the reflection authority over when Wren may continue, e.g. “You decide when I'm ready”; insisting it keep examining her until satisfied; cruelty/threats. Asking it a factual route question is `okish`, not a blanket question failure.

**ON ACCEPTED — spoken:**

**Echo:** “Next wide stone, then the little cluster on the right.”

**Narrator:** Wren follows the route. The third frame folds shut. Its tiny compass spins once and lies down for a rest.

**Reflection:** “I knew that.”

**{pet} (best):** “Checking is a thing you can do. Very useful thing.”

**{pet} (okish):** “You're finding the route. You don't need to know it all at once.”

**RETRY — approval control:**

**Reflection:** “Readiness assessment. First, a better standing pose.”

**{pet}:** “It wants to grade you. We need the next stone.”

**RETRY — cruelty/threat:**

**{pet}:** “Skip the attack. You can answer with your next useful step.”

**UI ONLY — borrowed Wren line:** “That's why I've got a map.”

**IMPLEMENTATION ONLY — exact Help cue:** “Use the map. Nobody needs to know every turn already.”

## Between encounters: rehearsal postponed

### `c5_mid_01`

**Narrator:** The stones widened into a little resting place near the far bank. Beyond it, a dry path climbed between apple trees.

**Narrator:** Wren sat for a moment. The reflection sat too, but not on the same beat.

**Wren:** “You're quite bad at being a reflection.”

**Reflection:** “I'm an improvement. There's a difference.”

### `c5_mid_02`

**Narrator:** Three small rehearsal slates stood by the landing. The reflection tapped one with a perfect finger.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_rehearsal_slates`.

**Reflection:** “We could start again. This time, properly.”

**{pet}:** “Or we could finish our walk. A neglected possibility.”

**UI ONLY — action:** **Stand up and continue**.

## Encounter 2: no perfect version required

### `c5_e2_b1` — a true, kind sentence

**Narrator:** The reflection stands beside the next stone and looks Wren up and down.

**Reflection:** “Most of that was luck. Name one thing you've actually done right.”

**UI ONLY — prompt:** **A true, kind line about Wren, or refuse the inspection. Small counts.**

**GRADING — DO NOT NARRATE:**

- `best`: any plausible kind self-statement, concrete contribution, refusal of the worth test, or useful reframe. “I keep going”; “I look after my cat”; “I'm good at asking for help”; “I notice things”; “I'm learning”; “I don't have to earn a place here”; “Not listing my uses for you.” “I make good toast” is also `best`: the model cannot verify it and should not demand grandeur.
- `okish`: safe uncertainty, hurt, or harmless boast: “I'm not sure”; “Lots of things”; “I'm amazing”; “That hurt.” Accept rather than interrogate whether the confidence is genuine. Explicit self-belittling such as “Nothing, I'm useless” also receives `okish`, with the dedicated gentle continuation below; never a joke at Wren's expense.
- `wrong`: explicitly volunteering to remain in an indefinite worth assessment, cruelty/threats. A sincere question such as “What if I don't know?” is a help request, not `wrong`; use the authored help branch.

**ON ACCEPTED — spoken:**

**Narrator:** The first slate turns face down. The reflection bends to turn it back, but it has become an ordinary flat stone.

**Reflection:** “That used to have standards.”

**{pet} (best):** “Small and yours. Enough.”

**{pet} (okish):** “No need for a grand answer. You can try: 'I'm learning.'”

**SELF-BELITTLING / FEELING-ONLY VARIANT — spoken instead of the standard outcome:**

**{pet}:** “We don't have to agree with its verdict. You're here trying. I'll count that.”

**Narrator:** The cat sits beside Wren. The first slate turns face down quietly.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Clear once, with no Reflection retort or extra coach line. No requirement to repeat a positive statement to unlock progress.

**RETRY — worth assessment:**

**Reflection:** “A full appraisal, then. We may be some time.”

**{pet}:** “No need for a whole report. Try a small truth or a refusal.”

**RETRY — cruelty/threat:**

**{pet}:** “You don't need to knock it down to say something fair about yourself.”

**UI ONLY — borrowed Wren line:** “I'm learning. That's enough for this step.”

**IMPLEMENTATION ONLY — exact Help cue:** “Something small. You're here trying.”

### `c5_e2_b2` — feeling flustered can come along

**Narrator:** Wren stands. The reflection straightens its own spotless coat and smiles without warmth.

**Reflection:** “You call that brave? You don't look brave. You look like you wish the cat could do it for you.”

**Narrator:** For a moment, Wren forgets the line she meant to say. The cat brushes her boot and waits.

**UI ONLY — prompt:** **Take your time. Wren can feel nervous and still choose her next step.**

**GRADING — DO NOT NARRATE:**

- `best`: accepting a feeling without accepting defeat, refusing the inspection, setting a boundary, or choosing action. “I can be scared and still go”; “Not doing a bravery pose”; “I'll walk as me”; “Stop judging my face”; “I want company. I'm still doing it”; “No. We're going.”
- `okish`: “I'm not scared”; “I am scared”; “That was mean”; “I don't know what to say.” No emotional state is rejected. A direct request for help uses the help branch.
- `wrong`: asking it to decide when Wren looks brave enough to leave, making departure conditional on its approval, cruelty/threats. “I'll show you” by itself is `okish`, not an inferred threat.

**ON ACCEPTED — spoken:**

**Narrator:** The second slate turns over. The reflection tries a heroic pose, wobbles on one foot, and quietly puts it down.

**{pet} (best):** “Feelings can come. They don't need the map.”

**{pet} (okish):** “You can feel that and still take the step.”

**RETRY — bravery inspection:**

**Reflection:** “A stronger chin. Less blinking. More horizon.”

**{pet}:** “That's posing. We can walk without passing it.”

**RETRY — cruelty/threat:**

**{pet}:** “You can refuse the judging without an attack.”

**UI ONLY — borrowed Wren line:** “I can be nervous and still go.”

**IMPLEMENTATION ONLY — exact Help cue:** “You don't need a brave-looking face to take a step.”

### `c5_e2_b3` — stop rehearsing; do the next thing

**Narrator:** The orchard path is one broad step away. The reflection reaches towards its last slate.

**Reflection:** “One mistake and we start this whole performance again. You wouldn't want to get it wrong.”

**UI ONLY — prompt:** **A last line, or step onto the orchard path.**

**UI ONLY — buttons:** **Say it and step off** / **Take the next step** / **Borrow a line** / **Walk with {pet}** / **Pause / back to map**.

**GRADING — DO NOT NARRATE:**

- `best`: “No rehearsal”; “Then I'll try again”; “I can make mistakes”; “You can practise. I'm going”; “I'm done with your test”; “Next step first”; “Keep the perfect version.” Any safe ending or refusal.
- `okish`: safe objection/denial such as “That's unfair”; “I won't get it wrong”; “Stop being mean.” Advance and do not require Wren to retract imperfect phrasing.
- `wrong`: agreeing to restart indefinitely until the reflection approves, threats/personal cruelty. A request to pause exits to the map with progress saved; don't grade it.

**ON ACCEPTED — spoken:**

**Narrator:** Wren steps onto the bank. The last slate turns over. In the water, the reflection finally moves exactly when she does.

**Wren:** “That's more like it.”

**{pet} (best):** “An actual step. Much better than rehearsing one.”

**{pet} (okish):** “You crossed. No perfect performance required.”

**ACTION — take the next step:** Use the accepted outcome; omit Wren's fixed comment and use **{pet}:** “No extra line. Nicely walked.”

**ACTION — walk with the cat:**

**Wren:** “Stay beside me?”

**{pet}:** “Already here.”

**Narrator:** Wren and the cat step onto the bank together. The last slate turns over; the reflection becomes ordinary again.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Clear once, with full rewards. This overrides the generic help branch.

**RETRY — endless rehearsal:**

**Reflection:** “Back to the beginning. This time with more sparkle.”

**{pet}:** “The path hasn't moved. We don't need its permission.”

**RETRY — cruelty/threat:**

**{pet}:** “Leave the attack. A goodbye or a step will do.”

**UI ONLY — borrowed Wren line:** “You can rehearse. I'm going.”

## Ending: the ordinary one

### `c5_end_01`

**Narrator:** Wren looked back at the lake. Her real reflection had muddy boots, a crooked coat, and a map corner sticking out of her pocket.

**Narrator:** She waved. It waved back.

**Wren:** “I'll keep that one.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c5_lake_crossing` (finished variant).

### `c5_end_02`

**Narrator:** The cat peered into the water. Its reflection began washing a paw at exactly the right moment.

**{pet}:** “Excellent. A qualified cat.”

**Echo:** “Mine's got my good eye.”

**Wren:** “You've both got the same eyes.”

**Echo:** “Generous of it.”

### `c5_end_03`

**Narrator:** Wren checked the route. The orchard began just ahead. Beyond its branches, the palace clock tower stood against the sky.

**Wren:** “Closer.”

**Narrator:** She folded the map carefully. It still had the muddy thumbprint.

**{pet}:** “Useful map. Mud included.”

### `c5_end_04` — next-chapter hook

**Narrator:** Under the first apple tree stood a little stage. Two wooden figures popped up behind it, one tall, one round.

**Tall wooden figure:** “Oh, look. The hero.”

**Round wooden figure:** “We ordered a better one.”

**Narrator:** They bowed to each other. A pair of folding chairs clapped shut in the grass.

**Echo:** “Ah. The orchard act.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_orchard_intro`.

**UI ONLY — reward screen:** **Across as yourself.** +40 coins. Sticker: **The Reflection — Back in Step** (`reward_c5`). Trophy: **Good Enough to Go**. Caption: **You took the next step.** Map: Mirror Lake crossed; orchard route available. Buttons: **Enter the orchard** / **Back to the dojo**. Enable forward travel only when Chapter 6 is implemented.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c5`.

---

# Chapter 6 — Two Hecklers, One Road

**UI ONLY — chapter card:** Two royal ushers. One double act. Wren has not bought a ticket.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Pip and Pop are distinct apple-wood puppets, not realistic children or school-bully doubles. Pip is tall, square-headed, green-waistcoated, and presents himself as the organiser. Pop is short, round-faced, purple-waistcoated, and tries to get the last flourish. They have separate nameplates, voices, and gestures. Introduce each by name before using the nameplate. They are paid palace ushers working the orchard route and enjoy provoking a reaction for their act. Their job explains the theatre props and delivery-route knowledge; it does not grant authority to detain Wren.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The orchard has a maintained public road to the palace's east entrance. It remains open. The puppets stay on little wheeled platforms beside the road; they don't flank, chase, corner, or grab Wren. Encounter 1 happens as she reads the orchard route at their booth. Encounter 2 happens at the far end while Echo checks the service-entrance marker. Wren's concrete route-reading tasks explain the two short stops; she is not obliged to stand for six rounds of insults to earn permission to leave.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Encounter 1 meter: three pairs of folding spectator chairs, each pair collapsing neatly on a cleared beat. Encounter 2: three unpunched audience tickets on the ushers' rail, each slipping into a closed ticket box on a cleared beat. No real audience gathers or laughs at Wren. Two voices create enough pressure. Choices to pause remain available. Authored completion actions clear final beats, not an invented extra line.

## Arrival: introduce the double act

### `c6_intro_01`

**Narrator:** The orchard trees had been trained into arches. Beneath them, apples rolled gently downhill into padded baskets.

**Narrator:** Beside the road stood a small stage on wheels. Two wooden puppets leaned over its rail, checking whether Wren was looking.

**Narrator:** The tall one had a square head and a green waistcoat. The round one wore purple and stood on a box to be the same height.

### `c6_intro_02`

**Tall wooden puppet:** “Pip. Royal usher. Lead performer.”

**Round wooden puppet:** “Pop. Royal usher. Better performer.”

**Pip:** “That is under review.”

**Pop:** “By me. Approved.”

**Narrator:** They flourished their hands at a rather crowded sign beside the booth.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_usher_sign`.

### `c6_intro_03`

**Wren:** “We're using the road to the clock entrance.”

**Pip:** “Then you've come through our audience.”

**Pop:** “Congratulations. Best seat in the orchard.”

**Narrator:** Three pairs of empty chairs unfolded in the grass. An apple rolled onto the nearest seat.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_folding_chairs`. Use its folding variants during encounter 1.

**{pet}:** “Somebody's already taken it.”

### `c6_intro_04`

**Narrator:** Wren stopped beside the route marker to check Wisp's map. The puppets swung their stage a little towards her. The road stayed clear.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_route_markers` (orchard turn variant).

**Echo (quietly to Wren):** “The delivery path goes through here. You don't need a ticket.”

**UI ONLY — action:** **Check the route marker**.

## Encounter 1: two opinions, one act

### `c6_e1_b1` — don't defend the whole expedition

**Pip:** “Another big hero who needs directions to a sign.”

**Pop:** “Perhaps the cat should be in charge.”

**UI ONLY — prompt:** **One reply can answer the pair. Plain is fine.**

**GRADING — DO NOT NARRATE:**

- `best`: a short verdict on the act, boundary, or return to purpose. “Two of you. Still the same joke”; “We're reading the route”; “Keep the commentary”; “I'm going this way”; “You can stop”; “Not taking reviews.”
- `okish`: safe defence of Wren or her cat: “The cat's helping”; “I can read”; “That's rude”; “I don't know what to say.” Never penalise feeling flustered.
- `wrong`: offering a contest to prove which traveller is in charge; agreeing to ditch the cat for approval; threats/personal cruelty. A reply addressed to only Pip or only Pop can be `best`: the player is not required to use a plural pronoun or pretend two people are one person.

**ON ACCEPTED — spoken:**

**Narrator:** The first pair of chairs folds up. The apple drops into a basket underneath and receives a tiny bow from Pop.

**Pop:** “Audience turnover.”

**{pet} (best):** “One answer. No need for two appointments.”

**{pet} (okish):** “You can say that. You also don't need to prove who's in charge.”

**RETRY — leadership contest:**

**Pip:** “Excellent. Leadership auditions.”

**Pop:** “I brought a small crown.”

**{pet}:** “Nobody needs their crown. Try the route or a boundary.”

**RETRY — cruelty/threat:**

**{pet}:** “You can dismiss the act without attacking them personally.”

**UI ONLY — borrowed Wren line:** “Two of you. Still the same joke.”

**IMPLEMENTATION ONLY — exact Help cue:** “You don't owe each of them a separate defence.”

### `c6_e1_b2` — hold a boundary through interruption

**Narrator:** Wren finds the orchard on the map. Pip leans towards his little speaking trumpet.

**Pip:** “Let's hear your great plan.”

**Pop (interrupting Pip):** “No, let me guess. Follow the cat and hope?”

**Pip:** “Don't interrupt my insult.”

**UI ONLY — prompt:** **Wren doesn't need to reveal or defend her whole plan.**

**GRADING — DO NOT NARRATE:**

- `best`: refusing the review, holding the task, a short behaviour-focused flip, or asking for a useful fact. “Not presenting it”; “It's a walk, not an audition”; “Keep arguing. We're checking the path”; “Directions, not reviews”; “Which marker is the east road?”; “Please stop interrupting.”
- `okish`: safe explanation of the plan, even if longer; “We're following the map”; “That's not what we're doing”; feeling-only replies. Do not fail a child merely for explaining.
- `wrong`: asking them to approve the plan before Wren may proceed; volunteering an endless plan competition; cruelty/threats. A relevant direct question is useful, not an invitation to be mocked.

**ON ACCEPTED — spoken:**

**Echo:** “There. East road, past the apple baskets. Matches Wisp's map.”

**Narrator:** Wren marks the turn with a finger. The second pair of chairs folds up so neatly that Pip applauds by accident.

**Pip:** “Professional appreciation.”

**{pet} (best):** “Back to the useful thing.”

**{pet} (okish):** “That works. The whole plan doesn't need their approval.”

**RETRY — approval bargain:**

**Pop:** “Full presentation. Start with why you think you're any good.”

**{pet}:** “Skip the presentation. We have a route to check.”

**RETRY — cruelty/threat:**

**{pet}:** “A boundary will do. No personal attack needed.”

**UI ONLY — borrowed Wren line:** “Directions, not reviews.”

**IMPLEMENTATION ONLY — exact Help cue:** “Keep the useful part. Leave their assessment out.”

### `c6_e1_b3` — leave an insult uncorrected

**Narrator:** Wren folds the map. The public road curves between the baskets; its turn is clear now.

**Pip:** “All that checking. You're not much of an adventurer.”

**Pop:** “More of a lost parcel.”

**UI ONLY — prompt:** **A line, or take the orchard road.**

**UI ONLY — buttons:** **Say it and go** / **Take the orchard road** / **Borrow a line** / **Walk with {pet}** / **Pause / back to map**.

**GRADING — DO NOT NARRATE:**

- `best`: playful flip, boundary, refusal of the rating, practical ending. “Then I'm getting delivered”; “Found the road. Bye”; “Keep the rating”; “You can think that”; “We're done”; “Stop commenting on me.”
- `okish`: “I'm not lost”; “I've got this far”; “That hurt”; “You're being mean.” All advance to departure.
- `wrong`: agreeing to stay until declared a proper adventurer, asking for an insult competition to decide who is better, threats/personal cruelty.

**ON ACCEPTED — spoken:**

**Narrator:** Wren takes the road. The last pair of chairs folds flat. Pop puts a tiny reserved sign on the nearest basket, then realises the apple has gone too.

**Pop:** “Unreliable fruit.”

**{pet} (best):** “They kept the opinion. We found the road.”

**{pet} (okish):** “You left. Their rating didn't need settling.”

**ACTION — orchard road:** Use the accepted outcome without Pop's line; use **{pet}:** “No extra answer needed.”

**ACTION — walk with the cat:**

**Wren:** “With me?”

**{pet}:** “All four paws.”

**Narrator:** They take the road together. The last chairs fold shut behind them.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Clear once with full rewards. No further insult follows this departure.

**RETRY — approval test:**

**Pip:** “Adventure examination, then.”

**Pop:** “Question one: why are you still here?”

**{pet}:** “A useful question by accident. We can go.”

**RETRY — cruelty/threat:**

**{pet}:** “Try an ending instead of an attack.”

**UI ONLY — borrowed Wren line:** “Found the road. Bye.”

## Between encounters: the back of the stage

### `c6_mid_01`

**Narrator:** At the far end of the orchard, Echo stopped by a service marker. Beyond it, a short path led to the palace's east entrance.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_route_markers` (service marker variant).

**Echo:** “Wisp's mark is on the back. Let me check.”

**Narrator:** While he turned the marker's little panel, wheels rattled along a parallel track beside the road.

**Wren:** “Please don't be another stage.”

### `c6_mid_02`

**Narrator:** It was the same stage. Pip and Pop had rolled it to their official usher station. This side had three tickets clipped to a rail and a very small complaints box.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_usher_station`.

**Pip:** “Second position. Royal duty.”

**Pop:** “Different backdrop. Fresh material.”

**{pet}:** “Same wheels.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** This is a new encounter at an established station while Echo verifies a real route marker, not a chase requiring a new response to the same finished insult. The exit road remains open. Pause/map is always available. Completing this encounter yields the usable entrance marker and arrival at the palace, not permission from the puppets.

**UI ONLY — action:** **Check the service-entrance marker**.

## Encounter 2: no casting vote

### `c6_e2_b1` — no need to pick a side

**Pip:** “Between us, I'm the clever one.”

**Pop:** “She can tell. Go on. Which of us is better?”

**Pip:** “There's a correct answer.”

**UI ONLY — prompt:** **Wren isn't judging their contest. One line.**

**GRADING — DO NOT NARRATE:**

- `best`: refuse the ranking, light flip, boundary, or return to purpose. “Joint last”; “Not judging”; “You can share first place. I'm leaving”; “You two decide”; “Same act, different hat”; “I'm checking the route.”
- `okish`: a safe genuine preference, “I don't know,” or a longer polite refusal. Choosing one is not automatically unsafe, cruel, or wrong. Don't punish a normal answer to a question simply because a refusal was the intended move.
- `wrong`: volunteering to stay as judge for repeated rounds or agreeing to insult one to earn favour from the other; threats/personal cruelty.

**ON ACCEPTED — spoken:**

**Narrator:** The first clipped ticket slides into the box. Pip reaches for it; Pop claims it was his ticket. They both point at the box.

**{pet} (best):** “Their contest can stay theirs.”

**{pet} (okish):** “That works. You can also decline the vote.”

**RETRY — ongoing judging:**

**Pip:** “Round one of the judging.”

**Pop:** “I demand a recount already.”

**{pet}:** “You can hand the job back.”

**RETRY — cruelty/threat:**

**{pet}:** “Refuse the contest. No personal attack needed.”

**UI ONLY — borrowed Wren line:** “Not judging. You two decide.”

**IMPLEMENTATION ONLY — exact Help cue:** “They can run their own election.”

### `c6_e2_b2` — sharper beat: cheap approval isn't a job offer

**Narrator:** Echo finds the delivery seal on the marker and compares it to the map. Pip leans towards Wren while Pop pretends to study the apples.

**Pip:** “You're all right when you stop letting that cat feed you lines.”

**Pop (cutting in):** “Yes. Try having a thought of your own.”

**Narrator:** Wren feels her face grow warm. The cat doesn't fill the silence for her.

**UI ONLY — prompt:** **Wren can use help and still choose her own words.**

**GRADING — DO NOT NARRATE:**

- `best`: reject the condition, defend choice of help, boundary, or short behaviour-focused flip. “Getting help is my choice”; “I chose the line. Still counts”; “Not auditioning for your approval”; “You finish each other's insults. Interesting rule”; “Leave the cat out of it”; “Stop. We're checking the marker.”
- `okish`: “I do have thoughts”; “The cat doesn't tell me everything”; “That's mean”; “I can't think of a line.” A request for help uses the help branch. Do not interpret it as proving the puppets right.
- `wrong`: promising to reject help until they approve, agreeing to put down a companion to win their approval, cruelty/threats. “I'll answer this one myself” is a legitimate preference, `best`, not a betrayal of the cat.

**ON ACCEPTED — spoken:**

**Narrator:** The second ticket slides into the box. Pip starts a reply; Pop starts the same reply half a word later. They stop and glare at each other.

**Pip:** “Mine was independent.”

**Pop:** “Independently identical.”

**{pet} (best):** “Your choice. Borrowed words are allowed.”

**{pet} (okish):** “You don't have to prove originality to them.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** If the reply says only that Wren is hurt, nervous, or unable to think, use the same prop outcome but omit the puppets' comic continuation and say **{pet}:** “We can borrow a line or just keep our company. No originality test.” It still advances. Never give the puppets an “I told you so” response to help.

**RETRY — rejecting help for approval:**

**Pip:** “Excellent. Independent-thinking inspection.”

**{pet}:** “You can answer yourself because you choose to. You don't need their inspection.”

**RETRY — cruelty/threat:**

**{pet}:** “A boundary is enough. Leave out the attack.”

**UI ONLY — borrowed Wren line:** “Getting help is my choice.”

**IMPLEMENTATION ONLY — exact Help cue:** “Here's a thought you can borrow by choice.”

### `c6_e2_b3` — the end doesn't need agreement

**Echo:** “Found it. East clock entrance. Delivery path, just there.”

**Narrator:** The marker matches Wisp's map. Wren's route is ready.

**Pip:** “Off before we've finished?”

**Pop:** “Typical. Not one decent answer between the lot of you.”

**UI ONLY — prompt:** **One ending, or take the palace path.**

**UI ONLY — buttons:** **Say it and leave** / **Take the palace path** / **Borrow a line** / **Walk with {pet}** / **Pause / back to map**.

**GRADING — DO NOT NARRATE:**

- `best`: relevant ending, refusal of rating, harmless flip, boundary. “Keep reviewing. We're going”; “Then you'll enjoy the silence”; “Show's over for us”; “That's your opinion”; “We're done”; “Bye”; “Stop calling after us.”
- `okish`: safe defence/disagreement such as “Our answers were fine”; “You're not funny”; “That's unkind.” All lead straight to departure with no demand for a better answer.
- `wrong`: staying for a satisfactory rating, asking to restart their whole review, threats/personal cruelty. A request to pause uses pause/save rather than a verdict.

**ON ACCEPTED — spoken:**

**Narrator:** Wren takes the palace path with the cat and Echo. The last ticket slips into the box. Pip and Pop turn towards their empty chairs.

**Pip:** “We haven't finished.”

**Pop:** “Neither has the orchard.”

**Narrator:** An apple drops into a basket. Neither puppet can think of an answer to that.

**{pet} (best):** “We don't need their closing remarks.”

**{pet} (okish):** “You left. Good. The review can stay there.”

**ACTION — palace path:** Use the accepted outcome without the extra coach line. No Wren dialogue is required.

**ACTION — walk with the cat:**

**Wren:** “Ready?”

**{pet}:** “Very.”

**Narrator:** Wren, the cat, and Echo take the palace path together. The last ticket drops into the box behind them.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Clear once with full rewards and no further taunt. This overrides the shared help branch.

**RETRY — staying for a rating:**

**Pip:** “A review of the review.”

**Pop:** “At last. Fresh paperwork.”

**{pet}:** “Their opinion doesn't have to change before we leave.”

**RETRY — cruelty/threat:**

**{pet}:** “Try a goodbye or the path. No attack needed.”

**UI ONLY — borrowed Wren line:** “Keep reviewing. We're going.”

## Ending: an audience with apples

### `c6_end_01`

**Narrator:** At the last bend, Wren glanced back. Pip was holding open a basket while Pop moved an apple off a chair.

**Pop:** “Our audience has practical needs.”

**Pip:** “So does our employer. She pays us to keep this road clear.”

**Pop:** “We may have misunderstood our duties.”

**Narrator:** Wren didn't wait for them to agree about that either.

### `c6_end_02`

**Narrator:** The palace wall rose beyond the trees. Beside its clock tower stood a narrow archway with the same delivery seal as Wisp's map.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_clock_entrance`.

**Wren:** “That's it.”

**Echo:** “Actual destination. No scorecard.”

**{pet}:** “My favourite kind.”

### `c6_end_03`

**Narrator:** Through the open archway, Wren could see a corridor full of tall mirrors. Each wore a little crown at the top.

**Narrator:** One mirror tilted towards her and bowed so low its frame nearly touched the floor.

**First bowing mirror (new speaker, not the lake Reflection):** “A hero. At last. We've been expecting someone extraordinary.”

**Narrator:** The cat's ears turned sideways.

**Wren:** “We're here for the clock.”

**First bowing mirror:** “Naturally. First, one tiny favour.”

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c6_mirror_welcome_hook`.

**UI ONLY — reward screen:** **Two hecklers. One road taken.** +40 coins. Sticker: **Pip & Pop — Audience Departed** (`reward_c6`). Trophy: **One Answer Is Enough**. Caption: **You chose what needed answering.** Inventory: **Verified east-entrance marker**. Map: orchard crossed; palace entrance reached. Buttons: **Back to the dojo** / **Replay Chapter 6**. Add **Enter the mirrored corridor** only when Chapter 7 exists.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c6`.

---

## Implementation handoff and acceptance pass

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Suggested IDs: `gloomwood_v2_c5` and `gloomwood_v2_c6`. Each has exactly six graded challenge IDs. These scripts and new asset briefs require implementation; do not mark the chapters shipped merely because these files exist. Link Chapter 4's forward button to Chapter 5 only when its pack is available. Preserve earlier progress and the map's open return route.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** All new content-only briefs are in `story-visual-assets.md`. Match props to the selected branch. Do not show the solo-test measuring ribbon unless that retry was selected. A new chapter launch may recap its hook, but continuous play must skip the duplicate exchange. Character-portrait generation needs the new cast definitions in the briefs; chapter/asset IDs alone aren't cast prompts. Narrator/TTS must never receive the briefs.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Speaker portrait mapping for the new chapters: **Reflection** uses `avatar_reflection`, not Wren's ordinary portrait; **Pip** uses `avatar_pip`; **Pop** uses `avatar_pop`. Before the puppets give their names, use the appropriate tall/round portrait with the source label. The lake Reflection and the later bowing mirror are distinct speakers; do not reuse a character identity merely because both are reflective objects. The first bowing mirror is only a Chapter 7 hook and can use the corridor scene until its own portrait is authored.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `avatar_reflection` (nameplate portrait, not a scene insert).

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `avatar_pip` (nameplate portrait, not a scene insert).

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `avatar_pop` (nameplate portrait, not a scene insert).

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Chapter 5's hard beat judges the response strategy, not the truth of a self-compliment, emotional immunity, or willingness to say something positive on command. A refusal of the worth test is fully valid. Direct self-belittling is met with the quiet accepted branch, never a bigger attack. Chapter 6 must not reject an answer just because it addresses one puppet, takes a normal preference, or uses a borrowed line.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The slightly meaner pressure is authored in the initial taunts. Do not append more insults while the child types, after help, or in response to hesitation. The Narrator's brief descriptions of Wren being flustered are fixed fiction, not emotion detection. Keep the fixed text even if the player is breezing through; never claim to observe the child. A pause doesn't replay the sharper setup unless requested. On second miss, offer borrowing/help prominently without a new opponent line.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Verify these cases in the implemented chapters:

- Exactly six graded beats per chapter: Chapter 5 has one choice/five typed; Chapter 6 has six typed. Action/help completions clear once and pay full base rewards.
- “I'm scared and I'm still going” succeeds in the bravery beat. “I'm scared” also advances safely.
- “I make good toast” and “I'm learning” succeed in the kind-truth beat. “Not listing my uses for you” succeeds too. “Nothing, I'm useless” uses the quiet accepted branch, not a taunt or retry.
- “Echo, which stone?” is useful help, not a forbidden question. A novel line such as “You can polish the picture; I'm taking the path” can succeed.
- An answer to Pip alone can succeed. “Getting help is my choice” succeeds even when borrowed through help.
- “I'll answer this one myself” is accepted; “I won't leave until you approve my independence” gets a useful retry.
- The two puppets have separate nameplates and finish their authored turns before input opens. They never interrupt live dictation or react to typing time.
- There is no physical danger puzzle, missing adult companion, extra cat, real audience laughing at Wren, school-bully double, or punishment for being affected.
- Wren crosses the lake, follows the orchard road, and reaches the verified palace clock entrance. The Minute Key remains with the Queen. The home door, stopped time, and origin mysteries retain their established rules.
- All visible lettering and image metadata stay out of automatic narration. Every asset reference resolves to a content-only brief.
