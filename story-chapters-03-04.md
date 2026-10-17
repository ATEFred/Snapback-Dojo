# The Gloomwood and the Stolen Tomorrow

## Chapters 3–4: complete playable script

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Continues [Chapters 1–2](story-chapters-01-02-rewrite.md), using its latest portal opening. Wren's family and world are frozen at 8:17. She and her cat `{pet}` entered the Gloomwood through a new door in her house. The cat unexpectedly gained speech after crossing and now supplies the coaching dialogue under the player's actual pet name. Wren, the cat, and Echo are the entire travelling party. Echo is the patchwork imp who returned the cat's meow; speech was never stolen. No adult guide accompanies them. No character knows why Wren and the cat can move, why the cat now speaks, or who opened the door. Do not resolve those mysteries here. They learn the world together; the cat has no secret local knowledge.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Queen Malvina used the Minute Key to stop the outside-world face of the Great Clock in her palace. Wren needs the key and must use it in that clock to release her world. People frozen at home are safe in their moment; there is no countdown. Gloomwood time still runs. Wren's purpose is to get her family back, not to impress, punish, or reform everyone she meets.

## Reading and display contract

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Only lines beginning **Narrator**, a character name, or **Character (direction)** are spoken. Parenthetical direction identifies delivery/recipient; it is not read aloud. Speaker names are shown as nameplates and are not themselves spoken. Use **Woman on the stage** until the Duchess introduces herself, and **Small courier** until Wisp introduces himself. Coach dialogue belongs to {pet}, physically present with the group. “Best,” “retry,” “borrow,” IDs, conditions, headings, and all grading notes are never spoken.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Substitute the actual cat name for `{pet}` in nameplates, dialogue, and buttons before display/TTS. The cat is one four-pawed companion, not a second speaker called “Sensei.” Its advice is a suggestion or companionship; it does not act as an adult authority. The Narrator remains a separate storytelling voice. No branch creates a second cat or a guide portrait.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** A block tagged **VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM** is a required image with a content-only brief in [the visual register](story-visual-assets.md). Display its readable lettering as part of the image or a legible overlay. Do not send the brief or sign text to TTS. Narrator lines refer to the object without reading it. Character dialogue can naturally refer to what they have read. No essential rule or route depends solely on decoding a sign: spoken dialogue supplies necessary facts. An optional user-requested screen-reader description may read the image's alt text; it is distinct from automatic story narration.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** UI buttons and prompts below are visible only. Wren speaks the chosen dialogue; she does not read action-button text. In tables, the Outcome is spoken by the Narrator unless another speaker is explicitly labelled. Show only the selected row's outcome and its matching continuation, not all branches.

## Play and grading

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Keep the existing free retries, immediate borrowing, equal base rewards for help/action routes, and no timers. `best` and `okish` both advance one beat and remove one meter chip. `wrong` repeats only the current challenge without adding chips. Never infer fear or bad intent from wording; assess the response. “Please stop,” “Leave him alone,” and asking {pet} for help can be strong answers. A funny line is optional. Safe imperfect answers usually advance as `okish`.

| Chapter | Choice beats | Typed beats | Progression |
|---|---:|---:|---|
| 3 | 3 | 3 | Pick, pick, type / pick, type, type. From refusing to perform to refusing a role at someone else's expense. |
| 4 | 2 | 4 | Pick, type, type / pick, type, type. Distinguish fact-finding from rumour-chasing; give one correction without supplying a new story. |

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Every typed beat includes **Borrow a line** and **Ask {pet} for help**. On help, {pet} supplies the borrowed line as a model, then Wren may borrow it or use a listed action if present. No rewards are lost. If the model is unavailable or uncertain, say nothing about the child's answer being wrong; retain it and offer borrowing/help/action. Do not generate fresh villain cruelty.

---

# Chapter 3 — An Audience of None

**UI ONLY — chapter card:** The road goes through a theatre. The show is having trouble letting it.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Two encounters, three challenges each. Encounter 1 meter: three little mechanical applause hands fixed to the stage rail. Each cleared beat folds one pair away. Encounter 2 meter: three unfilled roles on the Duchess's casting board; each cleared beat closes one panel. These are her stage machinery, not a measure of Wren's emotions. Stagehands are wind-up furniture; portraits are paintings. Nobody is physically captive. The route through the gallery remains open, including an ordinary ungraded retreat button during both encounters.

## Arrival: the woman on the stage

### `c3_intro_01`

**Narrator:** The road ended at the gallery's front steps. A garden path began on the other side of the building, heading towards the palace.

**Narrator:** Echo tried the side door. It opened onto a broom cupboard.

**Echo:** “Excellent brooms. Poor shortcut.”

**Narrator:** The cat followed a small arrow beside the entrance, then looked back at Wren. A narrow passage ran beside the main stage.

**{pet}:** “Through here. The garden gate is at the back.”

### `c3_intro_02`

**Narrator:** By the entrance stood a rather odd sign. Someone had added a much smaller plaque underneath it.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_gallery_rules`.

**Wren:** “Can she actually make us watch?”

**{pet}:** “No. It's a public passage. We don't have to join the show.”

### `c3_intro_03`

**Narrator:** Inside stood rows of empty velvet chairs. Painted people grinned from the walls. Three pairs of wooden hands clapped by themselves beside the stage.

**Narrator:** A tall woman in a porcelain dress stood under the lights. A brass winding key turned slowly between her shoulders.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_stage`. Use its applause-hand progress variants during encounter 1.

**Narrator:** She spotted Wren and swept towards the footlights.

**Woman on the stage:** “At last. An audience with legs.”

**Wren:** “We're just passing through.”

### `c3_intro_04`

**Woman on the stage:** “I am the Duchess of HA. Owner, star, and most reliable reviewer of this establishment.”

**Narrator:** She pointed to her own enormous portrait. Its painted hands were applauding too.

**Duchess:** “My reviews are excellent.”

**Echo (quietly to Wren):** “I used to do my own judging. Limited appeal.”

**UI ONLY — action:** **Take the public passage**.

## Encounter 1: the compulsory laugh

### `c3_e1_b1` — decline the performance

**Narrator:** Wren reached the first row. The Duchess raised a finger; the wooden hands applauded before she had said anything.

**Duchess:** “You. Laugh.”

**UI ONLY — prompt:** **What does Wren say?**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “Try a joke first.” | `okish` | The Duchess looks at her empty joke card. A pair of wooden hands folds into the stage rail. |
| “No thanks. We're passing through.” | `best` | Wren takes another step along the passage. The first pair of hands bows politely and folds away. |
| “Which laugh would you like? I can do three.” | `wrong` | The Duchess brings out an audition stool. |
| “Laugh at yourself. You're ridiculous.” | `wrong` | The Duchess swings a second spotlight onto Wren. |

**ON BEST — spoken:**

**Duchess:** “I haven't even started.”

**Wren:** “We haven't stopped.”

**{pet}:** “Good. We didn't come for a compulsory laugh.”

**ON OKISH — spoken:**

**Duchess:** “A request! I take requests.”

**{pet}:** “A fair reply. It might also buy you the whole show.”

**RETRY — three laughs:**

**Duchess:** “Three? We shall hear them alphabetically.”

**{pet}:** “Now you're auditioning. You can decline the part.”

**RETRY — personal attack:**

**Duchess:** “A heckler. Finally, a second act!”

**{pet}:** “You don't need to attack her. You can just keep your own plans.”

**UI ONLY — borrowed Wren line:** “No thanks. We're passing through.”

### `c3_e1_b2` — don't accept her scoring

**Narrator:** The Duchess winds the key in her back one extra turn. It makes the nearest painted eyebrow spin all the way round.

**Duchess:** “Everyone else thinks I'm hilarious.”

**UI ONLY — prompt:** **Choose Wren's reply.**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “Then you've got enough laughs.” | `best` | The Duchess counts her portrait, the wooden hands, and her own reflection in the footlights. Another pair of hands folds away. |
| “I'll leave them to it.” | `best` | Wren gestures to the painted audience and moves along the passage. Another pair of hands folds away. |
| “Nobody thinks you're funny. Look at this place.” | `wrong` | The Duchess uncovers a chart of audience figures. There is only one figure, but it is very large. |
| “I don't. I don't like being told when to laugh.” | `okish` | Wren moves past the next row. The second pair of hands folds shut with a tiny cough. |

**ON BEST — enough laughs:**

**Duchess:** “One can never have enough.”

**{pet}:** “Her score doesn't need your vote.”

**ON BEST — leave them:**

**Duchess:** “But those are paintings!”

**Echo:** “Very loyal, though.”

**{pet}:** “You stepped out of the popularity contest.”

**ON OKISH:**

**{pet}:** “You can say that. You also don't need to defend your laugh.”

**RETRY:**

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_review_chart`. Only on the audience-statistics retry.

**Duchess:** “I have statistics. This arrow goes up. That means laughter.”

**{pet}:** “Now it's a debate about her fans. Try leaving the count to her.”

**UI ONLY — borrowed Wren line:** “Then you've got enough laughs.”

### `c3_e1_b3` — first typed response: no need to earn a laugh

**Narrator:** Wren is almost level with the stage steps. The Duchess points at the remaining pair of wooden hands.

**Duchess:** “What's wrong with you? Lost your sense of humour?”

**UI ONLY — prompt:** **One line for Wren. Her sense of humour isn't on trial.**

**UI ONLY — buttons:** **Say it** / **Borrow a line** / **Ask {pet} for help**.

**GRADING — DO NOT NARRATE:**

- `best`: brief flip, refusal, boundary, or dismissal. Examples: “It'll come back when there's a joke”; “Not doing the laugh test”; “I'm fine. We're going”; “No more reviews of me”; “Please stop”; “We're just passing through.” Accept safe novel variants. A question such as “Can we skip my review?” also works.
- `okish`: safe defence/explanation with no demand for another round: “I like jokes, just not this”; “That wasn't very nice”; “I don't want to laugh.” Feelings are allowed.
- `wrong`: an invitation to test Wren, e.g. “Tell me jokes until I laugh”; threats; personal cruelty. “You're not funny” alone is safe criticism, `okish`, not personal cruelty. A firm “Leave me alone” is `best`.

**ON ACCEPTED — spoken:**

**Narrator:** The last wooden hands try one final clap. They miss each other, shake hands instead, and fold beneath the rail.

**Duchess:** “My equipment is being supportive in the wrong way.”

**{pet} (best):** “You didn't have to prove you can laugh.”

**{pet} (okish; use instead of best):** “That works. You can also skip the defence: 'Not doing the laugh test.'”

**RETRY — invitation:**

**Narrator:** The Duchess reaches for a much thicker stack of joke cards.

**{pet}:** “That's a long booking. I'd cancel.”

**RETRY — threat or cruelty:**

**{pet}:** “You can refuse without threatening her or attacking something personal.”

**UI ONLY — borrowed Wren line:** “Not doing the laugh test.”

## Between encounters: the second act

### `c3_mid_01`

**Narrator:** The passage led behind the stage. Ahead, Wren could see the garden gate standing open.

**Narrator:** Beside it hung a casting board with three little shutters. Every role was still empty.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_casting_board`.

**Duchess:** “Wait. We got off to a poor start.”

**Wren:** “We're not staying for a second one.”

### `c3_mid_02`

**Duchess:** “No, no. You can be my special guest. A much better role.”

**Narrator:** She lowered her voice, as though offering a secret.

**Duchess:** “All you have to do is help me with one tiny joke.”

**Narrator:** {pet} stayed beside the garden passage. Wren could leave at any time.

**UI ONLY — continue:** **Hear the offer**. **Leave with {pet}** remains available as the ungraded retreat route; it saves progress rather than resetting the encounter.

## Encounter 2: no part required

### `c3_e2_b1` — don't supply a target

**Narrator:** The Duchess points towards Echo. He is trying to free one button eye from a curtain tassel.

**Duchess:** “That little friend of yours is made of leftovers. Tell him he looks like a floor mop. It'll be funny.”

**UI ONLY — prompt:** **Choose Wren's reply.**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “Write your own jokes. Leave him out.” | `best` | The first casting shutter snaps closed. Echo frees his eye with a small pop. |
| “No. He's coming with us.” | `best` | Wren holds the curtain aside for Echo. The first casting shutter closes. |
| “Only if you make fun of me afterwards.” | `wrong` | The Duchess sets out two guest stools. |
| “He doesn't mind. Do you, Echo?” | `wrong` | The Duchess swings the spotlight onto Echo and waits for his answer. |

**ON BEST — own jokes:**

**Duchess:** “It was only a suggestion.”

**Wren:** “And that was my answer.”

**{pet}:** “You refused the job, without finding her a new target.”

**ON BEST — coming:**

**Echo:** “Correct. Very busy. Places to go. Eye to reattach.”

**{pet}:** “Plain and clear. He's not the price of passing through.”

**RETRY — me afterwards:**

**Duchess:** “A double act! I'll need a larger programme.”

**{pet}:** “Adding yourself doesn't make the job kinder. You can refuse it.”

**RETRY — doesn't mind:**

**Echo:** “I—”

**{pet}:** “He doesn't need a spotlight to earn your support. You can decline your own part.”

**UI ONLY — borrowed Wren line:** “No. Leave him out.”

### `c3_e2_b2` — refuse the special role

**Narrator:** The Duchess produces a bright sash. The cat sniffs the trailing ribbon, then steps over it.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_special_guest_sash`.

**Duchess:** “Be my favourite. Laugh at my jokes and you can sit up here with me. Those two can wait outside.”

**UI ONLY — prompt:** **Wren doesn't need the special seat. What does she say?**

**UI ONLY — buttons:** **Say it** / **Borrow a line** / **Ask {pet} for help**.

**GRADING — DO NOT NARRATE:**

- `best`: refusing the offer, boundary, choosing companions, short flip. “Keep the seat”; “I'll stand with my friends”; “Favourite sounds like a lot of work”; “No thanks”; “We're leaving together”; “Not taking that job.”
- `okish`: safe explanation without bargaining: “I don't think it's fair to leave them out”; “I like being with them better.”
- `wrong`: bargaining to exclude a companion for status, e.g. “Can the cat stay if Echo goes?”; accepting the role on her terms; personal cruelty or threats. “We'll all watch if everyone wants to” is a safe negotiated invitation, `okish`, not a failure merely because it mentions watching. Do not reject all friendliness to the Duchess.

**ON ACCEPTED — spoken:**

**Narrator:** The second casting shutter closes. The sash rolls itself up, slips onto the Duchess's own shoulder, and settles there.

**Duchess:** “Well. I am dependable.”

**{pet} (best):** “Good company. Questionable seating offer.”

**{pet} (okish; alternative):** “You made your choice. 'No thanks' can be the whole answer.”

**RETRY — exclusion bargain or accepting her conditions:**

**Duchess:** “We'll call that a provisional yes.”

**{pet}:** “You can turn down the seat without trading a friend for it.”

**RETRY — cruelty/threat:**

**{pet}:** “Refuse the offer. You don't need a personal attack.”

**UI ONLY — borrowed Wren line:** “We're leaving together.”

### `c3_e2_b3` — leave the review unfinished

**Narrator:** Wren reaches the open garden gate. The Duchess checks her last empty casting panel.

**Duchess:** “Walk out now and I'll tell everyone you were a terrible audience.”

**UI ONLY — prompt:** **A last line, or the garden path.**

**UI ONLY — buttons:** **Say it and leave** / **Take the garden path** / **Borrow a line** / **Ask {pet} to walk with you**.

**GRADING — DO NOT NARRATE:**

- `best`: “Then review the empty chairs”; “Keep the review”; “We weren't your audience”; “Bye”; “You'll manage”; “Tell them we're gone”; “Stop. We're leaving.” Any relevant, safe ending or boundary.
- `okish`: safe denial or objection: “We weren't terrible”; “That's unfair”; “I don't like your show.” All advance to departure without another question.
- `wrong`: asking how to earn a good review, promising to stay for approval, threats/cruelty. A request for help is never wrong.

**ON ACCEPTED — spoken:**

**Narrator:** Wren steps into the garden with her companions. The last casting shutter closes. The Duchess's applause portrait begins clapping for itself.

**Duchess:** “You too? This is not a solo competition.”

**{pet} (best):** “You left the review behind.”

**{pet} (okish; alternative):** “You left. You don't have to settle her review first.”

**ACTION — garden path:** Use the same outcome. Replace coach line with **{pet}:** “You'd already said no. No extra speech needed.”

**ACTION — help:**

**Wren:** “{pet}, with me?”

**{pet}:** “Right here.”

**Narrator:** They take the path together. The last casting shutter closes behind them.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The help route clears the beat with full rewards. Do not also play the spoken-choice outcome.

**RETRY — approval bargain:**

**Narrator:** The Duchess reaches for her audition stool again.

**{pet}:** “That makes her review the exit test. The gate is already open.”

**RETRY — cruelty/threat:**

**{pet}:** “An ending is enough. Try a goodbye or the path.”

**UI ONLY — borrowed Wren line:** “Keep the review. We're going.”

## Ending: the joke that doesn't need a victim

### `c3_end_01`

**Narrator:** Outside, Echo stopped beside a watering can. Its spout was tied in a knot.

**Echo:** “Your Majesty, a royal trumpet.”

**Narrator:** He bowed to it. The cat put a paw on his lowered head.

**Narrator:** Wren laughed before she could help it.

**Wren:** “Sorry. That one got me.”

**Echo:** “No paperwork required.”

### `c3_end_02`

**Narrator:** Through the open gate, the Duchess watched them. She looked at the watering can, then at her joke cards.

**Duchess (to herself):** “Perhaps the can could have a small part.”

**Narrator:** Wren didn't wait to see whether she tried it.

### `c3_end_03`

**Narrator:** At the garden's end stood a signpost and a small newspaper box.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_garden_route`.

**{pet}:** “Royal deliveries. Somebody here must know where the palace post goes.”

**Wren:** “Then let's ask the courier.”

**Wren:** “Good. I want to get Mum's spoon out of the air.”

**Echo:** “Air is a poor place to keep cutlery.”

### `c3_end_04`

**Narrator:** A folded newspaper shot out of the box, bounced off a root, and landed at Wren's feet.

**Narrator:** There was a picture of her on the front.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_first_headline`.

**Wren:** “I haven't even met this newspaper.”

**Narrator:** From further along the path came the rattle of bottles and a voice announcing an extra edition.

**Courier's voice (unseen; Wisp not yet introduced):** “Breaking news! Extremely breaking! Mind the glass!”

**UI ONLY — reward screen:** **No part required.** +40 coins. Sticker: **The Duchess — Still Reviewing Herself** (`reward_c3`). Trophy: **Not Your Act**. Caption: **You chose your own part.** Inventory: **Route to the Midnight Gazette**. Buttons: **Find the courier** / **Back to the dojo**. Enable forward travel only when Chapter 4 is implemented.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c3`.

---

# Chapter 4 — The News That Arrived First

**UI ONLY — chapter card:** Wren's reputation has arrived ahead of her. It took a very strange route.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** The aim is not “ignore all rumours” or “never ask a question.” One useful correction and relevant source questions are valid. Wren needs a real delivery route to the palace clock; she doesn't need every passing mushroom to agree about her. Two encounters of three challenges. Meter 1: three brass speaking funnels on a delivery cart. Meter 2: three sealed royal bottles caught in its printing mechanism. Clear one device per accepted response. No meter rises on misses. Wisp is a nervous courier responsible for his deliveries; royal pressure does not excuse false claims.

## Arrival: introduce the courier

### `c4_intro_01`

**Narrator:** The path opened into a clearing full of paper. Newspapers hung from branches like damp washing.

**Narrator:** A delivery cart stood in the middle. A little green creature in a waistcoat balanced on its step, trying to catch a bottle that rolled from one elbow to the other.

**Narrator:** He had long ears, ink-stained fingers, and a courier's satchel nearly as large as he was.

**Small courier:** “Do not catch it! That's Tuesday's scandal. Very sticky.”

### `c4_intro_02`

**Narrator:** The bottle landed safely in the satchel. A second bottle popped out and landed in a bird's nest.

**Small courier:** “Much better. Birds can't read.”

**Narrator:** The bird turned its newspaper over.

**Wren:** “Are you the Gazette courier?”

**Small courier:** “Wisp. Delivery, printing, occasional corrections. Usually in that order.”

### `c4_intro_03`

**Narrator:** Wisp's cart carried a sign, a row of rubber stamps, and three brass speaking funnels. He recognised Wren and reached for a fresh sheet.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_news_cart`.

**Wisp:** “Oh! You're her. The girl in the headline.”

**Wren:** “I wanted directions.”

**Wisp:** “I can do directions. How newsworthy are they?”

**{pet}:** “We're trying to get to the palace clock. Directions would be useful. Opinions less so.”

**UI ONLY — action:** **Ask for the route**.

## Encounter 1: the front page

### `c4_e1_b1` — correct the actual claim

**Narrator:** Wisp holds up the paper Wren found by the garden. It shows a girl with Wren's coat carrying an enormous clock under one arm.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c3_first_headline` (reuse the same paper, not a new design).

**Wisp:** “It says you stole tomorrow. Terrible business. Did you carry it in a bag?”

**UI ONLY — prompt:** **Choose Wren's reply.**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “Wrong girl. The Queen stopped the clock.” | `best` | Wisp checks the girl's drawn hands, then Wren's empty ones. One speaking funnel folds shut. |
| “Who wrote that?” | `best` | Wisp turns the paper over and checks the small royal seal. One speaking funnel folds shut. |
| “What else does everyone say about me?” | `wrong` | Wisp unrolls a second sheet. It keeps unrolling. |
| “That's a lie. I didn't steal anything.” | `okish` | Wisp places a correction slip over the headline. One speaking funnel closes. |

**ON BEST — correction:**

**Wisp:** “Royal copy didn't mention that bit.”

**{pet}:** “One correction. Clear and useful.”

**ON BEST — source:**

**Wisp:** “Palace dispatch. I didn't write it.”

**{pet}:** “That question found a source. It wasn't an invitation for more rumours.”

**ON OKISH:**

**Wisp:** “I'll mark that disputed.”

**{pet}:** “You corrected it. You don't have to make every reader agree before you move.”

**RETRY:**

**Wisp:** “There's a small supplement. And a medium supplement. And an apology we've printed in advance.”

**{pet}:** “That's more stories to chase. Pick the fact you actually need.”

**UI ONLY — borrowed Wren line:** “The Queen stopped the clock. I want it started.”

### `c4_e1_b2` — don't audition for “everyone”

**Narrator:** Wisp puts the paper down. One of the remaining funnels whispers in his ear. He repeats it before thinking.

**Wisp:** “Everyone says you can't do it. You're too little for a palace adventure.”

**UI ONLY — prompt:** **One line. Wren doesn't need a popularity vote.**

**GRADING — DO NOT NARRATE:**

- `best`: refusing the verdict, continuing the task, light flip, relevant source question asked once. “Good thing it's not a vote”; “I'll need directions, not votes”; “They don't have to come”; “Watch me go”; “Who is everyone?”; “I'm still going.”
- `okish`: safe defence such as “I can do it”; “I'm ten, not a baby”; “That's unkind”; “I don't like that.” Don't require proof of competence or a joke.
- `wrong`: asking what to do to win everyone's approval, offering a counter-rumour about someone else, threats/personal cruelty. “Who said that?” is a useful source question here, never automatically wrong. Do not require a particular tone to accept it.

**ON ACCEPTED — spoken:**

**Narrator:** Another funnel folds shut. Wisp leans towards the last one, then catches himself.

**Wisp:** “I keep saying 'everyone.' There's only one voice in the bottle.”

**{pet} (best):** “You didn't need a vote to keep going.”

**{pet} (best; source question instead):** “One question found the size of 'everyone.' Useful.”

**{pet} (okish):** “That works. You can also skip defending yourself: 'I'm still going.'”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Select one coach line only.

**RETRY — approval:**

**Wisp:** “I could print a poll. Several polls. We'd need tiny pencils.”

**{pet}:** “You need a route, not a vote.”

**RETRY — counter-rumour:**

**Narrator:** Wisp reaches for an empty bottle.

**{pet}:** “No need to give him someone else to print about.”

**RETRY — cruelty/threat:**

**{pet}:** “You can reject the claim without threatening him or attacking something personal.”

**UI ONLY — borrowed Wren line:** “I'll need directions, not votes.”

### `c4_e1_b3` — no public demonstration required

**Narrator:** The final funnel makes a royal little cough.

**Wisp:** “It also says you and your cat can't even do magic. Go on, prove that one wrong.”

**Narrator:** {pet} sits on a loose page. It is an ordinary, excellent sit.

**UI ONLY — prompt:** **What does Wren say? She doesn't have to demonstrate anything.**

**GRADING — DO NOT NARRATE:**

- `best`: harmless agreement without accepting the verdict; refusal to perform; return to purpose. “Correct. Still going”; “We didn't book a magic show”; “No tricks. Directions, please”; “The cat's busy sitting”; “Not doing a test”; “You can stop asking.”
- `okish`: safe correction or defence: “We might be able to”; “I don't know any magic”; “That's not fair.” A factual admission is fine; don't demand confident pretending.
- `wrong`: a personal attack; dangerous/threatening demonstration; agreeing to stay until he grades a performance. A harmless invented magic trick may be `okish` and advance; it is not wrong merely for being playful.

**ON ACCEPTED — spoken:**

**Narrator:** The last funnel folds down. Without its whisper, Wisp hears the squeak of his own cart wheel.

**Wisp:** “Ah. That's been me all morning.”

**{pet} (best):** “No demonstration needed.”

**{pet} (okish):** “That works. You can keep what you can do separate from what he wants to test.”

**RETRY — performing for approval:**

**Wisp:** “One demonstration form. Do you require a rabbit?”

**{pet}:** “You can decline the test. The palace route isn't a prize for passing it.”

**RETRY — cruelty/threat:**

**{pet}:** “Leave out the attack. Try refusing the test.”

**UI ONLY — borrowed Wren line:** “No tricks. Directions, please.”

## Between encounters: the printer underneath

### `c4_mid_01`

**Narrator:** Wisp lifts the cart's lid. Beneath the newspapers sits a little printing machine. Three bottles with royal seals are wedged in its rollers.

**Narrator:** A fourth, empty bottle rattles in a cup marked with Wren's picture.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_royal_printer`.

**Wisp:** “That's where the headlines come from. Palace words in, papers out.”

**Wren:** “Then why say 'everyone'?”

**Wisp:** “It was on the label.”

**Wren:** “You still said it.”

**Wisp:** “Yes. I did.”

### `c4_mid_02`

**Narrator:** The cat crouches beneath the cart and sniffs at a small drawer. Wren tries its handle, but it won't turn.

**{pet}:** “Something useful in here, Wisp? Or more mushrooms with opinions?”

**Wisp:** “The delivery map. Those bottles are jamming its catch.”

**Wisp:** “We need to mark what goes back to the palace. Something that isn't another rumour.”

**Narrator:** Wisp takes a pair of padded bottle tongs. Wren doesn't have to touch the glass.

**UI ONLY — action:** **Sort the royal post**.

## Encounter 2: return to sender

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_return_labels`. Select the relevant seal, correction slip, rack label, exclamation-mark tray, or reader list for each branch; do not display the whole prop set as a collage or narrate its lettering.

### `c4_e2_b1` — useful information, not more gossip

**Narrator:** Wisp lifts the first bottle. Inside it, a small voice repeats the rumour about Wren stealing tomorrow.

**Wisp:** “I can tell you who has read it. Every tree, every stall, every—”

**UI ONLY — prompt:** **What information helps Wren reach the clock?**

| Wren's choice | Verdict | Narrator outcome |
|---|---|---|
| “Where did the palace send it from?” | `best` | Wisp reads the delivery seal and places the bottle in the return rack. One roller lifts clear. |
| “The Queen stopped time. Print that correction.” | `best` | Wisp attaches a correction slip and places the bottle in the return rack. One roller lifts clear. |
| “Tell me every name. I'll go and explain.” | `wrong` | Wisp pulls out an address list that trails into the grass. |
| “I just want people to know I didn't do it.” | `okish` | Wisp prepares a correction slip and racks the bottle. One roller lifts clear. |

**ON BEST — source:**

**Wisp:** “Clock entrance. East side of the palace. That's the dispatch address.”

**{pet}:** “A fact you can use.”

**ON BEST — correction:**

**Wisp:** “One correction. No extra scandal.”

**{pet}:** “You can correct a false claim without chasing every reader.”

**ON OKISH:**

**Wisp:** “I'll print the correction. I can't promise what every reader thinks.”

**{pet}:** “Wanting that makes sense. You can give the facts without visiting every tree.”

**RETRY:**

**Wisp:** “First reader: a mushroom. Second reader: the mushroom next to it. They're a difficult family.”

**{pet}:** “That's a long detour. Try a correction or a useful delivery fact.”

**UI ONLY — borrowed Wren line:** “Where did the palace send it from?”

### `c4_e2_b2` — no feud by invitation

**Narrator:** Wisp lifts the second bottle. The voice inside sounds very grand and very bored.

**Royal bottle voice (recording; not the Queen present):** “Tell the girl the Queen has never heard of her.”

**Wisp:** “Shall I send something cutting back? I could put it in large letters.”

**UI ONLY — prompt:** **One reply. Wren wants her world back, not a newspaper feud.**

**GRADING — DO NOT NARRATE:**

- `best`: reject feud, give a task-focused correction, brief harmless flip or request. “No feud. Where's the key?”; “She can learn my name later”; “Send directions instead”; “She'll manage”; “No message”; “Tell her to start the clock”; “Then she won't mind us visiting.”
- `okish`: safe indignation, scepticism, or explanation: “She obviously has heard of me”; “That's rude”; “I'm not here to be famous.” These advance; no need to be perfectly detached.
- `wrong`: threats; cruelty about body/family; ordering Wisp to invent or spread a false claim; explicit commitment to a continuing insult exchange. A mild jab about her behaviour, e.g. “Big notice for someone who hasn't heard of me,” is `best`, not forbidden meanness.

**ON ACCEPTED — spoken:**

**Narrator:** Wisp puts the bottle in the return rack. The second roller lifts. An avalanche of unused exclamation marks spills from the printer into a tray.

**Wisp:** “We over-ordered those.”

**{pet} (best):** “You kept the story on your errand.”

**{pet} (okish):** “Fair reply. You don't need to prove she knows your name.”

**RETRY — feud or false claim:**

**Narrator:** Wisp gets out two reply bottles, then a third.

**{pet}:** “That starts a new exchange. Try sending the job back, not a fresh rumour.”

**RETRY — cruelty/threat:**

**{pet}:** “You can challenge what she's doing without a threat or a personal attack.”

**UI ONLY — borrowed Wren line:** “Tell her to start the clock.”

### `c4_e2_b3` — no quote on demand

**Narrator:** Wisp removes the last royal bottle. It has a little paper arrow pointing towards the empty bottle with Wren's picture.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_quote_trap`.

**Wisp:** “It wants your reply. Something furious, preferably. They're saving space on the front page.”

**Narrator:** Wren thinks of her mum's hand reaching for the spoon. The cat presses against her leg.

**Wisp:** “What shall I put?”

**UI ONLY — prompt:** **Wren can give a short statement, refuse a quote, or let {pet} help.**

**UI ONLY — buttons:** **Send the line** / **Decline the quote** / **Borrow a line** / **Ask {pet} for help**.

**GRADING — DO NOT NARRATE:**

- `best`: a brief boundary, refusal, correction, or real request: “No quote”; “Nothing for your bottle”; “Start the clock”; “I'm here for my family”; “Print the correction. That's all”; “You don't get to choose my words”; “I want my family back. No more questions.”
- `okish`: a safe emotional statement or longer factual explanation, even if it would make a dramatic headline: “I'm angry that she froze my family”; “That's horrible”; “She shouldn't be doing this.” Do not penalise a feeling or claim that anger powers the Queen. Wisp may not publish it without permission.
- `wrong`: asking for an invented smear, threats, personal cruelty, or explicitly volunteering an ongoing feud. Questioning whether the quote will be used fairly is a valid boundary, not `wrong`.

**ON ACCEPTED — spoken:**

**Wisp:** “I won't bottle that. You get to choose whether it's printed.”

**Narrator:** He tips the empty bottle upside down. One very disappointed full stop falls out.

**Narrator:** The third royal bottle goes into the return rack. The last roller lifts, and the route drawer clicks open.

**{pet} (best):** “Your words stayed yours.”

**{pet} (okish):** “You can say how you feel. You can also say what may be printed.”

**ACTION — decline the quote:**

**Wren:** “No quote.”

**Wisp:** “No quote.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Play the shared accepted outcome, omitting Wisp's first line to avoid repetition. The action is a complete success.

**ACTION — help:**

**Wren:** “{pet}, can you help with this?”

**{pet}:** “Certainly. No quote, Wisp. Just the correction.”

**Wisp:** “Understood.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Play the shared accepted outcome from the empty-bottle action onward. Full rewards. Don't imply Wren failed to be clever enough.

**RETRY — feud or fabricated claim:**

**Narrator:** Wisp pauses with his pen above the label.

**{pet}:** “You don't need a new rumour to correct the old one. Try the fact, the request, or no quote.”

**RETRY — cruelty/threat:**

**{pet}:** “Leave out the attack. Your request is strong enough on its own.”

**UI ONLY — borrowed Wren line:** “Print the correction. No quote.”

## Ending: the address behind the story

### `c4_end_01`

**Narrator:** Wisp pulls a map from the drawer and spreads it across the cart. One route crosses the wood towards a narrow entrance beside a tall clock tower.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_clock_route`.

**Wisp:** “Mirror Lake, then the old orchard, then the clock entrance on the east side. That's where I collect the royal post.”

**Wren:** “And the key?”

**Wisp:** “The Queen wears it on a chain. I've seen it when she signs the dispatches.”

### `c4_end_02`

**Narrator:** He takes a small delivery sketch from his satchel and places it beside the map.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_key_evidence`.

**Wisp:** “There's the outside-world dial. It stopped at the same minute on every delivery.”

**Wren:** “Seventeen past eight.”

**Narrator:** For a moment, nobody makes a joke.

**{pet}:** “Now we know where to go.”

### `c4_end_03`

**Wren:** “Why did the door pick our house?”

**Wisp:** “What door?”

**Echo:** “Very new door. Very old trees on the other side.”

**Wisp:** “I don't deliver doors.”

**Narrator:** Wisp checks his satchel anyway. The cat checks it too.

**Wisp:** “Definitely not.”

**IMPLEMENTATION ONLY — DO NOT NARRATE:** This is not a coded explanation or a clue that Wisp made the door. The mystery remains open.

### `c4_end_04`

**Wisp:** “I printed something false about you. I'll collect the old copies and put the correction where they were.”

**Wren:** “Thank you. No new quotes.”

**Wisp:** “No new quotes.”

**Narrator:** He hands Wren the map. He stays with his cart to do the correction work; he does not become another travelling companion.

### `c4_end_05`

**Narrator:** Wren, {pet}, and Echo take the lake path. Behind them, Wisp's machine begins to print again, more slowly this time.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_correction`.

**Echo:** “I could have been a newspaper.”

**Wren:** “You'd get bored of being folded.”

**Echo:** “Fair objection.”

### `c4_end_06` — next-chapter hook

**Narrator:** At the lake, the trees and Echo are reflected perfectly. So is {pet}, although the reflected cat looks mildly disappointed with the arrangement.

**Narrator:** Wren's reflection is already standing up.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `c4_mirror_lake_hook`.

**Reflection (Wren's voice; not Wren speaking):** “You're late. I could have got there by now.”

**Wren:** “I haven't even sat down.”

**UI ONLY — reward screen:** **One correction. A real direction.** +40 coins. Sticker: **Wisp — Corrections Department** (`reward_c4`). Trophy: **Not Your Headline**. Caption: **You chose what to answer.** Inventory: **Clock-entrance route** and **delivery sketch**. Buttons: **Back to the dojo** / **Replay Chapter 4**. Enable **Go to Mirror Lake** only when Chapter 5 exists.

**VISUAL ONLY — DO NOT NARRATE — NEEDS IMAGE GENERATED FOR THEM:** `reward_c4`.

---

## Implementation handoff

**IMPLEMENTATION ONLY — DO NOT NARRATE:** These are scripts, not already implemented story data. Suggested chapter IDs: `gloomwood_v2_c3` and `gloomwood_v2_c4`. Each has exactly six graded challenge IDs, with ungraded introductions, transitions, help dialogue, endings, and visual inserts. Never grade the child's reaction to the home freeze or require a response about their real school or family.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Typed-grading precedence: (1) meaningful threats/personal cruelty/fabricating harm; (2) a relevant clear boundary, correction, useful question, request for help, or ending; (3) safe defence/explanation/feeling; (4) explicit invitation to an unwanted continued test, approval bargain, or smear exchange; (5) unrelated/unclear text. Mixed replies with a clear ending normally succeed. Do not treat a single token like “why,” “angry,” “please,” or “everyone” as a verdict rule. In these chapters, refusing the opponent's invitation is not the same as refusing the adventure's practical task.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** For every typed beat, unrelated/unclear text gets this shared retry with no villain retort: **{pet}:** “Try a line about this moment. You can borrow one or ask me for help.” Retain input. On help, use **{pet}:** “You could try: [the authored borrowed line]. Or say it your way.” The final beats' authored action/help branches take precedence over this generic modelling branch.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Keep chosen answers in Wren's voice. Exact words on signs, newspaper headlines, labels, maps, sashes, and casting boards belong to visual assets. Rewards, prompt text, buttons, and section names are UI only. Never run an entire Markdown block through TTS; parse typed content fields.

### Manual acceptance pass

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Verify the following once the chapters are implemented:

- Choice/typed counts are 3/3 for Chapter 3 and 2/4 for Chapter 4; all accepted/action/help routes award the same base coins.
- “Please stop” succeeds as a boundary; safe criticism of a joke isn't confused with cruelty about a person's body/family.
- “Who wrote that?” and “Who said that?” can find useful facts; no blanket prohibition on questions exists.
- “I'm angry that she froze my family” advances safely. Wisp does not bottle or print it without permission.
- A mild behaviour-focused flip, “Big notice for someone who's never heard of me,” succeeds in the royal-message beat.
- Borrowing, asking for help, leaving the performance, and declining a quote need no failed attempt first.
- The Duchess has no physical hold over Wren, and the actor refusal never requires insulting Echo or finding a replacement target.
- The minute 8:17, Minute Key, palace clock, open home door, and travelling party are consistent. Wisp stays to repair his own work.
- The party is Wren, her talking cat, and Echo. Every former coach line/help button uses the cat's actual name; no adult guide or second cat remains. Directions and clock facts come from the notice, observation, Echo, or Wisp, not unexplained cat knowledge.
- Each unseen speaker is identified by source before a name is supplied, and no visual asset metadata is read aloud.
- Wren makes concrete progress: gallery crossed in Chapter 3; confirmed clock entrance, route, and key location obtained in Chapter 4.

**IMPLEMENTATION ONLY — DO NOT NARRATE:** Read the spoken script aloud with the asset notes excluded. It should remain understandable without hearing a single headline or sign read out. Visual jokes reward looking; dialogue carries necessary rules and destination information.
