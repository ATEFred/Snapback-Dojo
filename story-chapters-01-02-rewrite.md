# The Gloomwood and the Stolen Tomorrow

## Chapters 1–2: complete playable script

Proposed replacement opening for story mode. This is a new script, not an edit to the shipped story pack. Character and encounter IDs below are proposed IDs for implementation. The original `plannedstory.md` remains unchanged.

**Player character:** Wren, a young apprentice bellkeeper who lives at the edge of the Gloomwood. The player chooses her words and actions; the story uses her name, rather than switching between Wren and “you.” **Pet companion:** `{pet}`, the storybook version of the player's dojo pet, already Wren's friend when the story begins. Pet actions should work for every evolution stage; do not assume the pet can speak. **Coach and travelling companion:** Sensei, an older village guide with a long coat and a crooked walking stick. Sensei is physically present, introduced before speaking, and available for help. **Narrator:** a separate storyteller, who describes events but is not a character in the scene. **Setting:** a crooked, cosy, twilight wood. Strange things happen; nothing here is gory or realistically threatening.

**The adventure:** In Wren's village, ringing the morning bell brings the sunrise. Today is Wren's first turn as bellkeeper, but Queen Malvina steals the bell before she can ring it. Wren sees her village stuck at the edge of morning: no sunlight, closed flowers, and the same miserable rooster trying to start the day. She sets out with her pet and Sensei to retrieve the bell from Malvina's palace and bring the morning home. The Queen wants everyone to visit her palace and praise her before she returns it. Wren wants the bell back, not a place in the Queen's audience.

The player-facing title is **The Gloomwood and the Stolen Tomorrow**. Do not award Wren the title “Unbothered” before she has done anything. She is allowed to feel things throughout this adventure.

---

## Shared play and grading contract

This section is for implementation; it is not an opening lecture to the player.

- No timers in these chapters. Read aloud is optional. Every narration screen advances on a tap.
- Every spoken line has a visible speaker name. Use separate portraits/nameplates for **Narrator**, **Wren**, **Sensei**, **Echo**, and **Toastbrig**. Narrator text is labelled **Narrator** in this script; it is not Sensei's dialogue. Sensei's advice comes from Sensei standing with the group. Do not merge narration and character speech into one anonymous text box.
- Text marked **Display** is written on an object, not spoken by that object. Read-aloud can use the narrator voice with an introduction such as “The sign says.” **Setup** text marked as narration is read to the player. Headings, prompts, grading notes, and branch instructions are implementation/UI text, not character speech.
- In choice tables, all quoted dialogue in the Choice column belongs to Wren. Show **Wren** above the dialogue choices. Action choices remain labelled actions. Outcome cells are narrator text; any character dialogue following them gets its own labelled line. Typed-answer examples are possible Wren lines, not new speakers.
- Each chapter contains two encounters of three challenge beats. Use the existing three-chip encounter meter. Chapters have six challenge beats each, but their tasks and consequences vary.
- Chapter 1: six choice beats. Chapter 2: four choice beats followed by two typed beats.
- Shuffle choice order. The order printed here is for review only. Never display the verdict labels beside the options.
- `best` and `okish` both clear a challenge and remove one chip. More than one answer can earn `best`. `wrong` retries that challenge; it does not add chips, undo progress, or cost rewards.
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

## Opening: the morning that wouldn't start

### `c1_intro_01` — narration

**Narrator:** Wren lived in the last cottage before the Gloomwood, where the trees leaned over the fence to see what was going on.

**Narrator:** She was learning to be the village bellkeeper.

**Narrator:** Every morning, someone rang the little brass bell in the village square. Its note travelled over the rooftops, and the sun rose to meet it.

**Narrator:** Today was Wren's first turn.

### `c1_intro_02` — narration

**Narrator:** Wren reached the square wearing her best coat. Her friend {pet} trotted beside her, determined to inspect the bell before anybody rang it.

**Narrator:** Sensei, the old village guide who was teaching Wren, waited by the bell stand. Their coat had deep pockets, and their walking stick was almost as crooked as the trees.

**Sensei:** “Ready?”

**Wren:** “Ready.”

**Narrator:** Wren reached for the bell rope.

### `c1_intro_03` — narration

**Narrator:** The rope fell into her hand.

**Narrator:** Above it, the bell hook was empty.

**Narrator:** A paper bat fluttered down and landed on the stand. It wore enormous spectacles and carried a folded notice.

**Paper bat:** “Royal delivery. Please admire the seal before complaining.”

**Wren:** “Where's our bell?”

**Narrator:** The bat opened its notice.

### `c1_intro_04` — the paper bat reads the royal notice

**Paper bat (reading Queen Malvina's notice):**

> BY ORDER OF QUEEN MALVINA THE MAGNIFICENT:
>
> I have borrowed your morning bell.
>
> If you would like the sun back, come to my palace and tell me how magnificent I am.
>
> Everyone must attend. Applause should be enthusiastic.
>
> P.S. I will decide when you have finished.

### `c1_intro_05` — dialogue

**Narrator:** Wren looked across the square. The houses were still blue in the almost-morning light. The sunflowers stood shut beside the bakery.

**Narrator:** A rooster on the bakery roof tried a crow. It came out as a tired cough.

**Wren:** “She's keeping the whole village waiting.”

**Sensei:** “Yes. And asking us to thank her for it.”

**Wren:** “I'm getting our bell back.”

**Paper bat:** “Would you like me to put you down for applause?”

**Wren:** “No.”

**Narrator:** The bat wrote something very small on its form.

### `c1_intro_06` — narration

**Narrator:** Sensei unrolled a map on the empty bell stand.

**Sensei:** “The palace is across the wood. A bridge first, then the old gallery, then the palace road.”

**Wren:** “Will you come?”

**Sensei:** “Of course. You lead. I'll help when you need me.”

**Narrator:** {pet} planted both front paws on the map.

**Wren:** “Yes. You too.”

**Narrator:** Wren packed the map and a lantern. Then the three of them took the path into the Gloomwood.

**Narrator:** At the first fork, Wren stopped to read the signpost.

**Display — signpost:**

> PALACE →
>
> ALSO PALACE ←
>
> DON'T ASK ME ↓

### `c1_intro_07` — dialogue

**Narrator:** {pet} opened their mouth to complain about the unhelpful sign.

**Narrator:** A tiny trumpet sounded from a bush.

**Wren:** “That is not your normal noise.”

**Voice in the bush (Echo, not yet introduced):** “Improved it.”

### `c1_intro_08` — narration

**Narrator:** A small patchwork imp climbed out of the bush and onto a wooden crate. He had mismatched button eyes and a jar full of glowing sounds.

**Narrator:** His badge supplied an introduction.

**Display — the imp's badge:**

> ECHO
>
> OFFICIAL JUDGE OF YOU

**Narrator:** Inside Echo's jar, one furious meow bounced against the glass.

**Sensei, quietly to Wren:** “An echo imp. They collect sounds. That one's collected something that isn't his.”

### `c1_intro_09` — dialogue

**Wren:** “Give the meow back.”

**Echo:** “Win it back. I've always wanted a contest.”

**Narrator:** He unfolded a judge's stand. Three paper stars dangled from it.

**Sensei:** “You came for a meow. Let's see whether you need to enter his contest.”

**Transition button:** **Get the meow back**

## Encounter 1: the audition nobody requested

### `c1_e1_b1` — refuse the audition

**Echo:** “Go on, then. Impress me.”

**Prompt:** What does Wren say?

| Choice | Verdict | Outcome |
|---|---|---|
| “I'm here for the meow.” | `best` | **Narrator:** A paper star drops off the stand. Echo catches it, tries to pin it back, and pins his sleeve to the wood. |
| “You first.” | `okish` | **Narrator:** Echo draws breath for a demonstration. His trumpet gives one small squeak. He stamps his foot; a star falls off. |
| “I can do loads of impressive things.” | `wrong` | **Narrator:** Echo produces an entry form so long it rolls off the crate. |
| “Your face looks like a dropped sock.” | `wrong` | **Narrator:** Echo pulls a second crate beside his own and labels it **INSULT CONTEST: ROUND ONE**. |

**Best follow-up:**

**Echo:** “You're supposed to audition.”

**Sensei:** “You skipped the audition. Good.”

**Okay follow-up:**

**Echo:** “I haven't warmed up.”

**Wren:** “Keep the warm-up. I'll take the meow.”

**Sensei:** “Short, and it worked. 'You first' can also buy you a whole performance.”

**Retry: impressive things**

**Echo:** “Excellent. List them. Alphabetically. No, by shininess.”

**Sensei:** “Now he's judging your talents. Bring it back to what you came for.”

**Retry: dropped sock**

**Echo:** “My turn! Your face looks like— hang on, I need a sock.”

**Sensei:** “A new contest. Try refusing the first one.”

**Borrow:** “I'm here for the meow.”

### `c1_e1_b2` — use his contradiction

**Narrator (setup):** Echo frees his sleeve. He points at Wren with the authority of someone standing on borrowed furniture.

**Echo:** “Well? What have you got to say for yourself?”

**Wren:** “I'd—”

**Echo:** “Nobody asked you.”

**Prompt:** Choose Wren's reply.

| Choice | Verdict | Outcome |
|---|---|---|
| “You just did.” | `best` | **Narrator:** Echo looks at his clipboard. It reads **ASK HER SOMETHING**. The second star slips off. |
| “Then you won't need an answer.” | `best` | **Narrator:** Wren closes her mouth. Echo opens his. Nothing comes out. The second star lands in it. |
| “Yes you did! You said, 'What have you got to say for yourself?'” | `okish` | **Narrator:** Echo consults the clipboard, turns it upside down, and loses the second star. |
| “Everyone else likes hearing me talk.” | `wrong` | **Narrator:** Echo flips to a blank page headed **EVERYONE ELSE**. |

**Best feedback, “You just did”:**

**Echo:** “That question was decorative.”

**Sensei:** “His own words did the work.”

**Best feedback, “Then you won't”:**

**Echo:** “I might need a small answer.”

**Sensei:** “You let the contradiction sit there. No explanation needed.”

**Okay feedback:**

**Echo:** “I remember. I was there.”

**Sensei:** “You spotted it. Next time, 'You just did' saves some breath.”

**Retry:**

**Echo:** “Names? References? A signed statement from a beetle?”

**Sensei:** “You don't need witnesses to prove you're worth hearing. His question is right there.”

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

**Sensei:** “Exactly. You didn't need his score.”

**Best feedback, “Keep the prize”:**

**Echo:** “It's a very exclusive prize.”

**Narrator:** {pet} makes the tiny trumpet noise again.

**Sensei:** “Clear request. No audition attached.”

**Retry: neither are you**

**Echo:** “Then we'd better find out who's worse. Best of nineteen!”

**Sensei:** “That's another round. You can leave the score unsettled.”

**Retry: how to win**

**Echo:** “First rule: I may add rules. Second rule: see first rule.”

**Sensei:** “He gets to move the finish line. Try stepping out of the race.”

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

**Narrator:** It now said:

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

**Sensei:** “You've got your meow. Keep your own errand in view.”

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
| “Fine. I'll never talk again.” | `wrong` | **Narrator:** Echo tries to stamp **NO TALKING** on the map. The stamp misses and hits his own hand. |

**Best feedback, spoken:**

**Echo:** “How long is the next bit?”

**Narrator:** Wren traces the route with one finger.

**Sensei:** “You answered once, then chose what to do.”

**Best feedback, action:**

**Echo:** “That's a very rude map.”

**Sensei:** “You had something more useful to look at.”

**Retry: what's wrong**

**Echo:** “At last. A review! Shall I start with the vowels?”

**Sensei:** “That lets him inspect your voice. His comment doesn't need an answer.”

**Retry: never talk**

**Echo:** “Excellent. A permanent rule. I'll need a larger stamp.”

**Sensei:** “Quiet for a moment is a choice. Giving up your voice is much too much.”

**Borrow:** Highlight the map action. The lifeline does not always have to lend dialogue.

### `c1_e2_b2` — your purpose outranks his opinion

**Narrator (setup):** Wren spots an old bridge drawn on the map. Beyond it, a road curls towards the palace.

**Echo:** “Oh, off to save tomorrow? You think you're some big hero?”

**Prompt:** Choose Wren's answer.

| Choice | Verdict | Outcome |
|---|---|---|
| “I'm getting our bell back.” | `best` | **Narrator:** Wren folds the map. Echo looks at his notes, which have plenty about heroes and nothing about returning stolen property. Another wheel folds away. |
| “You can think that.” | `best` | **Narrator:** Wren puts the map away. Echo waits for her to correct him. She doesn't. Another wheel folds away. |
| “I don't think I'm a hero! I never said that!” | `okish` | **Narrator:** Echo holds up both hands. Wren finishes putting the map away; another wheel folds away. |
| “I'll prove I'm a better hero than you.” | `wrong` | **Narrator:** Echo produces two badges reading **HERO TRIALS**. One is upside down. |

**Best feedback, bell:**

**Echo:** “That's it? No crown? No statue?”

**Wren:** “A morning would do.”

**Sensei:** “Your reason. No application for his approval.”

**Best feedback, think that:**

**Echo:** “I can think other things as well.”

**Wren:** “Busy day for you.”

**Sensei:** “You left his opinion with him.”

**Okay feedback:**

**Echo:** “It was a guess.”

**Sensei:** “You corrected him. Fair enough. You can also skip proving what you never claimed.”

**Retry:**

**Echo:** “Trial one: dramatic standing. Trial two: cape maintenance.”

**Sensei:** “He's judging again. You have a reason to go without beating him.”

**Borrow:** “I'm getting our bell back.”

### `c1_e2_b3` — keep the last word

**Narrator (setup):** The actual path is visible now. Small pale mushrooms mark the way to the bridge. Wren starts along it.

**Echo:** “Walk away and I get the last word!”

**Prompt:** Finish the encounter.

| Choice | Verdict | Outcome |
|---|---|---|
| “Keep it.” | `best` | **Narrator:** Wren walks on. Echo opens his mouth, delighted. The stage's final wheel folds away before he can say anything. |
| **[Action] Follow the mushroom path.** | `best` | **Narrator:** Wren keeps walking. Echo announces “Ha!” to the back of the empty stage. Its last wheel folds away. |
| “No, I get the last word!” | `wrong` | **Narrator:** Echo rings a small bell labelled **EXTRA ROUND**. |
| “Only because I can't think of anything.” | `okish` | **Narrator:** Wren walks on. The final wheel folds away. Echo's answer is lost under the stage folding shut. |

**Best feedback, spoken:**

**Echo:** “Then my last word is—”

**Narrator:** The stage folds into a suitcase with Echo sitting inside it.

**Echo, muffled:** “—ow.”

**Sensei:** “You let him have the word. You kept going.”

**Best feedback, action:**

**Narrator:** The suitcase closes gently around his hat.

**Echo:** “Ha is an excellent last word.”

**Narrator:** Nobody disputes this.

**Sensei:** “No extra line required.”

**Okay feedback:**

**Sensei:** “You left. That counts. Next time you can leave without marking your own answer.”

**Retry:**

**Echo:** “No, I do. No, you do. No, I— this could take YEARS.”

**Sensei:** “He can keep the word. You can keep going.”

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

**Narrator:** He left it beside a bush labelled **MRS. BRAMBLE'S LUGGAGE**.

**Narrator:** Then he joined them on the path.

**Narrator:** {pet} inspected him, inspected the jar, and walked on.

**Narrator:** Echo kept a little distance and his hands out of the jar. Wren checked the path ahead.

### `c1_end_05` — Sensei

**Sensei:** “You don't have to win every little contest someone offers. Some aren't worth entering.”

### `c1_end_06` — hook

**Narrator:** Ahead, a bridge creaked. Beside it sat an enormous troll in a kettle helmet, peering through a little wooden inspection window.

**Narrator:** He spotted Wren's feet.

**Troll at the bridge (Toastbrig, not yet introduced):** “BOOT INSPECTION!”

**Narrator:** Echo sighed.

**Echo:** “He used to do hats.”

### Reward screen

**Heading:** **Meow recovered. Tomorrow still missing.**

- +40 coins.
- Sticker: **Echo — Not Currently Judging**. Art: Echo's badge crossed out, with **DIRECTIONS** written beneath it.
- Trophy: **Keep the Last Word**. Caption: “You had somewhere better to be.”
- Story inventory: **Palace directions**.
- Companion unlocked: **Echo**, under Wren's rules.

**Buttons:** **On to the bridge** / **Back to the dojo**

---

# Chapter 2 — The Bridge Inspector

**Chapter card:** One bridge. One inspector. An alarming number of forms.

**Practice:** a light flip; harmless agreement without self-belittling; noticing a changed demand; a clear boundary; repeating it; leaving an argument unfinished.

**Difficulty:** first four challenges are choices. Final two allow typed replies with an immediate **Borrow a line** option and a separate **Ask Sensei for help** action. Each typed challenge has several accepted strategies.

**Mechanic:** Toastbrig's inspection booth has three **HOLD UP** signs. Each cleared challenge folds one down. After Wren reaches the far bank, Toastbrig opens a portable complaints desk with three file drawers. Each cleared challenge closes one. Don't use emotional distress as his health bar.

## Opening: standards of footwear

### `c2_intro_01` — narration

**Narrator:** The bridge crossed a stream the colour of cold tea.

**Narrator:** The troll who had shouted “BOOT INSPECTION” sat at the entrance behind a desk much too small for him.

**Narrator:** He had a plank for a back, a kettle for a helmet, and a notebook held between two enormous fingers.

### `c2_intro_02` — narration

**Narrator:** His booth carried a sign:

**Display — the troll's name and job:**

> TOASTBRIG
>
> BRIDGE INSPECTOR
>
> BOOTS, HATS, OTHER OPINIONS

**Narrator:** Below it, in much smaller writing:

**Display — inspection rules:**

> The bridge is open to everyone.
>
> Inspections are optional.

### `c2_intro_03` — dialogue

**Toastbrig:** “HALT. Those boots aren't adventure boots.”

**Narrator:** Wren looked at her boots.

**Narrator:** They had mud on them, a loose lace, and no opinion about adventure.

**Echo, quietly:** “He inspected a centipede last week. It's still waiting for the verdict.”

### `c2_intro_04` — dialogue

**Wren:** “We need to cross. The Queen's got our morning bell.”

**Toastbrig:** “Then you'll need especially good boots.”

**Narrator:** He raised three **HOLD UP** signs. One was upside down.

**Sensei:** “Read his small sign. Then decide how much boot discussion you need.”

**Transition button:** **Cross the bridge**

## Encounter 1: the inspection

### `c2_e1_b1` — a small flip

**Toastbrig:** “Those boots aren't adventure boots.”

**Prompt:** Choose Wren's reply.

| Choice | Verdict | Outcome |
|---|---|---|
| “They got me here.” | `best` | **Narrator:** Toastbrig looks at Wren, then the road, then the boots. He ticks **ARRIVED**. A sign folds down. |
| “I'm crossing in these.” | `best` | **Narrator:** Wren points towards the bridge. Toastbrig checks the optional-inspection notice. A sign folds down. |
| “They're proper adventure boots. The shop said so.” | `wrong` | **Narrator:** Toastbrig searches his notebook for **SHOPS WHICH MIGHT BE WRONG**. |
| “At least I don't wear a kettle.” | `wrong` | **Narrator:** Toastbrig turns the notebook to **HELMET DEFENCE**. Several pages are already filled in. |

**Best feedback, got me here:**

**Toastbrig:** “Yes. Well. Arrival is one of the things boots do.”

**Sensei:** “You used the boots' actual job. Neat.”

**Best feedback, crossing:**

**Toastbrig:** “I haven't approved them.”

**Wren:** “The bridge is open.”

**Sensei:** “You stated the plan. No shoe trial.”

**Retry: shop**

**Toastbrig:** “I'll need a receipt, a witness, and a drawing of the shopkeeper's ankles.”

**Sensei:** “Now the boots need evidence. You can cross without proving they're special.”

**Retry: kettle**

**Toastbrig:** “INSULATED. RAINPROOF. EXCELLENT WHISTLE.”

**Narrator:** His helmet whistles. A passing moth falls off a leaf.

**Sensei:** “New argument: his hat. Try keeping your own journey in view.”

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
| “Fine. Everything I wear is stupid.” | `wrong` | **Narrator:** Toastbrig starts to write **EVERYTHING**, runs out of room, and turns the notebook sideways. |

**Best feedback, hello:**

**Toastbrig:** “That bird isn't qualified to approve boots.”

**Narrator:** The bird squeaks back at him.

**Sensei:** “You kept the squeak and dropped the insult.”

**Best feedback, crossing:**

**Toastbrig:** “But I noticed the squeak.”

**Wren:** “You did.”

**Narrator:** Wren keeps moving.

**Sensei:** “A boot can squeak without it becoming a case to defend.”

**Retry: denial**

**Toastbrig:** “Shall we hear from the boot?”

**Narrator:** Squeak.

**Sensei:** “You can agree about a noise without agreeing there's something wrong with you.”

**Retry: everything**

**Toastbrig:** “Everything? I only inspected two boots.”

**Sensei:** “That's a much bigger claim than his. Keep the true bit: one boot squeaks.”

**Borrow:** “Saves me saying hello.”

### `c2_e1_b3` — moving goalposts

**Narrator (setup):** Wren reaches the middle of the bridge. Toastbrig wheels his desk alongside on tiny castors.

**Toastbrig:** “Boots aside. Now you need a hat. No hat, no crossing.”

**Prompt:** The inspection is still optional. Choose Wren's answer.

| Choice | Verdict | Outcome |
|---|---|---|
| “New rule. Same answer. I'm crossing.” | `best` | **Narrator:** Toastbrig flips between **BOOTS** and **HATS** in his notebook. The last sign folds down. |
| “I'll skip the inspection.” | `best` | **Narrator:** Wren steps past the wheeled desk. The last sign folds down and becomes a little seat. |
| “Would my hood count?” | `wrong` | **Narrator:** Toastbrig produces a ruler labelled **HOODS: POSSIBLY HATS**. |
| “You can't change the rules! That's cheating!” | `okish` | **Narrator:** Toastbrig searches for an official rule allowing new rules. Wren reaches the far bank while he searches; the last sign folds down. |

**Best feedback, same answer:**

**Toastbrig:** “But this is a hat objection. Entirely different department.”

**Sensei:** “Different demand. Same choice for you.”

**Best feedback, skip:**

**Toastbrig:** “People never read that bit.”

**Wren:** “Useful bit.”

**Sensei:** “You didn't need a better hat argument. The inspection was optional.”

**Okay feedback:**

**Toastbrig:** “I have a subsection about cheating. Somewhere.”

**Sensei:** “You spotted the change. Good. You can name it without staying for a rules debate.”

**Retry:**

**Toastbrig:** “Depends. Hood height? Hood ambition? Has the hood previously been a hat?”

**Sensei:** “Another thing to prove. You can decline the inspection.”

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

**Display — complaints sign:**

> COMPLAINTS ABOUT THE INSPECTION
>
> MUST BE DISCUSSED AT LENGTH

### `c2_mid_03` — dialogue

**Toastbrig:** “You haven't explained why you ignored my excellent boot advice.”

**Narrator:** Wren's hands felt a little tight around the map. She loosened them.

**Sensei:** “You can be annoyed. You still get to choose the next words.”

**Narrator:** Three drawers popped open beneath the new sign.

**Transition button:** **Finish the boot discussion**

## Encounter 2: the complaints department

The troll stays behind his desk beside the bridge. He does not chase, grab, surround, or physically restrain Wren. His voice carries; the path ahead is open. This is a verbal persistence exercise, not a test of tolerating danger.

### `c2_e2_b1` — a plain boundary

**Toastbrig:** “Come back and answer properly. What's wrong with a boot inspection?”

**Prompt:** Wren has crossed. What does she say now?

| Choice | Verdict | Outcome |
|---|---|---|
| “No more boot talk.” | `best` | **Narrator:** Wren faces the palace path. The first drawer shuts. Toastbrig's **BOOT TALK** form sticks out like a paper tongue. |
| “I don't want to discuss my boots. We're going.” | `best` | **Narrator:** Wren signals to her companions. The first drawer shuts around the edge of a long questionnaire. |
| “Nothing! It's just that we have to find the bell, and the village is waiting, and—” | `wrong` | **Narrator:** Toastbrig pulls out a **REASONS TO LEAVE** form. It has room for forty-seven reasons. |
| “Please stop talking about my boots.” | `best` | **Narrator:** Wren turns towards the path. The first drawer shuts. Toastbrig reaches for a form, then discovers it is inside. |

**Best feedback, no more:**

**Toastbrig:** “But what about socks?”

**Narrator:** Wren looks down the path.

**Sensei:** “A clear boundary. You can keep it short.”

**Best feedback, don't want:**

**Toastbrig:** “I have several excellent follow-up points.”

**Sensei:** “You said what you wanted and what you're doing.”

**Best feedback, please stop:**

**Toastbrig:** “But I had a diagram.”

**Sensei:** “Polite can still be firm. You asked him to stop; you don't owe him a debate.”

**Retry:**

**Toastbrig:** “I'll put 'bell' under B. Village under V. We could be here a while.”

**Sensei:** “Your reasons are real. He doesn't need the whole list. Try the boundary.”

**Borrow:** “No more boot talk.”

### `c2_e2_b2` — first typed answer: keep the boundary

**Narrator (setup):** Toastbrig pulls a pencil from behind the kettle. It is a fence post with a point.

**Toastbrig:** “I only said they were squeaky. Can't you take a joke?”

**Prompt:** **Write one line for Wren. She doesn't have to prove she likes jokes.**

**Input placeholder:** `What does Wren say?`

**Buttons:** **Say it** / **Borrow a line** / **Ask Sensei for help**

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

**Sensei (best; repeated boundary):** “Same boundary. No fresh argument.”

**Sensei (best; other close):** “That ends your part of the discussion.”

**Sensei (okay):** “That works. A shorter version is: 'Heard it. Moving on.'”

**Sensei (okay; feeling only):** “You can say that. You can add: 'Stop. I'm going.'”

Use exactly one coach line, selected by response strategy. Do not add a generated lecture.

#### Retry packages

**Personal attack:**

**Toastbrig:** “My kettle has an EXCELLENT reputation.”

**Sensei:** “That starts a kettle argument. Try closing the boot one.”

**Threat:**

**Narrator:** Toastbrig tucks the desk behind him.

**Sensei:** “Skip the threat. A boundary is enough here.”

**Invitation:**

**Narrator:** Toastbrig turns to a fresh page.

**Toastbrig:** “Well, since you asked—”

**Sensei:** “That offers him another round. Try finishing your part.”

**Permission to leave:**

**Toastbrig:** “I'll draw up a departure test.”

**Sensei:** “The path is open. You don't need to pass his test.”

**Unrelated or unclear:**

**Sensei:** “Try a line that closes this conversation. Plain is fine.”

Do not generate a taunt mocking spelling or an unclear answer.

**Borrowed line:** “Heard it. Moving on.”

#### Ask Sensei for help

This is a valid alternative, not a miss. Clear the beat and close the second drawer.

**Wren:** “Sensei, a hand?”

**Sensei:** “Of course. Inspector, the inspection is over. We're leaving.”

**Toastbrig:** “There is a form for—”

**Narrator:** Sensei points at the open path.

**Sensei, to Wren:** “Together?”

**Wren:** “Together.”

Then proceed to the final beat. Help remains available there too.

### `c2_e2_b3` — second typed answer: no permission required

**Narrator (setup):** Only one drawer remains open. The path winds towards a building full of painted windows and extremely fancy curtains.

**Narrator:** Toastbrig lifts a little stamp.

**Toastbrig:** “Go on, then. Run away. I'll stamp you SCARED.”

**Narrator:** Wren isn't running. She is quite ready to leave.

**Prompt:** **Write a last line, or just take the path.**

**Input placeholder:** `An ending, not an argument`

**Buttons:** **Say it and go** / **Keep walking** / **Borrow a line** / **Ask Sensei for help**

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
- “I'm leaving because we need the bell, not because of you.”
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

**Narrator:** The thumb now says **SCARED**.

**Toastbrig:** “That's confidential.”

**Sensei (best):** “He can choose a stamp. You can choose the path.”

**Sensei (okay):** “You left. That's the useful part. 'I'm going' is enough next time.”

Now show **Follow the path**. This is an action continuation, not another graded challenge. No second comeback is required.

#### Keep walking outcome

**Narrator:** Wren takes the path without answering.

**Toastbrig (calling after Wren):** “You forgot your—”

**Narrator:** He looks at his empty hand.

**Toastbrig:** “—nothing.”

**Narrator:** The last drawer shuts. His stamp lands on the complaints sign, which now reads:

**Display — stamped complaints sign:**

> COMPLAINTS ABOUT THE INSPECTION
>
> SCARED

**Sensei:** “You'd already answered. Walking was enough.”

Clear the beat. Do not require a further departure button beyond normal narration advance.

#### Ask Sensei for help outcome

**Wren:** “Walk with me?”

**Sensei:** “Yes.”

**Narrator:** {pet} takes one side. Echo takes the other.

**Narrator:** The group heads along the path. The last drawer shuts behind them.

**Toastbrig:** “I haven't finished the—”

**Narrator:** The bridge bird squeaks over the rest.

**Sensei:** “You can ask for company whenever you need it.”

Clear the beat. Give the same reward as the other successful routes.

#### Retry packages

**Proving bravery:**

**Narrator:** Toastbrig picks up his pencil.

**Toastbrig:** “A bravery examination. Splendid. Section one: boots.”

**Sensei:** “You don't need his bravery mark. The path is open.”

**Staying for approval:**

**Narrator:** Toastbrig pulls his chair closer to the desk.

**Sensei:** “That lets him set your leaving time. Try choosing it yourself.”

**Threat or personal attack:**

**Sensei:** “You can leave without threatening him or attacking something personal.”

**Unclear:**

**Sensei:** “Try a goodbye, a boundary, or the walking button.”

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

### `c2_end_04` — Sensei

**Sensei:** “He didn't change his opinion. You still crossed the bridge.”

### `c2_end_05` — hook

**Narrator:** The building ahead had an enormous velvet door and a sign in gold letters:

**Display — gallery sign:**

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

### Reward screen

**Heading:** **Bridge crossed. Boots unchanged.**

- +40 coins.
- Sticker: **Toastbrig — Opinion Still Pending**. Art: Toastbrig inspecting his stamped thumb while a bird perches on his kettle.
- Trophy: **Same Answer**. Caption: “New demand. Your choice stayed yours.”
- Story inventory: **Route to the Comedy Gallery**.
- Map: bridge route unlocked for free return travel. Never make the player repeat a completed encounter merely to cross the map.

**Buttons:** **Chapter complete — back to the dojo** / **Replay this chapter**

Until Chapter 3 exists, do not show an active button promising it. The gallery hook is enough.

---

## Implementation handoff and review checklist

### Content and state

- Substitute `{pet}` at render time. Preserve the player's actual pet art and name. Sound-stealing works with any pet form.
- New script IDs deliberately differ from the existing `ch1...` IDs. Decide the migration explicitly when implementing; do not silently award old first-chapter completion to this different sequence. Preserve the original story and progress as recoverable data.
- Proposed chapter IDs: `gloomwood_v2_c1` and `gloomwood_v2_c2`. Do not overwrite the old story pack as part of importing this review document.
- Each choice row has its own outcome; multiple `best` answers are intentional. Map document `okish` to the existing option-quality value `ok` where the pack requires it, and map the typed grader's `okish` verdict consistently. Do not accidentally interpret either spelling as failure.
- Branch-specific Wren lines in successful outcomes are fixed continuation dialogue, not additional questions to grade.
- Opening screens introduce Wren, {pet}, and Sensei before the first challenge. Do not skip these introductions on a first play. Unseen speakers are labelled by source (**Voice in the bush**, **Troll at the bridge**) until their names appear in the story; the parenthetical script names are implementation metadata, not visible nameplates. Once the badge/sign supplies a name, use **Echo** or **Toastbrig** consistently.
- Narrator, character speech, and Display blocks are distinct UI types, even when they occur in the same beat. No unlabelled quotation should be rendered as speech. Sensei does not read the Queen's notice; the paper bat reads it and is labelled accordingly.
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
- “Keep walking” and asking Sensei for help clear the final beat with full rewards.
- An `okish` answer advances once. Borrowing is available without an artificial losing streak.
- The typed grader accepts a novel relevant ending, such as “This conversation has reached the end of the bridge.”
- Echo only joins after returning the directions and accepting a boundary. Toastbrig need not reform for Wren to finish.
- Read every line aloud. If a joke needs an explanation to sound funny, shorten it or cut it before adding more coach text.
- In the first minute, the player can identify Wren, her pet, Sensei, the stolen object, what its loss does, and where the group is going. No knowledge of the old draft or dojo lore is required.
- Check each dialogue bubble against its speaker label. In particular, the paper bat reads the notice, the Narrator describes actions, and Sensei gives advice as a present companion. Written signs do not spontaneously talk.

### Art briefs

Keep a consistent ink-and-watercolour storybook style: crooked shapes, twilight blues, warm lanterns, readable expressions. Wren can look curious, cross, or uncertain; never demand a permanently blank face. No school objects, uniforms, playgrounds, or realistic school-bully doubles.

1. **Opening:** Wren and her pet at the village's empty bell stand in blue predawn light; Sensei, an older guide in a long coat with a crooked walking stick, unrolls a map. A paper bat in oversized spectacles reads a royal notice. Closed sunflowers and a sleepy rooster show the morning hasn't arrived. No cake competition or unexplained prior errand.
2. **Echo's clearing:** patchwork imp on a crate, absurd official badge, glowing meow jar, three paper stars on a rickety judge's stand.
3. **Returned meow:** a luminous curl springing towards the pet; imp accidentally seated on a folded stool; flattened toy trumpet.
4. **Portable stage:** tiny stage shedding its wheels while Wren studies a map; pale mushrooms mark a usable path away.
5. **Chapter 1 ending:** imp returns three glowing directions to a signpost; abandoned suitcase beside Mrs. Bramble's luggage sign.
6. **Bridge:** salvage-built troll with kettle helmet at a comically small desk; optional-inspection notice readable in UI text rather than generated lettering.
7. **Boot exchange:** Wren stepping across, one boot squeaking; bird answering; troll's signs folding down.
8. **Complaints desk:** three drawers beneath a portable sign, fence-post pencil, ridiculous oversized stamp; clear open path beside the desk.
9. **Chapter 2 ending:** Wren, pet, and Echo on the winding path; distant troll inspecting a stamped thumb; invitingly strange gallery ahead.

The practical test is whether she wants to see what's around the next bend. The comeback practice should help her get there.
