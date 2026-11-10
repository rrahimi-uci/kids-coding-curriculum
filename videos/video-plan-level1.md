# Level 1 Teaching Video Production Plan

> **Status:** Production-ready scripts and an automated regeneration contract for all 12 Level 1 lessons.
> Each video is designed for children ages 10–11 and is shorter than five minutes.

## 1. Instructional and creative direction

- **Series:** Nova & Pixel's Code Quest
- **Audience:** Children ages 10–11 who are complete beginners
- **Frame:** 16:9, 1920×1080, 24 or 30 fps
- **Narration:** Warm, curious, inclusive, and clear at about 140–145 words per minute; friendly without sounding babyish
- **Visual language:** Bright modern 2D motion graphics, real Scratch or Thonny captures, deterministic code overlays, and a recurring mission map
- **Accessibility:** Open captions, Okabe–Ito palette, high contrast, large readable type, no color-only clues, gentle motion, and no rapid flashing

### Recurring story world

Nova is an inventive ten-year-old coder. Pixel is a palm-sized helper robot who takes instructions very literally. Each week, the pair opens a new door in the Code Quest workshop by learning one idea, testing it, and repairing one friendly bug. Learners are invited to predict before the answer appears.

### Five-part learning rhythm

Every episode follows the same reassuring rhythm: a surprising mission, one plain-language idea, a worked example, a friendly bug hunt, and a direct handoff to the lesson activity. The video launches hands-on learning; it does not replace it.

### Production rules

- Keep the final runtime at or below 5:00; the planned episodes are 4:30.
- Record at roughly 140–145 words per minute, with pauses after questions.
- Caption every spoken word. Never use color as the only clue.
- Render code, Scratch blocks, filenames, and UI labels as deterministic overlays—not inside generated artwork.
- Use the Okabe–Ito color palette, high contrast, readable type, gentle motion, and no rapid flashes.
- Show only nicknames and invented data. Never ask a child for a real name, address, school, password, or contact information.
- End with an age-appropriate practice prompt and normalize debugging as part of coding.
- Disclose synthetic narration in the end card and video description.

## 2. Curriculum audit summary

The source review covered the Level 1 syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief and starter, and the final project materials. The sequence moves from Scratch (weeks 1–6) to Python and Thonny (weeks 7–12), while repeatedly connecting algorithms, events, loops, choices, variables, decomposition, testing, and reflection.

The videos preserve the course's strongest teaching choices: concrete analogies before vocabulary; one-change-at-a-time debugging; Grade 4–5 mathematics; visible, testable outcomes; creativity alongside correctness; safe sharing; and a final interactive art project. Each script below names the misconception it prevents and points learners back to the exact lesson activity.

## 3. Episode scripts and storyboards

## Week 1: Robots Need Exact Instructions

- **Driving question:** How can we turn an idea into steps a computer can follow?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** algorithm, sequence, sprite, stage, block, green flag
- **Misconception to prevent:** Computers can guess the missing parts of a vague instruction or quietly fix steps placed in the wrong order.
- **Digital citizenship:** Use a nickname in projects and never type a real full name, school, address, password, or contact information.

### Instructional objectives

- Explain that an algorithm is an ordered set of exact instructions.
- Identify the Scratch stage, sprite, blocks palette, scripts area, and green flag.
- Predict how changing the order of blocks changes what a sprite does.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Nova needs Pixel to deliver a glowing key to the workshop door. ‘Take it over there,’ says Nova. Pixel spins, puts the key on a chair, and proudly beeps. Oh! Pixel did exactly what it heard—but Nova's instruction was not exact. Can you give Pixel steps it cannot misunderstand? | Workshop map with Nova, Pixel, a chair, and a locked door. Pixel follows a dotted path to the wrong place; freeze before the reveal. **On screen:** MISSION: Deliver the key; Pause: What exact steps would you give? | Use a three-second prediction pause and a soft comic boing, not a failure buzzer. |
| 0:25–1:20 | **Explain algorithm and sequence** | A computer is like Pixel: fast and helpful, but not a mind reader. An algorithm is a list of exact steps for a job. Sequence means the order of those steps. Try this algorithm: move forward three floor squares, turn right, move forward two, place the key beside the blue door. If we place the key before we move, the same steps make a different result. Order matters. | Numbered floor tiles animate one at a time. Then cards 1–4 are shuffled so ‘place key’ comes first, producing a visible different result. **On screen:** Algorithm = exact steps; Sequence = the order; Same steps + new order = new result | Give every numbered card both a symbol and a label; do not rely on blue alone to identify the door. |
| 1:20–2:25 | **Connect to Scratch** | Scratch lets us build algorithms with blocks. The stage is where the action happens. A sprite is a character or object. We find commands in the blocks palette and snap them together in the scripts area. The green flag starts our algorithm. Watch: when green flag clicked, say ‘Hello, coder!’ for two seconds, move ten steps. Read the stack from top to bottom. What will the cat do first? Yes—speak, then move. | Clean labeled Scratch capture. Camera moves from stage to sprite list, blocks palette, and scripts area. Overlay a three-block stack and animate a bright outline down it. **On screen:** Stage = action area; Sprite = character or object; Read blocks top → bottom | Use an authentic current Scratch interface capture. Render labels as overlays outside the capture. |
| 2:25–3:35 | **Friendly bug hunt** | Pixel built a jump greeting, but it looks odd. The blocks say: move up, wait, say ‘Watch me jump!’, then move down. Pixel wanted the message before the jump. Our detective steps are: say what we expected, notice what actually happened, read one step at a time, then change one thing and test. Which blocks should trade places? Pause and point. Right: move the say block above the motion. A bug is a clue, not a reason to quit. | Split screen: expected mini-storyboard versus actual animation. A magnifying glass follows each block. Two blocks visibly swap and the corrected stack runs. **On screen:** Expected?; Actual?; Read one step at a time; Change one thing. Test. | Leave four seconds for prediction. Use check marks only after the rerun proves the fix. |
| 3:35–4:30 | **Safety, recap, and handoff** | You unlocked the first door! Remember: exact steps make an algorithm, their order is the sequence, and Scratch runs a stack from top to bottom. When you name your project or sprite, use a fun nickname—not your real full name, school, address, password, or contact details. Now open Hello Cat. Make a greeting, press the green flag, then swap two blocks. Be ready to explain why the result changed. Code, test, notice, improve! | Mission map door opens. Three recap icons appear, followed by a safe profile card labeled ‘StarCoder’ and crossed-out examples of private data categories. **On screen:** Exact steps • Right order • Test; Use a nickname; NEXT: Hello Cat | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Open the Week 1 Hello Cat activity. Build a greeting, then swap two blocks and explain exactly what changed.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week01.tex`
- `1-introduction/teaching-material/workbook/week01.tex`
- `1-introduction/teaching-material/homework/week01.tex`
- `1-introduction/exercises/week01/ex-hello-cat/README.md`
- `1-introduction/exercises/week01/ex-mixed-up-jump/README.md`

## Week 2: Loop-de-Loop

- **Driving question:** How can one short instruction make a repeated pattern?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** loop, repeat, forever, iteration, turn angle, Pen
- **Misconception to prevent:** Repeat and forever are interchangeable, or every polygon can use the same turn angle.
- **Digital citizenship:** Follow the 20-20-20 eye-break routine and make animation motion comfortable to watch.

### Instructional objectives

- Use repeat for a known number of repetitions and forever for ongoing behavior.
- Explain how repeating move-and-turn steps draws a regular polygon.
- Debug a shape by checking the repeat count and turn angle.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | The next workshop door needs a four-sided light pattern. Nova starts writing: move, turn, move, turn, move, turn… Pixel's paper rolls across the floor. There must be a shorter way! What instruction could tell Pixel to reuse the same two steps four times? | A comically long paper strip grows while a square outline waits unlit. Fold repeated move-turn cards into one loop card. **On screen:** MISSION: Light four sides; How can we avoid repeated blocks? | Pause for three seconds as the repeated pairs highlight together. |
| 0:25–1:20 | **Explain loops** | A loop repeats instructions. Use repeat when you know how many times: repeat four, clap once. One trip through a loop is an iteration. Use forever when an action should continue until the program stops, like a character gently blinking. Repeat four finishes after four iterations. Forever does not finish by itself. Which would you choose for the four sides? Repeat four—because we know the number. | Two labeled tracks: repeat 4 reaches a finish flag; forever circles a calm blinking sprite until a stop button is pressed. **On screen:** Loop = repeat instructions; repeat 4 → stops; forever → continues | Use shape and labels as well as color to distinguish the two tracks. |
| 1:20–2:25 | **Build a polygon** | With Scratch's Pen, Pixel can draw while moving. A square has four equal sides, so repeat four: move sixty steps, turn ninety degrees. Four quarter-turns bring Pixel all the way around. For another regular shape, use the course rule: turn equals three hundred sixty divided by the number of sides. A triangle uses three turns of one hundred twenty degrees. Say it with me: sides tell us repeats; three hundred sixty divided by sides tells us the turn. | Scratch Pen-down stack draws a square. A full-turn ring marked 360 splits first into four 90-degree pieces, then three 120-degree pieces. **On screen:** repeats = number of sides; turn = 360 ÷ sides; Square: repeat 4, turn 90° | Explain the rule visually; do not introduce algebraic notation beyond the course wording. |
| 2:25–3:35 | **Friendly bug hunt** | Pixel wants a pentagon, but the drawing leaves a gap. Expected: five sides that close. Actual: five sides that almost close. The stack repeats five times, so the side count is right. Now check the turn: Pixel used sixty degrees. A pentagon needs three hundred sixty divided by five, which is seventy-two degrees. Pause: which one thing should we change? Change sixty to seventy-two, test again, and the path closes. The gap was useful evidence. | Open pentagon beside a closed outline. A detective checklist confirms repeat 5, circles turn 60, and replaces it with 72 before rerunning. **On screen:** Expected: closed shape; Check repeats, then turn; 360 ÷ 5 = 72° | Hold the faulty result long enough to inspect; celebrate the test, not speed. |
| 3:35–4:30 | **Well-being, recap, and handoff** | Door two glows! Loops make code shorter. Repeat is for a known number; forever continues until stop. For regular polygons, repeat once per side and share a full three-hundred-sixty-degree turn. Before Polygon Party, give your eyes a reset: every twenty minutes, look about twenty feet away for twenty seconds. Then draw a square, try another side count, and debug any gap by checking repeats and the turn. Your pattern laboratory is open! | Door lights with a looping border. A gentle 20-20-20 card shows a window view, then transitions to the Polygon Party task card. **On screen:** repeat • forever • iteration; 20 minutes • 20 feet • 20 seconds; NEXT: Polygon Party | Keep all looped animation slow and stop motion during the eye-break card. Include AI-voice disclosure. |

**Lesson handoff:** Build Polygon Party: repeat equal moves and turns, then change the side count and calculate 360 ÷ sides.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week02.tex`
- `1-introduction/teaching-material/workbook/week02.tex`
- `1-introduction/teaching-material/homework/week02.tex`
- `1-introduction/exercises/week02/ex-polygon-party/README.md`
- `1-introduction/exercises/week02/ex-walking-cat/README.md`

## Week 3: When This Happens…

- **Driving question:** How can a program notice an event and choose what to do?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** event, condition, if, if-else, sensing, forever
- **Misconception to prevent:** An if block keeps checking forever by itself, even when it runs only once.
- **Digital citizenship:** Give kind, specific feedback about the project rather than judging the person who made it.

### Instructional objectives

- Explain that an event starts a script when something happens.
- Use if and if-else to choose actions from a condition.
- Place sensing choices inside a forever loop when they must keep checking.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Nova presses the workshop doorbell. Nothing happens. Pixel says, ‘I checked before you pressed it!’ A useful doorbell must notice the press when it happens. How can our program wait for an event, check a condition, and react at the right time? | Doorbell timeline shows Pixel checking too early, then Nova pressing later. Freeze on the missing connection. **On screen:** MISSION: Make the door react; What should the program notice? | Use a clear timeline arrow and a three-second prediction pause. |
| 0:25–1:20 | **Explain events and conditions** | An event is something that starts action: the green flag is clicked, a key is pressed, or a sprite is clicked. A condition is a yes-or-no question, such as ‘touching the pointer?’ An if block says: if the answer is yes, do this. An if-else block gives two paths: if yes, open the door; else, keep it closed. Only one path runs each time the choice is checked. | Doorbell icons connect to event hats. A large yes/no road fork demonstrates an if-else choice with words and symbols. **On screen:** Event = starts action; Condition = yes/no question; if yes… else… | Show the complete condition inside the Scratch block; narrate its punctuation-free meaning. |
| 1:20–2:25 | **Build a responsive script** | Let's make a ghost giggle when the pointer touches it. Start with the green flag. Inside forever, place: if touching mouse-pointer, say ‘That tickles!’; else, clear the speech. Why forever? The pointer may move later, so the program must ask the touching question again and again. Watch the highlight circle the loop: check, choose, react; check, choose, react. Move away, and the other path runs. | Authentic Scratch block overlay beside a ghost. A pulse travels through forever, condition, yes path, then else path as the pointer moves. **On screen:** forever: keep checking; check → choose → react; Test YES and NO | Keep the pointer motion slow. Use labels YES and NO in addition to path colors. |
| 2:25–3:35 | **Friendly bug hunt** | Pixel's ghost never reacts if Nova moves the pointer after the green flag. Expected: it giggles whenever touched. Actual: it checks once at the start, then stops. Read the stack: green flag, if touching, say. The condition is accurate, but it needs repeated checking. Where should the forever block go? Pause and point. Wrap forever around the if block. Test first with the pointer away, then touching. Now both cases work. | A single scan line passes the script and disappears. Then a forever bracket wraps around the choice and the scan line loops continuously. **On screen:** Bug: checked only once; Fix: keep the choice inside forever; Test both paths | Pause four seconds before wrapping the block; avoid implying forever belongs around every if statement. |
| 3:35–4:30 | **Feedback, recap, and handoff** | The door hears us now! Events start scripts. Conditions ask yes-or-no questions. If and if-else choose a path, and forever can keep a sensing choice awake. When you test a classmate's project, be a kind code detective: say what you noticed and offer one useful idea—‘The ghost reacts when I touch it; maybe make the message stay a little longer.’ Now build Tickle Ghost and prove both the touching and not-touching paths work. | Door opens to two test lanes. A feedback speech bubble transforms from ‘Bad game’ into a specific observation and suggestion. **On screen:** Events start; Conditions choose; Feedback: notice + helpful idea; NEXT: Tickle Ghost | Finish on a test card with two boxes: pointer away and pointer touching. Include AI-voice disclosure. |

**Lesson handoff:** Create Tickle Ghost so touching the pointer triggers a reaction, then test both touching and not-touching cases.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week03.tex`
- `1-introduction/teaching-material/workbook/week03.tex`
- `1-introduction/teaching-material/homework/week03.tex`
- `1-introduction/exercises/week03/ex-tickle-ghost/README.md`
- `1-introduction/exercises/week03/ex-arrow-explorer/README.md`

## Week 4: Keeping Score with Variables

- **Driving question:** How can a program remember a number that changes?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** variable, value, set, change, random, score
- **Misconception to prevent:** Set score to 1 and change score by 1 do the same job, or touching can add points many times before an object resets.
- **Digital citizenship:** Credit creators when remixing and describe what was changed instead of pretending all work is original.

### Instructional objectives

- Describe a variable as a named place that stores a value.
- Distinguish setting a variable from changing it.
- Use random positions and controlled scoring in a simple catch game.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Nova catches three falling stars. Pixel cheers—but the scoreboard still says zero. ‘I watched every catch,’ Pixel says, ‘but I forgot the number!’ Our next door opens at five points. What can a program use to remember a value while it changes? | Three stars land in a basket while a frozen scoreboard stays at zero. A labeled empty memory box appears beside Pixel. **On screen:** MISSION: Remember the score; What can store a changing value? | Count catches aloud with matching visual pips; pause after the question. |
| 0:25–1:20 | **Explain variables** | A variable is a named place where a program stores a value. Imagine a labeled box called score. At the start, set score to zero: replace whatever was there with zero. After one catch, change score by one: take the current value and add one. Set replaces. Change adjusts. If score is three, setting it to one gives one; changing it by one gives four. Which command belongs after a catch? Change by one. | A physical box labeled score swaps cards for set and adds a +1 chip for change. Side-by-side results animate from 3. **On screen:** Variable = named storage; set → replace; change → adjust | Use arrows and operators as well as color; hold the 3→1 and 3→4 comparison. |
| 1:20–2:25 | **Build catch-game logic** | Here is the catch-game plan. When the green flag is clicked, set score to zero. Put the action inside forever. Make the apple fall. If it touches the basket, change score by one, then move the apple to a random position at the top. Random means the program chooses from an allowed range, so the next catch is less predictable. The order matters: count one catch, then reset the apple before checking again. | Flow diagram and matching Scratch stack: reset, loop, fall, sense, score, random reset. A numbered outline follows execution. **On screen:** 1 Reset; 2 Check catch; 3 Add 1; 4 Move apple | Show random x-position as several allowed landing lanes, not as unexplained magic. |
| 2:25–3:35 | **Two-bug investigation** | Pixel finds two clues. First, a new game begins with yesterday's score. Expected zero; actual seven. The green-flag script forgot set score to zero. Second, one apple gives twenty points. The apple stays touching the basket while forever checks very fast. Pause: what should happen immediately after adding one? Move the apple away—to a new top position—before the next check. Change one thing, test, then investigate the next clue. | Detective board shows bug A: stale score and bug B: rapidly spinning counter. Repairs are applied and tested separately. **On screen:** Bug A: no reset; Bug B: counts one catch many times; Fix one clue, then test | Do not glamorize the runaway score with frantic flashing; keep counter motion readable and brief. |
| 3:35–4:30 | **Credit, recap, and handoff** | Five points—the door opens! Variables store values. Set replaces a value; change adjusts it. Random choices make games less predictable, and careful order prevents extra points. If you remix someone's Scratch idea, give credit: ‘Based on MayaCoder's catch game; I added random stars and a timer.’ That is honest and helpful. Now build Apple Catch. Start at zero, count exactly one point per catch, and test a brand-new game twice. | Score reaches five. A simple credit card shows creator nickname, original idea, and learner's change, then the Apple Catch challenge appears. **On screen:** Store • Set • Change; Credit the creator + name your change; NEXT: Apple Catch | Use invented nicknames only. Include AI-voice disclosure on the held end card. |

**Lesson handoff:** Build Apple Catch, reset score at the start, add one per catch, and move the apple before another point can be counted.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week04.tex`
- `1-introduction/teaching-material/workbook/week04.tex`
- `1-introduction/teaching-material/homework/week04.tex`
- `1-introduction/exercises/week04/ex-apple-catch/README.md`
- `1-introduction/exercises/week04/ex-pop-balloon/README.md`

## Week 5: Messages and My Blocks

- **Driving question:** How can we organize a big project into small jobs that work together?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** decomposition, My Block, input, broadcast, receive, message
- **Misconception to prevent:** A broadcast reaches only the selected sprite, or message names that look similar will automatically match.
- **Digital citizenship:** Make projects readable with text or symbols as well as color, so more people can understand them.

### Instructional objectives

- Break a repeated job into a named My Block with an input.
- Use broadcast and when-I-receive messages to coordinate sprites.
- Debug communication by checking exact message names and event order.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | The workshop stage has three performers. Nova tries to control every move in one giant stack. The blocks wobble higher than Pixel! One performer starts late, another never moves. Could we give each small job a name and send one clear message when showtime begins? | A towering Scratch stack bends while three performers wait. It separates into neat labeled cards connected by one message envelope. **On screen:** MISSION: Organize the show; Small jobs + clear messages | Use gentle squash-and-stretch on the block tower; pause for learner ideas. |
| 0:25–1:20 | **Explain decomposition and My Blocks** | Decomposition means splitting a big problem into smaller jobs. In Scratch, My Blocks lets us name a job we want to reuse. Define draw shape with an input called sides. Inside the definition: repeat sides, move, and turn. Then the main script can call draw shape four or draw shape six. The input is a value the block receives, so one useful recipe can make different shapes. | Big ‘art show’ puzzle splits into shape, movement, and speech pieces. A My Block definition receives 4, then 6, and draws two labeled results. **On screen:** Decomposition = smaller jobs; My Block = named reusable job; Input = value the job receives | Show the course's block structure accurately; keep the polygon turn formula visible as an overlay when used. |
| 1:20–2:25 | **Coordinate with messages** | A broadcast is like a stage manager's announcement. Nova's main script broadcasts showtime. Every sprite with a ‘when I receive showtime’ hat can respond: the star spins, the cat speaks, the backdrop changes. Broadcasting does not force every sprite to do the same action. It gives interested scripts the same starting signal. Message names must match exactly, including spaces. One clear announcement can coordinate many small jobs. | Stage manager sends a SHOWTIME envelope outward. Three separate receiver scripts light up and perform different actions in parallel. **On screen:** broadcast [showtime]; when I receive [showtime]; One signal, different jobs | Use radio-wave symbols plus labels; avoid implying the message contains private chat content. |
| 2:25–3:35 | **Friendly bug hunt** | Pixel's star never spins. Expected: all three performers start. Actual: only two respond. Read the sender: broadcast ‘show time’—two words. Read the star's receiver: when I receive ‘showtime’—one word. Scratch treats those as different messages. Pause: which name should change? Either spelling works, but sender and receiver must use the exact same message. Choose one from the dropdown, test again, and the star joins the show. | Two message tags align under a magnifier; a visible space separates SHOW TIME. The receiver selects the same dropdown item and a test pulse reaches all three sprites. **On screen:** Expected: 3 performers; Actual: 2 performers; Message names must match exactly | Do not fix by retyping if the dropdown can prevent a mismatch; model the safer action. |
| 3:35–4:30 | **Accessibility, recap, and handoff** | Showtime! Decompose a big project into smaller jobs. Put repeated jobs in named My Blocks, use inputs to vary them, and broadcast exact messages to coordinate sprites. Make your show understandable for more people: if red means stop and green means go, add the words or clear symbols too. Color should never be the only clue. Now build Shape Machine, then send one showtime message and test every receiver. | Door becomes a stage curtain. A color-only stop/go display gains STOP/GO labels and shapes, followed by a two-part activity card. **On screen:** Small jobs • Reusable blocks • Exact messages; Use words or symbols with color; NEXT: Shape Machine + Show Time | Verify contrast in both light and grayscale previews. Include AI-voice disclosure. |

**Lesson handoff:** Create Shape Machine with a reusable shape block, then coordinate a short show with one exact broadcast message.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week05.tex`
- `1-introduction/teaching-material/workbook/week05.tex`
- `1-introduction/teaching-material/homework/week05.tex`
- `1-introduction/exercises/week05/ex-shape-machine/README.md`
- `1-introduction/exercises/week05/ex-show-time/README.md`

## Week 6: Scratch Detective Checkpoint

- **Driving question:** Can we combine our Scratch ideas and explain how we debug?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** sequence, loop, event, condition, variable, debug
- **Misconception to prevent:** Debugging means guessing many changes at once or that a working project needs no explanation.
- **Digital citizenship:** Design fair, kind projects and test whether instructions, controls, and feedback make sense to another learner.

### Instructional objectives

- Connect sequence, loops, events, choices, variables, and messages in one project.
- Apply the four-step debugging routine and explain evidence for a fix.
- Relate familiar Scratch blocks to upcoming Python ideas.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Checkpoint hook** | Six workshop doors glow behind Nova and Pixel. The checkpoint console mixes every symbol we have found. A flag, a loop, a question, a score box, and a message—can you name what each one does? Today, you are the lead code detective. | Mission map zooms across six doors. Five familiar icons land on a detective board as unlabeled evidence cards. **On screen:** CHECKPOINT MISSION; Name it • Use it • Explain it | Pause briefly on each icon so a teacher can solicit answers. |
| 0:25–1:20 | **Retrieve six big ideas** | Sequence is the order of steps. A loop repeats steps. An event starts action. A condition chooses from a yes-or-no question. A variable remembers a value. A broadcast coordinates scripts with a message. In a catch game, the green flag starts a sequence, forever repeats movement, touching is a condition, score is a variable, and a game-over broadcast can start an ending. The ideas work as a team. | Each icon receives its label and then docks onto a single catch-game flow diagram at the exact place it contributes. **On screen:** Sequence • Loop • Event; Condition • Variable • Message; Ideas work together | Use consistent symbols from earlier episodes to support retrieval, not new decorative icons. |
| 1:20–2:25 | **Model debugging evidence** | A code detective does not mash blocks until something works. Use four moves. One: say the expected result. Two: describe the actual result. Three: read one step at a time and find the first difference. Four: change one thing and test. Pixel's hexagon has six repeats but turns ninety degrees. The first difference appears at the turn. A six-sided regular shape needs three hundred sixty divided by six: sixty degrees. Change ninety to sixty, then rerun. | Four numbered detective lenses reveal a wonky hexagon, its stack, the first wrong turn, and a controlled one-value repair. **On screen:** 1 Expected; 2 Actual; 3 First difference; 4 Change one thing + test | Keep the math helper visible: 360 ÷ 6 = 60. Avoid presenting the fix before evidence. |
| 2:25–3:35 | **Bridge from Scratch to Python** | Soon, our blocks will become typed Python. The ideas stay with us. A Scratch say block is like Python's print. A repeat block becomes a for loop. A variable still has a name and value. An if block is still a choice. A My Block is like a function. The spelling will matter more, but you already know how to plan, predict, test, and debug. Pause: which Python idea do you predict will replace broadcast? There can be several designs; the important skill is coordinating smaller parts. | A bridge pairs Scratch blocks with simple, large Python snippets: print, for, variable assignment, if, and def. Broadcast remains a question card, not a false one-to-one mapping. **On screen:** Blocks change. Ideas continue.; say → print; repeat → for; My Block → function | Do not imply every Scratch block has one exact Python equivalent. Keep code as deterministic overlays. |
| 3:35–4:30 | **Fair design, recap, and handoff** | Checkpoint cleared! Strong coders can build and explain. Strong detectives use evidence and change one thing at a time. Strong designers make projects fair and kind: controls are clear, success is possible, and feedback helps instead of teasing. Choose a relay bug today. Before touching the blocks, tell a partner the expected and actual result. After one fix, show the test that proved it. Then create your checkpoint project using at least three big ideas. | Checkpoint badges read Builder, Detective, Explainer. A fairness gauge checks clear controls, possible challenge, and kind feedback. **On screen:** Build • Debug • Explain; Fair controls + kind feedback; NEXT: Relay challenge | End with a five-second teacher pause card and AI-voice disclosure. |

**Lesson handoff:** Choose a Week 6 relay challenge, use the detective routine, and explain one fix before beginning the checkpoint project.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week06.tex`
- `1-introduction/teaching-material/workbook/week06.tex`
- `1-introduction/teaching-material/homework/week06.tex`
- `1-introduction/exercises/week06/ex-relay-broken-catch/README.md`
- `1-introduction/exercises/week06/ex-relay-silent-party/README.md`

## Week 7: Hello, Python!

- **Driving question:** How do typed instructions make words and turtle drawings appear?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** Python, Editor, Shell, Run, comment, turtle
- **Misconception to prevent:** Python guesses misspellings or ignores punctuation and capitalization the way a person might.
- **Digital citizenship:** Use a nickname in filenames and program output; do not put private information in code or screenshots.

### Instructional objectives

- Identify Thonny's Editor, Shell, Run button, and turtle window.
- Use print, comments, and basic turtle movement in a saved Python file.
- Read the final error message and line number to repair a simple typo.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **New-language hook** | A new door has no Scratch blocks—only a blinking text cursor. Nova types ‘Hello, Pixel!’ and presses Run. The words appear, and Pixel's screen lights up. We have crossed into Python, where we write instructions with text. The ideas are familiar; the way we spell them is new. | Blocks transform into carefully typeset text. A cursor blinks in a simplified Thonny Editor and output appears in the Shell. **On screen:** NEW MISSION: Python; Familiar ideas, typed instructions | Use a real Thonny capture after the stylized transition; keep code crisp and selectable in source assets. |
| 0:25–1:20 | **Tour Thonny** | Thonny is our Python workshop. We write and save a program in the Editor. The green Run button asks Python to follow the file. The Shell shows text output and useful error messages. Turtle programs also open a drawing window. Before running, save with a clear nickname-based filename, such as star_coder_square.py—not your full name. Editor writes, Run starts, Shell reports, turtle draws. | Real Thonny interface with four large callouts, followed by a safe filename comparison using category labels rather than real identities. **On screen:** Editor: write; Run: start; Shell: output + errors; Turtle window: drawings | Verify UI labels against the supported Thonny version. Never display a real home-folder username. |
| 1:20–2:25 | **Write first Python and turtle commands** | Type print, open parenthesis, quotation mark, Hello coder, matching quotation mark, close parenthesis. Print shows text in the Shell. A line beginning with a hash mark is a comment: a note for people that Python skips. For drawing, import turtle, then tell the turtle forward sixty and left ninety. Forward moves in steps; left turns in degrees. Run the file and watch each exact instruction happen in order. | Large syntax-highlighted overlays appear token by token, then a turtle moves 60 and turns left 90 with labeled distance and angle arcs. **On screen:** print("Hello, coder!"); # A comment for people; turtle.forward(60); turtle.left(90) | Code overlays must be exact. Read punctuation naturally but point to matching marks. |
| 2:25–3:35 | **Error-message bug hunt** | Pixel typed turtle.forword with one letter missing. Expected: a line. Actual: the turtle window stops and red text appears. Do not panic or read every line first. Look near the bottom for the line number and the final message. It points to line four and says turtle has no attribute forword. Compare the command with forward. Pause: what single spelling change should we test? Add the missing a, run again, and the line appears. Errors are directions, not danger. | Sanitized Thonny error capture zooms to the final line and source line number. A letter tile slides into forword to form forward; rerun succeeds. **On screen:** 1 Find the line number; 2 Read the last message; 3 Change one thing; 4 Run again | Use a recreated error with no local paths or usernames. Keep red as conventional text but add icons and labels. |
| 3:35–4:30 | **Safety, recap, and handoff** | Python door unlocked! In Thonny, write in the Editor, save, press Run, and read the Shell. Print shows words; comments help people; turtle moves and turns. Spelling, capitalization, quotes, and parentheses matter. Keep filenames and screenshots private-safe—use nicknames and invented words, never a real full name, school, address, password, or contact details. Now run Hello Python, then draw First Square. If it stops, let the last error message be your detective clue. | Four-tool recap orbit around the open door, then a safe file card and two-step activity handoff. **On screen:** Write • Save • Run • Read; Safe filename: star_coder_square.py; NEXT: Hello Python + First Square | Hold the final code challenge for five seconds and include AI-voice disclosure. |

**Lesson handoff:** Open Thonny, run Hello Python, save with a safe filename, then draw and debug the First Square activity.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week07.tex`
- `1-introduction/teaching-material/workbook/week07.tex`
- `1-introduction/teaching-material/homework/week07.tex`
- `1-introduction/exercises/week07/ex-hello-python/README.md`
- `1-introduction/exercises/week07/ex-first-square/README.md`
- `1-introduction/exercises/week07/ex-typo-hunt/README.md`

## Week 8: Loops in Python

- **Driving question:** How does indentation tell Python which steps belong inside a loop?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** for loop, range, colon, indentation, iteration, nested loop
- **Misconception to prevent:** Indented spacing is decoration, or range(4) repeats five times because counting includes 0 through 4.
- **Digital citizenship:** Ask for help with a useful sentence that includes the goal, actual result, and what has already been tried.

### Instructional objectives

- Write a for loop with range, a colon, and consistent four-space indentation.
- Use a loop to draw regular polygons with turtle.
- Recognize off-by-one and indentation bugs from visible results and errors.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Pixel types forward and left four times to draw a square. ‘This feels familiar,’ Nova says. We used a Scratch repeat block for this! Python can loop too—but instead of a block's colored border, spaces show which instructions repeat. Can we shrink eight lines into three? | Eight repeated Python lines fold into a for-loop card. Four visible space markers form a guide rail under the loop header. **On screen:** MISSION: Make repetition shorter; In Python, spaces can show a group | Use visible dot glyphs only as a teaching overlay; clarify learners type spaces, not dots. |
| 0:25–1:20 | **Explain for, range, colon, and indentation** | Read this header: for i in range four, colon. It means repeat the indented group four times. The colon announces that a group follows. Each line inside begins with the same four spaces. Python calls one trip an iteration. Range four gives four iterations: zero, one, two, three—not four as an extra turn. The loop variable i keeps track, even when our drawing does not need to display it. | Code header enlarges in parts. A four-seat iteration train is labeled 0, 1, 2, 3; four-space guides align two body lines. **On screen:** for i in range(4):; colon → a group follows; 4 spaces → inside the loop; range(4) → 4 iterations | Render exact monospaced code and show indentation guides without tabs. |
| 1:20–2:25 | **Draw polygons and preview nesting** | For a square, place turtle forward sixty and turtle left ninety inside range four. The same polygon rule returns: repeats equal sides; turn equals three hundred sixty divided by sides. A triangle repeats three and turns one hundred twenty. We can even place one loop inside another—a nested loop—to repeat a whole square while turning between copies. Think of a small music pattern repeated inside a larger dance pattern. | Square code executes with four highlighted iterations, then values transform to a triangle. A light preview shows a square-flower with inner and outer loop brackets. **On screen:** repeats = sides; turn = 360 ÷ sides; Nested loop = a loop inside a loop | Treat nesting as a preview, not a mastery demand. Use brackets and labels for each loop level. |
| 2:25–3:35 | **Two-clue bug hunt** | Pixel's first square has only three sides. The code says range three. That is an off-by-one bug: the repeat count is one away from what we need. Change it to four and test. Next, Python points to an indented line. One turtle command has two spaces while the other has four. Python uses indentation as structure, so line them up with four spaces. Pause before each repair: what evidence tells us which one thing to change? | An open three-sided shape links to range(3), then a Thonny indentation error links to uneven space guides. Repairs are tested separately. **On screen:** Clue 1: wrong repeat count; Clue 2: uneven indentation; Use evidence. Fix one thing. Test. | Show authentic error wording without private file paths; provide four seconds for each prediction. |
| 3:35–4:30 | **Help-seeking, recap, and handoff** | Python loops are ready! A for loop repeats the indented group. Range controls how many iterations, the colon starts the group, and matching spaces show what belongs inside. If you need help, give a useful report: ‘I expected a square, I got three sides, and I checked the turn.’ That helps a partner reason with you. Now build Loop Square, then change the side count and angle for Polygon Party. Predict the shape before you press Run. | Loop parts snap into a complete card. A weak ‘It doesn't work’ bubble expands into expected, actual, and tried fields, then the activity card appears. **On screen:** Expected + Actual + Tried; Predict before Run; NEXT: Loop Square + Polygon Party | End on code with visible indentation guides and AI-voice disclosure. |

**Lesson handoff:** Build Loop Square, then adapt the repeat count and turn angle for Polygon Party in Python.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week08.tex`
- `1-introduction/teaching-material/workbook/week08.tex`
- `1-introduction/teaching-material/homework/week08.tex`
- `1-introduction/exercises/week08/ex-loop-square/README.md`
- `1-introduction/exercises/week08/ex-polygon-party/README.md`
- `1-introduction/exercises/week08/hw-loop-fixer/README.md`

## Week 9: Variables, Input, and Choices

- **Driving question:** How can a Python program ask, remember, and choose?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** variable, input, string, int, if, elif, else
- **Misconception to prevent:** Input automatically becomes a number, or Python checks every branch after an earlier condition is already true.
- **Digital citizenship:** Programs for this course should ask only playful, invented questions—not names, birthdays, addresses, schools, passwords, or contact details.

### Instructional objectives

- Store input in variables and convert number text with int when needed.
- Use if, elif, and else as an ordered set of choices.
- Test normal and boundary inputs while protecting private information.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | The next door asks, ‘Choose a portal size: 40, 80, or 120.’ Nova types 80. Pixel stores the answer—but then tries to add ten and gets stuck. The input looked like a number. Why does Python see it as text, and how can our program choose the right portal? | A portal console accepts 80, which lands on a card marked text. A plus-ten gear cannot connect until a converter appears. **On screen:** MISSION: Ask, remember, choose; Input begins as text | Pause before revealing the text label; represent data type with words and shape, not color alone. |
| 0:25–1:20 | **Explain variables, input, and conversion** | A Python variable is a name connected to a value. This line asks a question and stores the answer: color equals input, open parenthesis, a safe playful question, close parenthesis. Input returns a string, which means text—even if the learner typed digits. When we need number math or comparisons, int can convert suitable digit text into a whole number. Size equals int of input. First ask, then convert, then use. | Variable name tags connect to text cards. Exact code overlays animate through ask → store text → int converter → store whole number. **On screen:** color = input("Pick a color: "); input → text; size = int(input("Pick 40, 80, or 120: ")) | Use exact nested parentheses and a simple whole-number explanation; do not introduce floats. |
| 1:20–2:25 | **Build ordered choices** | An if-elif-else chain is an ordered set of doors. Python checks the if condition first. If it is true, that branch runs and the rest are skipped. Otherwise, Python tries elif. If no listed condition is true, else provides a fallback. For size: if size equals 40, draw small; elif size equals 80, draw medium; else, draw the large or fallback choice. The first true branch wins. | Three physical doors align top to bottom. A token tests each condition and stops at the first true branch; exact code sits beside the animation. **On screen:** if → first check; elif → another check; else → fallback; First true branch wins | Distinguish assignment = from comparison == with a close-up callout. |
| 2:25–3:35 | **Input bug hunt and testing** | Pixel asks for a star count, then compares the answer with the number five. Expected: typing 5 draws five stars. Actual: the comparison does not match, because input produced the text ‘5’, not the number 5. Pause: where should conversion happen? Wrap the input with int when storing count. Now test 1, 5, and a value between branches. Also test an unexpected but safe value. A helpful else message makes the program easier to use. | Text card ‘5’ and number tile 5 fail to match, then pass through int. A compact test table fills Expected and Actual rows for several safe values. **On screen:** Text "5" ≠ number 5; Convert when number behavior is needed; Test more than one input | Do not claim int handles every input safely; frame non-digit handling as later learning. |
| 3:35–4:30 | **Privacy, recap, and handoff** | Portal opened! Input asks, variables remember, int converts digit text when number behavior is needed, and if-elif-else chooses the first true path. Ask only playful, invented questions in this course: favorite imaginary creature, safe color choice, or number of stars. Never ask for a real name, birthday, address, school, password, email, or phone number. Now build Color Choice and Size It. Try at least three answers and make the fallback helpful. | Safe-question cards pass through a shield; private-data category cards stop outside. The two activity cards slide into the workshop. **On screen:** Ask • Store • Convert • Choose; Only playful, invented input; NEXT: Color Choice + Size It | Use category names only, no examples that resemble real personal data. Include AI-voice disclosure. |

**Lesson handoff:** Build Color Choice, then Size It; test more than one answer and include a helpful else path.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week09.tex`
- `1-introduction/teaching-material/workbook/week09.tex`
- `1-introduction/teaching-material/homework/week09.tex`
- `1-introduction/exercises/week09/ex-color-choice/README.md`
- `1-introduction/exercises/week09/ex-size-it/README.md`

## Week 10: Random Art and Our Own Commands

- **Driving question:** How can functions and randomness turn one idea into many artworks?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** function, define, call, parameter, random, randint
- **Misconception to prevent:** Defining a function makes it run immediately, or random means the program can choose anything without limits.
- **Digital citizenship:** Use only self-created or credited assets and keep random choices within comfortable, readable visual limits.

### Instructional objectives

- Define and call a function with a parameter.
- Use random choice and randint within clear limits.
- Plan a Level 1 art-show project by combining reusable parts.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Creative mission hook** | The workshop gallery needs a hundred flowers, but no two should look exactly alike. Nova could copy the same drawing code again and again. Pixel suggests a better invention: teach Python one flower-making command, then call it with different sizes and random colors. Can one recipe create a whole garden? | One flower multiplies into a varied garden. Repeated code sheets fold into a single recipe card with adjustable dials. **On screen:** MISSION: One recipe, many artworks; Reusable + adjustable + surprising | Use calm variation, avoiding rapidly cycling colors. Pause on the recipe metaphor. |
| 0:25–1:20 | **Explain functions and parameters** | A function is a named set of instructions. We define flower with a parameter called size. The indented body draws using that size. Defining teaches Python the recipe; it does not serve the dish yet. To run it, call flower open parenthesis sixty close parenthesis. The value sixty travels into the size parameter. Define once, call many times. Different arguments can make small, medium, and large flowers from one tested recipe. | Exact def code builds a recipe machine. Calls with 30, 60, and 90 feed labeled values into the size slot and produce three flowers. **On screen:** def → define the recipe; parameter → input slot; flower(60) → call the function | Keep function body code aligned with four spaces and distinguish parameter from the supplied argument in plain language. |
| 1:20–2:25 | **Add bounded randomness** | Randomness lets Python choose from limits we provide. Random choice can select one item from a safe list of readable colors. Random randint ten comma eighty can choose a whole number from ten through eighty for a size or position. Random does not mean ‘anything in the universe.’ We design the allowed choices. A loop can call our flower function several times with new choices, making a garden that changes each run while following our rules. | A choice wheel contains four named accessible colors. A number gate visibly spans 10 through 80. Both feed the flower function inside a loop. **On screen:** random.choice(list); random.randint(10, 80); Random choices stay inside our limits | Use the actual inclusive randint behavior. Avoid color-only identification by labeling swatches. |
| 2:25–3:35 | **Function-call bug hunt** | Pixel's program runs without red errors, but the screen stays blank. Expected: one flower. Actual: nothing drawn. The flower function is defined perfectly, so where is the first difference? Scan below the definition—there is no call. Defining a function prepares it; calling makes it run. Pause: what one line could we add? Flower open parenthesis sixty close parenthesis. Run again. A quiet result can be a debugging clue even when no error message appears. | A complete function sits unused beside a blank turtle window. Detective scan reaches end-of-file, then one call line connects to the function and drawing begins. **On screen:** Defined ≠ called; No red error can still mean a logic bug; Add: flower(60) | Give a four-second prediction pause before showing the call. Keep all code deterministic. |
| 3:35–4:30 | **Project launch and handoff** | The gallery garden blooms! Functions name reusable jobs; parameters make them adjustable; calls run them; and bounded randomness adds variety. Use art you made yourself, or credit the source and follow its permission. For My Interactive Art Show, choose a safe theme, decide what the viewer can input, and sketch one function you will reuse. First build Flower Stamp and Random Art. Then write your project mission in one sentence: ‘My program will…’ | Gallery opens. A project-planning card fills Theme, Safe input, Reusable function, and Random choice; exercise cards lead into the project card. **On screen:** Define • Parameter • Call • Vary; PROJECT: My Interactive Art Show; My program will… | End with a printable planning-card layout and AI-voice disclosure. |

**Lesson handoff:** Build Flower Stamp and Random Art, then choose a theme and sketch the reusable function for My Interactive Art Show.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week10.tex`
- `1-introduction/teaching-material/workbook/week10.tex`
- `1-introduction/teaching-material/homework/week10.tex`
- `1-introduction/exercises/week10/ex-flower-stamp/README.md`
- `1-introduction/exercises/week10/ex-random-art/README.md`
- `1-introduction/project/project-brief.tex`

## Week 11: Project Studio: Build, Run, Check

- **Driving question:** How do we turn a project plan into a working program without getting lost?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** milestone, prototype, test, version, feedback, revision
- **Misconception to prevent:** The fastest way to finish is to type the whole project before running it, or every suggestion must be added.
- **Digital citizenship:** Share only the project window or safe code; remove names and private paths from screenshots, filenames, and demos.

### Instructional objectives

- Build the final project in small, testable milestones.
- Save useful versions and use a build-run-check cycle.
- Conduct peer testing with normal and unusual safe inputs.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Studio hook** | Nova has a brilliant art-show plan—and forty new lines typed without running once. Pixel presses Run. One tiny error hides somewhere in the stack. The studio clock is ticking. Would you rather search forty lines, or test each small piece as you build it? Today we work like project engineers. | Forty code lines form a maze around one tiny bug. The maze transforms into four short, testable stepping stones. **On screen:** STUDIO MISSION; Build small • Test often | Do not imply speed is the goal; frame the clock as choosing a calmer process. |
| 0:25–1:20 | **Plan milestones** | A milestone is a small result we can see and test. For an interactive art show: milestone one opens the turtle window and shows a title. Milestone two asks one safe question and stores the answer. Milestone three draws one complete artwork. Milestone four adds variety and a friendly ending. Start with the minimum that works. Extra sparkle comes after the core path is reliable. Each milestone gives us evidence and a place to recover. | Project road map with four concrete screenshots as checkpoints. A Core path stays solid while optional sparkle branches appear later. **On screen:** M1: opens; M2: asks safely; M3: draws; M4: adds variety; Core first, extras later | Match milestone language to the project guide; keep optional ideas visually secondary. |
| 1:20–2:25 | **Use build-run-check and versions** | Use a three-beat studio rhythm. Build one small change. Run it. Check expected against actual. If they match, save a new version such as art_show_v2.py. If they do not, use the first difference as a clue before adding more. A version is a saved checkpoint, not twelve mystery copies named final-final-really-final. Add a short comment describing the milestone. Then your future self can find a working place. | Build, Run, Check triangle rotates slowly. A tidy version ladder replaces chaotic filenames; each rung has a short milestone note. **On screen:** BUILD → RUN → CHECK; Expected vs actual; Save a clear working version | Use safe generic paths and filenames. Do not show Git as a student requirement. |
| 2:25–3:35 | **Model peer testing** | A tester tries the program without reading your mind. Give the one-sentence mission and let them use it. Ask them to try one normal safe input and one strange-but-safe input, like a very small allowed number or an unexpected color word. Record expected and actual. Then use two stars and a wish: two specific things that work, and one helpful next idea. The creator chooses which feedback fits the mission. Feedback is evidence, not an order or a judgment. | Two learners exchange a project safely. A test table fills Normal and Strange-but-safe rows; two star cards and one wish card cite concrete behaviors. **On screen:** Test: normal + strange-but-safe; 2 specific stars + 1 helpful wish; Creator decides the revision | Model consent before touching another learner's keyboard and kind neutral facial expressions. |
| 3:35–4:30 | **Safe sharing, recap, and handoff** | Studio checkpoint complete! Milestones keep big projects manageable. Build, run, and check one change. Save clear working versions. Test with more than one input, then choose useful feedback. When sharing, show only the project window or safe code. Hide real names, computer usernames, folders, school details, and notifications. Now finish your next milestone, save it as a new version, and trade a two-stars-and-a-wish test. Your goal is not perfect—it is tested, explainable progress. | A privacy curtain crops a screen to the turtle window. The studio checklist marks milestone, version, test, and chosen revision. **On screen:** Small milestone • Working version • Evidence; Share the project, not private details; NEXT: Build + peer test | Use a clearly fake desktop without real notifications. Include AI-voice disclosure. |

**Lesson handoff:** Complete the project's next milestone, save a new version, and exchange a structured two-stars-and-a-wish peer test.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week11.tex`
- `1-introduction/teaching-material/workbook/week11.tex`
- `1-introduction/teaching-material/homework/week11.tex`
- `1-introduction/project/project-brief.tex`
- `1-introduction/project/project-teacher-guide.tex`
- `1-introduction/project/starter/my_art_show.py`

## Week 12: Showcase and Celebration

- **Driving question:** How can we demonstrate a project and explain the thinking behind it?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** showcase, demo, audience, explain, reflection, feedback
- **Misconception to prevent:** A showcase is only entertainment, or a bug encountered during development should be hidden.
- **Digital citizenship:** Share only approved project content, use nicknames, and ask before recording or posting anyone's work or image.

### Instructional objectives

- Prepare a focused two-minute demonstration of the final project.
- Explain one meaningful code choice and one debugging story.
- Reflect on growth and give specific, kind audience feedback.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Showcase hook** | All twelve workshop doors open into a gallery. Nova has two minutes to guide visitors through an interactive artwork. Should the demo show every line of code? No—the best museum guides choose a clear story. What did you make, what should we notice, and what did you learn while building it? | Doors fold into a gallery wall. A two-minute timer appears beside three empty story frames labeled Make, Notice, Learn. **On screen:** FINAL MISSION: Tell your coding story; Make • Notice • Learn | Keep the timer calm and noncompetitive; pause after the guiding question. |
| 0:25–1:20 | **Shape a two-minute demo** | Plan four short parts. First, say the project's title and mission. Second, enter one safe example and show the main result. Third, point to one code idea—perhaps a loop, choice, variable, or function—and explain what job it does. Fourth, share one next improvement. Rehearse once with a timer. If it runs long, choose the clearest example instead of speaking faster. Your audience needs time to see and think. | Four storyboard cards fill a 0:00–2:00 strip with flexible markers: mission, demo, code idea, next step. A speedometer stays in a calm zone. **On screen:** 1 Mission; 2 Safe demo; 3 One code idea; 4 Next improvement | Do not prescribe exact seconds to children; emphasize clarity and flexibility within the two-minute target. |
| 1:20–2:25 | **Explain code and a debugging story** | Showing code is not reading every symbol. Point to one meaningful part and translate it: ‘This for loop repeats my star function eight times. The function lets one tested recipe draw different sizes.’ Then tell a detective story: expected, actual, clue, one change, test. ‘I expected eight stars, got seven, saw range seven, changed it to eight, and reran.’ A solved bug is evidence of reasoning. It belongs in the story. | A code spotlight highlights only a for-loop and function call. Four detective panels animate the seven-to-eight-star debugging story. **On screen:** Point → Translate → Show result; Expected • Actual • Clue • Test; A solved bug shows learning | Use code that matches the project concepts; avoid presenting range(8) as always required. |
| 2:25–3:35 | **Prepare audience feedback and privacy** | Audience members are code explorers, not judges. Notice one specific choice and ask one curious question: ‘The random sizes made each run different. How did you choose the limits?’ Presenters may say, ‘I don't know yet,’ and add it to future ideas. Before the demo, use the privacy check: nickname only; no real name, school, address, contact details, password, computer username, or private notification. Ask permission before recording, photographing, or posting anyone's project or image. | Audience cards transform vague praise into a specific notice and curious question. A privacy shield checks each category and a camera waits behind an ASK FIRST sign. **On screen:** Audience: specific notice + curious question; Nickname only; Ask before recording or posting | Do not depict a child being recorded without consent. Use category words, not realistic private data. |
| 3:35–4:30 | **Reflection and celebration** | Level 1 complete! You learned to sequence exact steps, repeat with loops, react to events, choose with conditions, remember with variables, organize functions, test inputs, and debug with evidence. Your final reflection is not ‘Am I a perfect coder?’ Ask: What can I explain now? Which bug taught me something? What do I want to build next? Rehearse your two-minute demo, run the privacy check, and celebrate every creator's tested, explainable progress. The next code quest starts with your curiosity. | All concept badges form a constellation around the learner's project. Three reflection prompts appear with writing space; the gallery doors open toward a blank future map. **On screen:** I can explain…; A bug taught me…; Next I want to build…; SHOWCASE: Rehearse • Check • Share safely | Use warm music with room for applause, five-second reflection hold, and AI-voice disclosure. |

**Lesson handoff:** Rehearse the two-minute demo, run the privacy checklist, present, and complete the Level 1 reflection.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week12.tex`
- `1-introduction/teaching-material/workbook/week12.tex`
- `1-introduction/teaching-material/homework/week12.tex`
- `1-introduction/project/project-brief.tex`
- `1-introduction/project/project-teacher-guide.tex`
- `1-introduction/project/starter/my_art_show.py`

## 4. Automated, adaptable regeneration pipeline

### Architecture

```text
Level 1 sources ──> SHA-256 change detector ──> curriculum analyst agent
                                                    │
                                                    v
tracked plan/spec <── deterministic gates <── scriptwriter agent
       │                 ^                          │
       │                 └──── reviewer agent ──────┘
       v
scene cards / optional illustrations ──> voice provider ──> FFmpeg + captions
       │
       └──> ignored media output; tracked manifest records curriculum inputs
```

The Python pipeline uses the OpenAI Agents SDK for a typed, traceable three-agent workflow. A curriculum analyst extracts only source-supported outcomes, vocabulary, examples, and safety points. A scriptwriter turns that brief into the `VideoSpec` contract. A reviewer scores curriculum alignment, age fit, timing, accessibility, and safety; failed reviews return to the scriptwriter for at most two bounded revisions. Deterministic validators remain the final authority.

### Change and approval flow

1. `check` hashes the syllabus, teacher guide, weekly lesson, workbook, homework, exercises, and project sources. It reports exactly which weeks changed.
2. `generate` sends only stale weeks through the agent workflow, validates structured output, updates `videos/specs/level1.json`, refreshes this plan, and writes a new manifest.
3. A teacher reviews the script and storyboard in the PR. Paid media generation never begins implicitly.
4. `render --approved` creates deterministic cards or optional generated illustrations, synthetic narration through the configured provider, captions, and an MP4 for each approved week.
5. Generated media and API caches remain ignored. Scripts, evidence paths, configuration, and source hashes remain reviewable in Git.

### Commands

```bash
python3 -m venv .venv-videos
source .venv-videos/bin/activate
python -m pip install -r videos/requirements.txt
python -m videos.pipeline.cli check
python -m videos.pipeline.cli generate --week 7
python -m videos.pipeline.cli render --week 7 --approved
```

`OPENAI_API_KEY` is required for agent, illustration, or OpenAI voice calls. `ffmpeg` and `ffprobe` are required for MP4 rendering. The current OpenAI Speech API adapter is deliberately isolated because its supported models are scheduled to retire on January 6, 2027; replace the adapter with a Realtime voice implementation without changing lesson analysis, scripts, or render contracts.

### Automated quality gates

- Exactly one episode for each Level 1 week, in order.
- Runtime from 3:00 through 5:00 and narration within the 145-wpm budget.
- At least two objectives and four fully specified scenes per episode.
- Existing curriculum evidence for every episode; changed evidence makes the manifest stale.
- Narration, visuals, readable on-screen text, and production notes in every scene.
- Human `--approved` gate before media calls; no automatic publication.
- Caption track, AI-voice disclosure, accessible palette, and deterministic code/UI overlays.

### Maintainability decisions

- The JSON spec is the machine-readable source; this Markdown file is reproducible from it.
- Agent prompts and typed output contracts live in code, separate from curriculum content.
- Source fingerprints support incremental regeneration and make drift visible in CI.
- Media providers are adapters. Replacing image or voice technology does not change the educational workflow.
- Agent traces carry level, week, and source digest metadata for review and troubleshooting.
- The system proposes updates; deterministic checks and a teacher review decide whether they ship.
