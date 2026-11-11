# Level 1 Teaching Video Production Plan

> **Status:** Reviewed scripts and an automated regeneration contract for all 12 Level 1 lessons.
> Audience: Children in Grades 4–5 (ages 9–11) who are complete beginners. Every episode is at most 4:37 long (the limit is 5:00).
> This file is generated from `videos/specs/level1.json`; edit the JSON, then run `python -m videos.pipeline.cli plan --level 1`.

## 1. Instructional and creative direction

- **Series:** Nova & Pixel's Code Quest
- **Audience:** Children in Grades 4–5 (ages 9–11) who are complete beginners
- **Frame:** 16:9, 1920×1080, 24 or 30 fps
- **Narration:** Warm, curious, inclusive, and clear at about 140–145 words per minute; friendly without sounding babyish
- **Visual language:** Bright modern 2D motion graphics, real Scratch or Thonny captures, deterministic code overlays, and a recurring mission map
- **Accessibility:** Closed captions (an MP4 caption track plus .srt and .vtt files), Okabe–Ito palette, high contrast, large readable type, no color-only clues, gentle motion, and no rapid flashing

### Recurring story world

Nova is an inventive ten-year-old coder. Pixel is a palm-sized helper robot who takes instructions very literally. Nova writes the code and Pixel runs it exactly as written, so when something goes wrong the two investigate together. Each week, the pair opens a new door in the Code Quest workshop by learning one idea, testing it, and repairing one friendly bug. Learners are invited to predict before the answer appears.

### Five-part learning rhythm

Every episode follows the same reassuring rhythm: a surprising mission, one plain-language idea, a worked example, a friendly bug hunt, and a direct handoff to the lesson activity. The video launches hands-on learning; it does not replace it.

Bug hunts use the course's four detective steps: *What did I expect? What happened? Read one block (or line) at a time with your finger. Change one thing, then test again.*

### Production rules

- Keep the final runtime at or below 5:00, and each scene's narration within its own timing budget.
- Record at roughly 140 words per minute, with pauses after questions.
- Never show the answer to an exercise, homework, relay, exit ticket, card sort or the project reference; teach with a nearby example instead.
- Caption every spoken word. Never use color as the only clue.
- Render code, Scratch blocks, filenames, and UI labels as deterministic overlays—not inside generated artwork.
- Use the Okabe–Ito color palette, high contrast, readable type, gentle motion, and no rapid flashes.
- Show only nicknames and invented data. Never ask a child for a real name, address, school, password, or contact information.
- End with an age-appropriate practice prompt and normalize debugging as part of coding.
- Disclose synthetic narration on the end card, in the file metadata and in the video description.

## 2. Curriculum audit summary

The source review covered the Level 1 syllabus, teacher guide, all 12 lesson plans, workbook and homework chapters, every exercise brief and starter, and the final project materials. The sequence moves from Scratch (weeks 1–6) to Python and Thonny (weeks 7–12), while repeatedly connecting algorithms, events, loops, choices, variables, decomposition, testing, and reflection.

The videos preserve the course's strongest teaching choices: concrete analogies before vocabulary; one-change-at-a-time debugging; Grade 4–5 mathematics; visible, testable outcomes; creativity alongside correctness; safe sharing; and a final interactive art project. Each script below names the misconception it prevents and points learners back to the exact lesson activity.

In November 2026 every script was checked line by line against its week's lesson plan, workbook, homework and exercises. That review fixed handoffs that named the wrong exercise or task, three citizenship points that did not use the lesson's wording, Python code that did not match the course starters, invented project milestones, and five bug hunts or examples that gave away exercise or exit-ticket answers.

## 3. Episode scripts and storyboards

## Week 1: Robots Need Exact Instructions

- **Driving question:** How can we turn an idea into steps a computer can follow?
- **Planned runtime:** 4:37 (277 seconds)
- **Vocabulary:** algorithm, sequence, program, bug, sprite, stage, script, green flag
- **Misconception to prevent:** Computers can guess the missing parts of a vague instruction or quietly fix steps placed in the wrong order.
- **Digital citizenship:** Use your coding nickname in projects—never your real full name, address, school, birthday or photos. Scratch stays offline with no account; if anything asks for your name or a password, stop and get a grown-up.
- **Practice activity:** `1-introduction/exercises/week01/ex-hello-cat`

### Instructional objectives

- Explain that an algorithm is an ordered set of exact instructions.
- Identify the Scratch stage, sprite, block categories, code area, and green flag.
- Predict how changing the order of blocks changes what a sprite does.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:32 | **Mission hook** | Welcome to Code Quest! Meet Nova, a young inventor, and Pixel, a helpful robot who does exactly what it's told. Today, Nova needs Pixel to carry a glowing key to the workshop door. ‘Take it over there!’ says Nova. Pixel zooms off… and puts the key on a chair. Beep boop! Pixel did exactly what it heard. But the instruction wasn't exact. Can you give Pixel steps it can't misunderstand? | Workshop with Nova, Pixel, a chair and a locked door. Nova points vaguely; Pixel zooms to the chair, sets the key down and beeps proudly. Freeze on a thinking bubble before the question. **On screen:** MISSION: Deliver the key; Pause: What exact steps would you give? | Use a three-second prediction pause and a soft comic boing, not a failure buzzer. |
| 0:32–1:27 | **Explain algorithm and sequence** | Here's a secret about computers: they're a lot like Pixel. Super fast, super helpful, but they can't read your mind. So we give them an algorithm. An algorithm is a list of exact steps for a job. And sequence means the order of those steps. Let's try one. Step one: move forward three squares. Step two: turn right. Step three: move forward two squares. Step four: put the key beside the door. It worked! Now watch what happens if we put the key down before we move. Same steps, different order, different result. Order matters! | A floor grid seen from above. Numbered step cards appear one at a time and Pixel follows each one to the door. Then card 4 jumps to the top, Pixel drops the key at the start, and the door stays locked. **On screen:** Algorithm = exact steps; Sequence = the order; Same steps + new order = new result | Give every numbered card both a symbol and a label; do not rely on blue alone to identify the door. |
| 1:27–2:32 | **Connect to Scratch** | Scratch lets us build algorithms with blocks. The stage is where the action happens. A sprite is a character or object, like this cat. We click a block category, find a block, and snap blocks together in the code area to make a script. The green flag starts our script. Let's build one: when green flag clicked, say ‘Hello, coder!’ for two seconds, then move ten steps. Scratch reads the stack from top to bottom. So what will the cat do first? Yes! Speak, then move. | Clean labeled Scratch capture. Camera moves from the stage to the sprite list, the block categories, and the code area. Overlay a three-block stack and animate a bright outline down it. **On screen:** Stage = action area; Sprite = character or object; Code area: snap blocks into a script; Read blocks top → bottom | Use an authentic current Scratch interface capture. Render labels as overlays outside the capture. |
| 2:32–3:42 | **Friendly bug hunt** | Uh-oh, time for a bug hunt! Nova builds a greeting for Pixel's show, and Pixel runs it exactly. The blocks say: say ‘Thanks for watching!’, then say ‘Welcome to my show!’ Hmm… that sounds backwards. Let's use our detective steps. One: what did we expect? Two: what actually happened? Three: read the blocks one at a time, with your finger. Four: change one thing, and test again. Which blocks should trade places? Pause and point. Right! Move ‘Welcome to my show!’ to the top. Now it works! A bug is a clue, not a reason to quit. | Split screen: expected mini-storyboard versus actual. A pointing finger follows each block. The two say blocks visibly swap and the corrected stack runs. **On screen:** 1 What did we expect?; 2 What happened?; 3 Read one block at a time; 4 Change one thing. Test. | Leave four seconds for prediction. Use check marks only after the rerun proves the fix. Do not use Exercise 1.2's jump script or the socks-and-shoes exit-ticket example. |
| 3:42–4:37 | **Safety, recap, and handoff** | You unlocked the first door! Let's remember. Exact steps make an algorithm. Their order is the sequence. And Scratch runs a script from top to bottom. One more thing: when you name your project or sprite, use your coding nickname, never your real full name, school, address, birthday, or photos. Our Scratch app works offline, with no account. If any app asks for your real name or a password, stop and get a grown-up. Now open Hello, Cat! Make the cat say hello with your nickname, walk, meow, and say bye. Then click the green flag. Which step came first, and which came last? Happy coding! | Mission map door opens. Three recap icons appear, followed by a safe profile card labeled ‘StarCoder’ and crossed-out examples of private data categories. **On screen:** Exact steps • Right order • Test; Use a nickname; NEXT: Hello, Cat! | End card includes ‘Narration uses an AI-generated voice’ and a five-second clean hold for teachers to pause. |

**Lesson handoff:** Open Exercise 1.1 Hello, Cat!: under when green flag clicked, snap go to x: 0 y: 0, a nickname greeting, move 100 steps, play sound Meow until done and say Bye!, then click the flag and say which step came first and which came last.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week01.tex`
- `1-introduction/teaching-material/workbook/week01.tex`
- `1-introduction/teaching-material/homework/week01.tex`
- `1-introduction/exercises/week01/ex-hello-cat/README.md`
- `1-introduction/exercises/week01/ex-mixed-up-jump/README.md`

## Week 2: Loop-de-Loop

- **Driving question:** How can one short instruction make a repeated pattern?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** loop, repeat, forever, costume, Pen extension, degrees
- **Misconception to prevent:** The turn equals the inside corner angle (so a triangle needs 60°), or repeat and forever are interchangeable.
- **Digital citizenship:** Follow the 20-20-20 eye rule—every 20 minutes, look 20 feet away for 20 seconds—and take a stretch break.
- **Practice activity:** `1-introduction/exercises/week02/ex-polygon-party`

### Instructional objectives

- Use repeat for a known number of repetitions, and forever (with next costume) to keep an animation going.
- Explain how repeating move-and-turn steps draws a regular polygon.
- Debug a shape by checking the repeat count and turn angle.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Code Quest! Today's door needs a square of light. Nova starts writing: move, turn, move, turn, move, turn… The list gets so long, Pixel's paper rolls right across the floor! There must be a shorter way. What could tell Pixel to repeat the same two steps four times? | A comically long paper strip grows while a square outline waits unlit. Fold repeated move-turn cards into one loop card. **On screen:** MISSION: Light four sides; How can we avoid repeated blocks? | Pause for three seconds as the repeated pairs highlight together. |
| 0:30–1:25 | **Explain loops** | A loop repeats instructions. Use repeat when you know how many times. Repeat four runs the blocks inside it four times, then the program carries on. Use forever when something should keep going until you click the red stop sign, like a cat switching costumes again and again, so it looks like it's walking. So which one fits our four sides? Repeat four, because we know the number! | Two labeled tracks: repeat 4 reaches a finish flag; forever circles a cat switching costumes until a stop button is pressed. **On screen:** Loop = repeat instructions; repeat 4 → then carries on; forever → until stop | Use shape and labels as well as color to distinguish the two tracks. |
| 1:25–2:30 | **Build a polygon** | First, add the Pen extension: click the Add Extension button in the bottom-left corner, and choose Pen. Now pen down lets our sprite draw while it moves. A square has four equal sides, so: repeat four, move one hundred steps, turn ninety degrees. Four quarter-turns bring the sprite all the way around. For other regular shapes, use the course rule: the turn equals three hundred sixty, divided by the number of sides. A triangle has three sides, so it turns one hundred twenty degrees. Say it with me: sides tell us the repeats, and three hundred sixty divided by the sides tells us the turn! | The Add Extension button opens the Pen extension. A pen-down stack draws a square. A full-turn ring marked 360 splits first into four 90-degree pieces, then three 120-degree pieces. **On screen:** repeats = number of sides; turn = 360 ÷ sides; Square: repeat 4, turn 90° | Explain the rule visually; do not introduce algebraic notation beyond the course wording. |
| 2:30–3:40 | **Friendly bug hunt** | Time for a bug hunt! Nova asks Pixel to draw a nine-sided shape, but the drawing leaves a gap. Expected: nine sides that close. What happened? The path stops short. The stack repeats nine times, so the side count is right. Now check the turn. The script says thirty degrees. But a nine-sided shape needs three hundred sixty divided by nine, which is forty. Which one thing should we change? Pause and point. Change thirty to forty, test again, and the shape closes! That gap was a useful clue. | Open nine-sided path beside a closed outline. A detective checklist confirms repeat 9, circles turn 30, and replaces it with 40 before rerunning. **On screen:** Expected: closed shape; Check repeats, then turn; 360 ÷ 9 = 40° | Hold the faulty result long enough to inspect; celebrate the test, not speed. Never show the pentagon answer: it is the exit ticket and a Polygon Party table row. |
| 3:40–4:35 | **Well-being, recap, and handoff** | Door two glows! Loops make code shorter. Repeat is for a known number of times; forever keeps going until you click the red stop sign. For a regular shape, repeat once for each side, and turn three hundred sixty divided by the number of sides. While you build, look after your body: every twenty minutes, look about twenty feet away for twenty seconds, then stretch. Now open Polygon Party: add the Pen extension, draw a square, then a triangle, a hexagon and a pentagon. If a shape has a gap, check the repeats first, then the turn. Happy coding! | Door lights with a looping border. A gentle 20-20-20 card shows a window view, then transitions to the Polygon Party task card. **On screen:** repeat • forever • Pen; 20 minutes • 20 feet • 20 seconds; NEXT: Polygon Party | Keep all looped animation slow and stop motion during the eye-break card. Include the voice disclosure. |

**Lesson handoff:** Open Polygon Party: add the Pen extension, draw the square with repeat 4, then use turn = 360 ÷ sides for a triangle, hexagon and pentagon, and fix Leo's triangle.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week02.tex`
- `1-introduction/teaching-material/workbook/week02.tex`
- `1-introduction/teaching-material/homework/week02.tex`
- `1-introduction/exercises/week02/ex-polygon-party/README.md`
- `1-introduction/exercises/week02/ex-walking-cat/README.md`

## Week 3: When This Happens…

- **Driving question:** How can a program notice an event and choose what to do?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** event, condition, if, if-else, sensing, feedback
- **Misconception to prevent:** An if block keeps checking forever by itself, even when it runs only once.
- **Digital citizenship:** Give kind, specific feedback with ‘two stars and a wish’: two things you like and one kind idea, about the project, not the person; say thank you when you receive feedback.
- **Practice activity:** `1-introduction/exercises/week03/ex-tickle-ghost`

### Instructional objectives

- Explain that an event starts a script when something happens.
- Use if and if-else to choose actions from a condition.
- Place sensing choices inside a forever loop when they must keep checking.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Code Quest! Nova walks up to the workshop door. Nothing happens. ‘I checked once, before you arrived!’ says Pixel. A useful door has to keep noticing. So how can our program start with an event, check a condition, and react at the right time? | Door-sensor timeline shows Pixel checking once, then Nova arriving later. Freeze on the missing connection. **On screen:** MISSION: Make the door react; What should the program notice? | Use a clear timeline arrow and a three-second prediction pause. |
| 0:30–1:25 | **Explain events and conditions** | An event is something that starts the action. The green flag is clicked, a key is pressed, or a sprite is clicked. A condition is a yes-or-no question, like ‘touching mouse-pointer?’ An if block says: if the answer is yes, do this. An if-else block gives two paths. If yes, open the door. Else, keep it closed. Only one path runs each time the choice is checked. | Doorbell icons connect to event hats. A large yes/no road fork demonstrates an if-else choice with words and symbols. **On screen:** Event = starts action; Condition = yes/no question; if yes… else… | Show the complete condition inside the Scratch block; narrate its punctuation-free meaning. |
| 1:25–2:30 | **Build a responsive script** | Let's make a ghost giggle when the pointer touches it. Start with when green flag clicked. Inside forever, place an if-else. If touching mouse-pointer, say ‘That tickles!’ Else, say with an empty box, which clears the bubble. Why forever? The pointer might move later, so the program has to ask the touching question again and again. Watch the highlight go around the loop: check, choose, react. Check, choose, react. Now move away, and the other path runs. | Authentic Scratch block overlay beside a ghost. A pulse travels through forever, condition, yes path, then else path as the pointer moves. **On screen:** forever: keep checking; check → choose → react; Test YES and NO | Keep the pointer motion slow. Use labels YES and NO in addition to path colors. |
| 2:30–3:40 | **Friendly bug hunt** | Time for a bug hunt! Nova builds a door sensor: when green flag clicked, if touching Nova, say ‘Welcome!’ Pixel runs it exactly. Expected: it greets Nova whenever Nova touches it. What happened? It checked once, right at the start, when Nova was far away. Then the script finished. The condition is right, but the question has to be asked again and again. Where should the forever block go? Pause and point. Wrap forever around the if block. Test first with Nova away, then touching. Now both cases work! | Door-sensor sprite and a Nova sprite. A single scan line passes the script and disappears; then a forever bracket wraps the if and the scan line loops continuously. **On screen:** Bug: checked only once; Fix: keep the choice inside forever; Test both paths | Pause four seconds before wrapping the block; avoid implying forever belongs around every if. Do not use the homework's pet or the Tickle the Ghost script for this bug. |
| 3:40–4:35 | **Feedback, recap, and handoff** | The door hears us now! Events start scripts. Conditions ask yes-or-no questions. If and if-else choose a path, and forever keeps checking. When you look at a classmate's project, give two stars and a wish. Two stars are two things you like, said exactly. Nova says, ‘I like how the ghost grows when I touch it!’ A wish is one kind idea. Pixel asks, ‘What if it also played a sound?’ Talk about the project, not the person, and say thank you when you get feedback. Now build Tickle the Ghost, and test both paths: pointer touching, and pointer away. Happy coding! | Door opens to two test lanes. Two star cards and one wish card appear beside the ghost project, each with a specific comment. **On screen:** Events start; Conditions choose; Feedback: two stars and a wish; NEXT: Tickle the Ghost | Finish on a test card with two boxes: pointer away and pointer touching. Include the voice disclosure. |

**Lesson handoff:** Build Tickle the Ghost: an if-else with touching mouse-pointer? inside forever; test with the pointer touching and with it away.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week03.tex`
- `1-introduction/teaching-material/workbook/week03.tex`
- `1-introduction/teaching-material/homework/week03.tex`
- `1-introduction/exercises/week03/ex-tickle-ghost/README.md`
- `1-introduction/exercises/week03/ex-arrow-explorer/README.md`

## Week 4: Keeping Score with Variables

- **Driving question:** How can a program remember a number that changes?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** variable, value, set, change, random, credit, remix
- **Misconception to prevent:** ‘set score to 1’ and ‘change score by 1’ do the same job, or a catch is counted only once by itself, even while the apple stays touching the bowl.
- **Digital citizenship:** Give credit for the art, sounds and ideas you use: add a credits comment for Scratch library sprites, and when you remix a friend's project, say whose project you started from.
- **Practice activity:** `1-introduction/exercises/week04/ex-apple-catch`

### Instructional objectives

- Describe a variable as a named place that stores a value.
- Distinguish setting a variable from changing it.
- Use pick random to place a sprite somewhere new, and fix a score that never resets or goes up too fast.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Code Quest! Nova catches three falling stars. One, two, three! Pixel cheers, but the scoreboard still says zero. ‘I watched every catch,’ says Pixel, ‘but I forgot the number!’ Our next door opens at five points. So what can a program use to remember a value while it changes? | Three stars land in a basket while a frozen scoreboard stays at zero. A labeled empty memory box appears beside Pixel. **On screen:** MISSION: Remember the score; What can store a changing value? | Count catches aloud with matching visual pips; pause after the question. |
| 0:30–1:25 | **Explain variables** | A variable is a named place where a program stores a value. Imagine a labeled box called score. At the start, set score to zero. That replaces whatever was there with zero. After one catch, change score by one. That takes the current value and adds one. Set replaces. Change adjusts. So if score is three, setting it to one gives one, but changing it by one gives four. Which command belongs after a catch? Change by one! | A physical box labeled score swaps cards for set and adds a +1 chip for change. Side-by-side results animate from 3. **On screen:** Variable = named storage; set → replace; change → add | Use arrows and operators as well as color; hold the 3→1 and 3→4 comparison. |
| 1:25–2:30 | **Build catch-game logic** | Here's the catch-game plan. When the green flag is clicked, set score to zero. Put the action inside forever. Make the apple fall. If it touches the bowl, change score by one, then move the apple to a random place at the top. The pick random block, in Operators, works like rolling a die. You get a number from a range, but you can't know which one. And the order matters: count one catch, then reset the apple before checking again. | Flow diagram and matching Scratch stack: reset, loop, fall, sense, score, random reset. A numbered outline follows execution. **On screen:** 1 Reset; 2 Check catch; 3 Add 1; 4 Move apple | Show random x-position as several allowed landing lanes, not as unexplained magic. |
| 2:30–3:40 | **Two-bug investigation** | Time for a bug hunt! Pixel finds two clues in Nova's star game. First, a new game begins with the last game's score. Expected: zero. What happened? Seven! The green-flag script forgot set score to zero. Second, one star gives lots of points. Remember the paper-ball game, when we scored for every second someone held the ball? Here, forever keeps asking ‘touching basket?’ while the star sits in the basket. What should happen right after adding one? Pause and point. Send the star back to the top before the next check. Change one thing, test, then investigate the next clue. | Detective board shows bug A: stale score and bug B: rapidly spinning counter. Repairs are applied and tested separately. **On screen:** Bug A: no reset; Bug B: counts one catch many times; Fix one clue, then test | Do not glamorize the runaway score with frantic flashing; keep counter motion readable and brief. Use the hook's stars and basket, not Mei's apple script from the exercise. |
| 3:40–4:35 | **Credit, recap, and handoff** | Five points, and the door opens! Variables store values. Set replaces a value; change adds to it. Pick random makes games less predictable, and careful order stops extra points. Our apple and bowl were drawn by real people and shared in the Scratch library, so we give credit. Right-click the code area, choose Add Comment, and type: ‘Credits: sprites and sounds from the Scratch library.’ If you remix a friend's project, say whose project you started from. Now build Apple Catch. Start at zero, count exactly one point for each catch, and test a brand-new game twice. Happy coding! | Score reaches five. A Scratch comment note appears in the code area reading ‘Credits: sprites and sounds from the Scratch library.’ Then the Apple Catch challenge appears. **On screen:** Store • Set • Change; Credit: Add Comment → credits note; NEXT: Apple Catch | Use invented nicknames only. Include the voice disclosure on the held end card. |

**Lesson handoff:** Build Apple Catch: the Bowl follows the mouse, set score to 0 at the start, change it by 1 per catch, send the apple back to the top right after scoring, and add a credits comment.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week04.tex`
- `1-introduction/teaching-material/workbook/week04.tex`
- `1-introduction/teaching-material/homework/week04.tex`
- `1-introduction/exercises/week04/ex-apple-catch/README.md`
- `1-introduction/exercises/week04/ex-pop-balloon/README.md`

## Week 5: Messages and My Blocks

- **Driving question:** How can we organize a big project into small jobs that work together?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** decomposition, My Block, define, input, broadcast, when I receive
- **Misconception to prevent:** A broadcast reaches only the selected sprite, or message names that look similar will automatically match.
- **Digital citizenship:** Design for everyone: use color-blind-safe colors, add a word, shape, or pattern so color is never the only clue, and keep text big enough to read.
- **Practice activity:** `1-introduction/exercises/week05/ex-shape-machine`

### Instructional objectives

- Break a repeated job into a named My Block with an input.
- Use broadcast and when-I-receive messages to coordinate sprites.
- Debug communication by checking exact message names and event order.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Mission hook** | Welcome back to Code Quest! The workshop stage has three performers. Nova tries to control every move in one giant stack. The blocks wobble higher than Pixel! One performer starts late, and another never moves. ‘This stack is too big!’ says Nova. Could we give each small job a name, and send one clear message when the curtain goes up? | A towering Scratch stack bends while three performers wait. It separates into neat labeled cards connected by one message envelope. **On screen:** MISSION: Organize the show; Small jobs + clear messages | Use gentle squash-and-stretch on the block tower; pause for learner ideas. |
| 0:30–1:25 | **Explain decomposition and My Blocks** | Decomposition means splitting a big job into smaller named parts. In Scratch, My Blocks, then Make a Block, lets us name a job we want to reuse. Nova makes a block called polygon, with two inputs: sides and length. Under the pink define hat go: pen down, repeat sides, move length steps, turn three hundred sixty divided by sides, and pen up. Now the main script can say polygon three, one hundred twenty, or polygon six, sixty. An input is a blank we fill in each time, so one block makes lots of shapes! | Big ‘art show’ puzzle splits into shape, movement, and speech pieces. A pink define polygon (sides) (length) hat receives 3, 120 then 6, 60 and draws two labeled results. **On screen:** Decomposition = smaller jobs; My Block = named reusable job; Input = a blank you fill in each time | Show the course's block structure accurately; keep the polygon turn formula visible as an overlay when used. |
| 1:25–2:30 | **Coordinate with messages** | A broadcast is like a stage manager's announcement. Nova's main script broadcasts curtain up. Every sprite with a ‘when I receive curtain up’ hat can respond. The star spins, the cat speaks, and the backdrop changes. Broadcasting doesn't make every sprite do the same action. It gives the scripts that are listening the same starting signal. Message names must match exactly, including spaces. One clear announcement can coordinate lots of small jobs. | Stage manager sends a CURTAIN UP envelope outward. Three separate receiver scripts light up and perform different actions in parallel. **On screen:** broadcast [curtain up]; when I receive [curtain up]; One signal, different jobs | Use radio-wave symbols plus labels; avoid implying the message contains private chat content. |
| 2:30–3:40 | **Friendly bug hunt** | Time for a bug hunt! In Nova's show, the star never spins. Expected: all three performers start. What happened? Only two respond. Read the sender: broadcast ‘curtain up’. That's two words. Now read the star's receiver: when I receive ‘curtainup’. That's one word! Scratch treats those as different messages. Which name should change? Pause and point. Either spelling works, but the sender and receiver must use the exact same message. Choose one from the dropdown, test again, and the star joins the show! | Two message tags align under a magnifier; a visible space separates CURTAIN UP. The receiver selects the same dropdown item and a test pulse reaches all three sprites. **On screen:** Expected: 3 performers; Actual: 2 performers; Message names must match exactly | Do not fix by retyping if the dropdown can prevent a mismatch; model the safer action. Do not show Show Time's start show / show start bug. |
| 3:40–4:35 | **Accessibility, recap, and handoff** | It's showtime! Decompose a big project into smaller jobs. Put repeated jobs in named My Blocks, use inputs to change them, and broadcast exact messages to coordinate sprites. Make your show easy for more people to understand. If red means stop and green means go, add the words or clear symbols too. Color should never be the only clue, and text should be big enough to read. Now build Shape Machine, then Show Time, where a presenter and a dancer pass messages, and you solve its bug hunt. Happy coding! | Door becomes a stage curtain. A color-only stop/go display gains STOP/GO labels and shapes, followed by a two-part activity card. **On screen:** Small jobs • My Blocks • Exact messages; Use words or symbols with color; NEXT: Shape Machine + Show Time | Verify contrast in both light and grayscale previews. Include the voice disclosure. |

**Lesson handoff:** Build Shape Machine (a polygon My Block with sides and length inputs, then add a pentagon), then build Show Time, where a presenter and a dancer pass the messages start show and finale, and solve its nobody-receives bug hunt.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week05.tex`
- `1-introduction/teaching-material/workbook/week05.tex`
- `1-introduction/teaching-material/homework/week05.tex`
- `1-introduction/exercises/week05/ex-shape-machine/README.md`
- `1-introduction/exercises/week05/ex-show-time/README.md`

## Week 6: Scratch Detective Checkpoint

- **Driving question:** Can we combine our Scratch ideas and explain how we debug?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** sequence, loop, event, conditional, variable, My Block, debugging
- **Misconception to prevent:** Debugging means guessing many changes at once or that a working project needs no explanation.
- **Digital citizenship:** Fun and fair for everyone: the same rules for all, no tricks, everyone can see and read it, credit is given, and no pressure to keep playing forever.
- **Practice activity:** `1-introduction/exercises/week06/ex-relay-wonky-hexagon`

### Instructional objectives

- Name and explain the six big ideas: sequence, loops, events, conditionals, variables, and My Blocks.
- Apply the four detective steps and explain the evidence for a fix.
- Relate familiar Scratch blocks to upcoming Python ideas.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **Checkpoint hook** | Welcome back to Code Quest! Six workshop doors glow behind Nova and Pixel. The checkpoint console mixes up every symbol we've found: a flag, a loop, a question, a score box, and a pink My Block. Can you name what each one does? Today, you're the lead code detective! | Mission map zooms across six doors. Five familiar icons land on a detective board as unlabeled evidence cards. **On screen:** CHECKPOINT MISSION; Name it • Use it • Explain it | Pause briefly on each icon so a teacher can solicit answers. |
| 0:30–1:25 | **Retrieve six big ideas** | Let's name them. Sequence is steps in order. A loop repeats steps. An event, like the green flag, starts a script. A conditional asks a yes-or-no question, then chooses. A variable is a labeled box that remembers. And a My Block gives a part a name, so we can use it again. In a catch game, the green flag starts it, forever repeats the falling, touching the bowl is a condition, score is a variable, and a My Block could name a job, like drop apple. The ideas work as a team! | Each icon receives its label and then docks onto a single catch-game flow diagram at the exact place it contributes. **On screen:** Sequence • Loop • Event; Conditional • Variable • My Block; Ideas work together | Use consistent symbols from earlier episodes to support retrieval, not new decorative icons. |
| 1:25–2:30 | **Model debugging evidence** | A code detective doesn't mash blocks until something works. We use the four detective steps. One: what did I expect? Two: what happened? Three: read the blocks one at a time, with your finger. Four: change one thing, then test again. Nova's cat should go to the middle and say ‘Hello, detectives!’ It moves, but it says nothing. Pixel points at each block. ‘When flag clicked: yes. Go to: yes. Say… wait, there's a gap!’ That block isn't snapped on, so it's not part of the script. One change: snap it on. Test. Hello! | Four numbered detective lenses: the cat in the middle with no speech bubble; the stack with a visible gap above the say block; a finger tracing each block; the block snaps on and the bubble appears. **On screen:** 1 What did I expect?; 2 What happened?; 3 Read one block at a time; 4 Change one thing, then test | Recreate the lesson demo: when flag clicked, go to x: 0 y: 0, gap, say Hello, detectives! for 2 seconds. Never show any relay project (Wonky Hexagon, Apple Catch, Silent Party) or its fixes. |
| 2:30–3:40 | **Bridge from Scratch to Python** | Soon, our blocks will turn into typed Python. But the ideas stay with us. For example, the green flag becomes Thonny's Run button. In today's card sort, you'll match Scratch blocks to Python lines. Look for clue words: a Python word often sounds like the words on the block. Watch for new marks too: parentheses, quote marks, and colons, where every letter matters. Which Python line do you think matches the say block? Pause and think. Make a guess, then check it with your partner. Later, a My Block will become a Python function, a command we name ourselves. And you already know how to plan, predict, test, and debug! | Scratch block cards face face-down Python cards; only the green flag ↔ Run button pair is revealed. **On screen:** Blocks change. Ideas continue.; green flag → Run button; Clue words • ( ) • " " • :; Guess, then check together | Do not reveal any card-sort or Homework 6 match (move, turn, say, repeat, pen up/down, set/change variable, if, ask, random, go to). Keep code as deterministic overlays. |
| 3:40–4:35 | **Fair design, recap, and handoff** | Detective training complete! Strong coders build and explain. Strong detectives use evidence, and change one thing at a time. Strong designers make projects fun and fair: the same rules for everyone, no tricks, and no pressure to keep playing forever. Now start the bug-hunt relay. Build each project card exactly as printed, bugs and all. Before you touch a block, tell your partner what you expected and what happened. Each project hides two bugs, so write both on your relay baton. Then show what you know in the short checkpoint. Happy coding! | Badges read Builder, Detective, Explainer. A fairness checklist shows same rules, no tricks, and no pressure, then the relay baton card appears. **On screen:** Build • Debug • Explain; Fun + fair for everyone; NEXT: Bug-hunt relay | End with a five-second teacher pause card and the voice disclosure. |

**Lesson handoff:** Start the bug-hunt relay: build each broken project card exactly as printed, use the four detective steps to find its two bugs, and write expected, happened, bug, and fix on the relay baton. Then do the short checkpoint.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week06.tex`
- `1-introduction/teaching-material/workbook/week06.tex`
- `1-introduction/teaching-material/homework/week06.tex`
- `1-introduction/exercises/week06/ex-relay-broken-catch/README.md`
- `1-introduction/exercises/week06/ex-relay-silent-party/README.md`
- `1-introduction/exercises/week06/ex-relay-wonky-hexagon/README.md`

## Week 7: Hello, Python!

- **Driving question:** How do typed instructions make words and turtle drawings appear?
- **Planned runtime:** 4:35 (275 seconds)
- **Vocabulary:** Python, Editor, Shell, Run, comment, turtle
- **Misconception to prevent:** Python guesses misspellings or ignores punctuation and capitalization the way a person might.
- **Digital citizenship:** Save files safely: keep work in one place (exercises in their own folder with Cmd+S, new programs in Documents/my-python), use sensible names with small letters and underscores like flag_drawing.py, never name a file turtle.py, and keep real names and addresses out of programs.
- **Practice activity:** `1-introduction/exercises/week07/ex-hello-python`

### Instructional objectives

- Identify Thonny's Editor, Shell, Run button, and turtle window.
- Use print, comments, and basic turtle movement in a saved Python file.
- Read the final error message and line number to repair a simple typo.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:30 | **New-language hook** | Welcome back to Code Quest! Today's door has no Scratch blocks, only a blinking text cursor. Nova types ‘Hello, Pixel!’ and presses Run. The words appear, and Pixel's screen lights up! We've crossed into Python, where we write instructions with text. The ideas are familiar. The way we spell them is new. | Blocks transform into carefully typeset text. A cursor blinks in a simplified Thonny Editor and output appears in the Shell. **On screen:** NEW MISSION: Python; Familiar ideas, typed instructions | Use a real Thonny capture after the stylized transition; keep code crisp and selectable in source assets. |
| 0:30–1:25 | **Tour Thonny** | Thonny is our Python workshop. We write the program in the Editor, the big part at the top. The green Run button is like the green flag: it tells Python to follow the file. The Shell, at the bottom, is where Python talks back, with words and red error messages. Turtle programs also open a drawing window, which can hide behind Thonny. Thonny asks you to save before running. Save new programs in your my-python folder, with a name that says what the program does, like flag_drawing.py. | Real Thonny interface with four large callouts, followed by a file-name card comparing flag_drawing.py with a vague name. **On screen:** Editor: write; Run: like the green flag; Shell: Python talks back; Turtle window: drawings | Verify UI labels against the supported Thonny version. Never display a real home-folder username. |
| 1:25–2:30 | **Write first Python and turtle commands** | Let's type our first line. Print, open parenthesis, quotation mark, Hello, coder!, closing quotation mark, close parenthesis. Print shows words in the Shell. A line that starts with a hash mark is a comment. It's a note for people, and Python skips it. Every turtle program has the same shape. Import turtle gets the toolbox. t equals turtle dot Turtle, with a capital T, makes a turtle called t. Then t dot forward one hundred moves, and t dot left ninety turns. Turtle dot done keeps the window open. Run it, and watch each exact instruction happen in order. | Large syntax-highlighted overlays appear line by line: print, a comment, import turtle, t = turtle.Turtle(), t.forward(100), t.left(90), turtle.done(). A turtle moves 100 and turns left 90 with labeled distance and angle arcs. **On screen:** print("Hello, coder!"); import turtle; t = turtle.Turtle(); t.forward(100) then t.left(90) | Code overlays must be exact and match the course starters (import turtle, t = turtle.Turtle(), turtle.done()). Read punctuation naturally but point to matching marks. |
| 2:30–3:40 | **Error-message bug hunt** | Time for a bug hunt! Nova typed t dot lef, with one letter missing. Expected: a corner. What happened? One line, then the turtle stops, and red text appears in the Shell. Don't panic, and don't read every line first. Find the line number, then read the last line. It says line four, and that the Turtle has no attribute lef. That means Python doesn't know a turtle command called lef. It even asks: did you mean left? What single change should we test? Pause and point. Add the missing letter t to make left, run again, and the turtle turns the corner! Errors are clues, not danger. | Sanitized Thonny capture: line 4, t.lef(90), last line AttributeError: 'Turtle' object has no attribute 'lef'. Did you mean: 'left'? Zoom to the line number and last line; a letter t slides onto lef; the rerun draws the corner. **On screen:** 1 Find the line number; 2 Read the last line; 3 Change one thing; 4 Run again | File lines: 1 import turtle, 2 t = turtle.Turtle(), 3 t.forward(100), 4 t.lef(90), 5 t.forward(100), 6 turtle.done(). Show the file name only, never a local path or username. Verify the ‘Did you mean’ line in the supported Thonny (bundled Python 3.10+). Keep red text but add icons and labels. Do not use Typo Hunt's bugs. |
| 3:40–4:35 | **Safety, recap, and handoff** | Python door unlocked! In Thonny, write in the Editor, press Run, and read the Shell. Print shows words, comments help people, and the turtle moves and turns. Spelling, capital letters, quotes, and parentheses all matter. Save safely: exercises stay in their own folder, new programs go in my-python, and names say what the program does. Never call a file turtle.py, and keep real names and addresses out of your code. Now run Hello, Python!, then finish My First Square. If it stops, the last line of the error is your clue. Happy coding! | Four-tool recap orbit around the open door, then a good-file-name card and a two-step activity handoff. **On screen:** Write • Run • Read; Good name: flag_drawing.py; NEXT: Hello, Python! + My First Square | Hold the activity card for five seconds and include the voice disclosure. |

**Lesson handoff:** Open Exercise 7.1 Hello, Python! in Thonny and add three print lines (nickname only), then finish Exercise 7.2 My First Square and run its self-check.

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
- **Vocabulary:** for loop, range, indentation, off-by-one bug, nested loop, list
- **Misconception to prevent:** Indentation is just decoration, or range(4) counts 1 to 4 (or 0 to 4) and so repeats a different number of times.
- **Digital citizenship:** Ask for help well: first try three before me (red message, workbook, partner), then use the help sentence: I expected …, but … happened. I tried ….
- **Practice activity:** `1-introduction/exercises/week08/ex-loop-square`

### Instructional objectives

- Write a for loop with range, a colon, and consistent four-space indentation.
- Use a loop to draw regular polygons with turtle.
- Recognize off-by-one and indentation bugs from visible results and errors.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Welcome back to Code Quest! Pixel types forward and left, four times, to draw a square. ‘This feels familiar,’ Nova says. ‘We used a Scratch repeat block for this!’ Python can loop too. But instead of a block's colored border, spaces show which instructions repeat. Can we shrink eight lines into three? | Eight repeated Python lines fold into a for-loop card. Four visible space markers form a guide rail under the loop header. **On screen:** MISSION: Make repetition shorter; In Python, spaces can show a group | Use visible dot glyphs only as a teaching overlay; clarify learners type spaces, not dots. |
| 0:25–1:20 | **Explain for, range, colon, and indentation** | Read this line: for i in range four, colon. It means: repeat the pushed-in lines four times. The colon says a group is coming. Every line inside starts with the same four spaces. That's called indentation. Thonny helps: after a colon, press Return, and it pushes the next line in for you. Range four gives four numbers: zero, one, two, three. Python starts counting at zero, but there are still four numbers, so the loop runs four times. The i keeps count, even when our drawing doesn't use it. | The code line enlarges in parts. Four seats labeled 0, 1, 2, 3 fill one by one; four-space guides align two body lines. **On screen:** for i in range(4):; colon → a group follows; 4 spaces → inside the loop; range(4) → 0, 1, 2, 3 = 4 times | Render exact monospaced code and show indentation guides without tabs. |
| 1:20–2:25 | **Draw polygons and preview nesting** | For a square, put t dot forward one hundred and t dot left ninety inside range four. The secret shape rule is back: repeats equal sides, and the turn equals three hundred sixty divided by sides. A triangle repeats three times and turns one hundred twenty. A loop can even hold another loop. That's a nested loop. In Square Flower, the outer loop takes one color at a time from a list called PALETTE, and the inner loop draws a whole square. The inner lines get eight spaces: four, then four more. | Square code runs with four highlighted trips, then values change to a triangle. A light preview shows a square flower with inner and outer loop brackets and a row of PALETTE color chips, each labeled. **On screen:** repeats = sides; turn = 360 ÷ sides; Nested loop = a loop inside a loop; for color in PALETTE: | Treat nesting as a preview, not a mastery demand. Use brackets and labels for each loop level. |
| 2:25–3:35 | **Two-clue bug hunt** | Time for a bug hunt! Nova wants a triangle, but the turtle draws only two sides. Count the trips: the code says range two. That's an off-by-one bug: the loop runs one time too few. A triangle has three sides, so change two to three, and test. Next, Nova's triangle is one long straight line! Look at the spaces. t dot left one hundred twenty isn't pushed in, so it's outside the loop, and it turns only once, at the end. Push it in four spaces, under t dot forward, and test. If the spaces don't match, Python shows a red IndentationError. Pause before each repair: what evidence tells us which one thing to change? | Open two-sided triangle links to range(2); then one long line links to an un-indented t.left(120) with space guides; repairs are tested separately; a small inset shows a mismatched-space IndentationError. **On screen:** Clue 1: loop runs one time too few; Clue 2: a line outside the loop; Use evidence. Fix one thing. Test. | Do not show a range(3) square or a star with its turn outside the loop (Homework 8). Real wording: ‘IndentationError: unindent does not match any outer indentation level’ or ‘IndentationError: unexpected indent’. Allow four seconds for each prediction. |
| 3:35–4:30 | **Help-seeking, recap, and handoff** | Python loops are ready! A for loop repeats the pushed-in lines. Range sets how many times, the colon starts the group, and four matching spaces show what belongs inside. Stuck? Try three before me: read the red message, check the workbook, and ask your partner. Then use the help sentence, like Nova: ‘I expected a triangle, but a straight line happened. I tried counting the spaces.’ Now build Loop Square, then write a square loop and a hexagon loop for Polygon Party. Predict the shape before you press Run. Happy coding! | Loop parts snap into a complete card. A weak ‘It doesn't work’ bubble expands into expected, actual, and tried fields, then the activity card appears. **On screen:** I expected… but… happened. I tried…; Predict before Run; NEXT: Loop Square + Polygon Party | End on code with visible indentation guides and the voice disclosure. |

**Lesson handoff:** Build Loop Square (add t.left(90) inside the loop, lined up under t.forward(100)), then in Polygon Party write a loop for a square and a loop for a hexagon, using turn = 360 ÷ sides.

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
- **Vocabulary:** variable, input, string, int, comparison, if, elif, else
- **Misconception to prevent:** Input automatically becomes a number, or Python checks every branch after an earlier condition is already true.
- **Digital citizenship:** Questions a program should NOT ask: ask about choices (colors, sizes, numbers), never about who you are. No full name, home address, school, birthday, password or photo. If an app or game asks for personal details, stop and ask a grown-up.
- **Practice activity:** `1-introduction/exercises/week09/ex-size-it`

### Instructional objectives

- Store input in variables and convert number text with int when needed.
- Use if, elif, and else as an ordered set of choices.
- Test normal and boundary inputs while protecting private information.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Mission hook** | Welcome back to Code Quest! The next door asks, ‘Choose a portal size: 40, 80, or 120.’ Nova types 80. Pixel stores the answer, but then tries to add ten and gets stuck. The input looked like a number. So why does Python see it as text? And how can our program choose the right portal? | A portal console accepts 80, which lands on a card marked text. A plus-ten gear cannot connect until a converter appears. **On screen:** MISSION: Ask, remember, choose; Input begins as text | Pause before revealing the text label; represent data type with words and shape, not color alone. |
| 0:25–1:20 | **Explain variables, input, and conversion** | A Python variable is a name connected to a value. This line asks a question and stores the answer: color underscore name equals input, open parenthesis, a playful question, close parenthesis. Input returns a string, which means text, even if you typed digits. When we need number math or comparisons, int can convert suitable digit text into a whole number. Size equals int of input. First ask, then convert, then use. | Variable name tags connect to text cards. Exact code overlays animate through ask → store text → int converter → store whole number. **On screen:** color_name = input(...); input → text; size = int(input("Pick a size: ")) | Use exact nested parentheses and a simple whole-number explanation; do not introduce floats. |
| 1:20–2:25 | **Build ordered choices** | An if-elif-else chain is an ordered set of doors. Python checks from the top. The first rule that's true wins, and the rest are skipped. Else catches everything left over, and else never has a condition. Try this rule: if size is greater than 100, open the big portal; elif size is greater than 50, open the medium portal; else, open the small one. 120 goes big, and only big. 80 goes medium. 40 goes small. Here's a tricky one: 100! 100 isn't greater than 100, so it goes medium. Remember: one equals sign puts a value in a box. Two equals signs ask, ‘Are these the same?’ | Three physical doors align top to bottom. A token tests each condition and stops at the first true branch; exact code sits beside the animation. **On screen:** if size > 100:; elif size > 50:; else:; First true rule wins | Distinguish assignment = from comparison == with a close-up callout. |
| 2:25–3:35 | **Input bug hunt and testing** | Time for a bug hunt! Pixel asks, ‘How many steps should I walk?’ Nova types 100. Expected: Pixel walks 100 steps. Actual: a red TypeError! Pause: what's inside the box called steps? Type steps in the Shell. Thonny shows ‘100’ with quote marks. That's text, and a turtle can't walk text. The fix: steps equals int of answer. Run again with 100, then 50, then 250. One more test: on a color question, type Blue with a capital B. No crash, but it goes to else, because Python is picky: ‘Blue’ and ‘blue’ are different. That's why a friendly else message helps. | Text card ‘100’ (with quote marks) fails to drive the turtle and a red TypeError line appears; int turns it into the number tile 100. A short test table fills Expected and Actual rows. **On screen:** Text '100' ≠ number 100; int(answer) → a number; "Blue" ≠ "blue" | Do not claim int handles every input safely; frame non-digit handling as later learning. |
| 3:35–4:30 | **Privacy, recap, and handoff** | Portal opened! Input asks, variables remember, int turns digit text into a number, and if-elif-else picks the first true path. Here's our rule: ask about choices, like colors, sizes, and numbers, never about who you are. So no full name, home address, school, birthday, password, or photo. If an app or game asks for personal details, stop and ask a grown-up. Now open Exercise 9.1, Square of Any Size, then 9.2, Pick a Color. Test every answer: orange, blue, green, and something silly, like pizza. Happy coding! | Safe-question cards pass through a shield; private-data category cards stop outside. The two activity cards slide into the workshop. **On screen:** Ask • Store • Convert • Choose; Ask about choices, not about you; NEXT: Square of Any Size + Pick a Color | Use category names only, no examples that resemble real personal data. Include the voice disclosure. |

**Lesson handoff:** Start with Exercise 9.1 Square of Any Size (fix the ‘text, not a number’ bug with int), then 9.2 Pick a Color (add an elif for green and a friendly else). Test orange, blue, green and pizza. Try 9.3 How Many Stars? if there is time.

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week09.tex`
- `1-introduction/teaching-material/workbook/week09.tex`
- `1-introduction/teaching-material/homework/week09.tex`
- `1-introduction/exercises/week09/ex-color-choice/README.md`
- `1-introduction/exercises/week09/ex-size-it/README.md`
- `1-introduction/exercises/week09/ex-star-row/README.md`
- `1-introduction/exercises/week09/hw-math-quiz/README.md`

## Week 10: Random Art and Our Own Commands

- **Driving question:** How can functions and randomness turn one idea into many artworks?
- **Planned runtime:** 4:30 (270 seconds)
- **Vocabulary:** function, define, call, parameter, random, randint, remix
- **Misconception to prevent:** Defining a function makes it run immediately, or random means the program can choose anything without limits.
- **Digital citizenship:** Being an original artist: borrowing an idea is fine when you make it your own and give credit in a comment (# Flower idea remixed from Exercise 10.1). Copying a whole program and calling it yours is not fair. Our art is drawn by code, so no internet pictures are needed.
- **Practice activity:** `1-introduction/exercises/week10/ex-flower-stamp`

### Instructional objectives

- Define and call a function with a parameter.
- Use random choice and randint within clear limits.
- Plan a Level 1 art-show project by combining reusable parts.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Creative mission hook** | Welcome back to Code Quest! The workshop gallery needs a hundred flowers, and no two should look exactly alike. Nova could copy the same drawing code again and again. But Pixel has a better idea: ‘Teach Python one flower-making command, then call it with different sizes and random colors!’ Can one recipe create a whole garden? | One flower multiplies into a varied garden. Repeated code sheets fold into a single recipe card with adjustable dials. **On screen:** MISSION: One recipe, many artworks; Reusable + adjustable + surprising | Use calm variation, avoiding rapidly cycling colors. Pause on the recipe metaphor. |
| 0:25–1:20 | **Explain functions and parameters** | A function is your own command, just like a My Block in Scratch. We write def, the name flower, and an input slot in parentheses: a parameter called size. Then a colon. The pushed-in lines are the recipe. But a recipe card isn't a cake. Defining writes the card; nothing is drawn yet. To use it, call flower, open parenthesis, sixty, close parenthesis. Sixty goes into the size slot. Define once, call many times: thirty, sixty, and ninety make three flower sizes from one recipe. | Exact def code builds a recipe machine. Calls with 30, 60, and 90 feed labeled values into the size slot and produce three flowers. **On screen:** def → define the recipe; parameter → input slot; flower(60) → call the function | Keep the function body aligned with four spaces. Flower Stamp's starter uses flower(x, y); keep this video's flower(size) visibly different and never show the exercise's calls. |
| 1:20–2:25 | **Add bounded randomness** | First, write import random at the top, next to import turtle. Random dot choice picks one item from a list, like picking a crayon from a bag with your eyes closed. Here, it picks from our color-blind-safe PALETTE. Random dot randint, ten comma eighty, picks a whole number from ten up to eighty, and both ten and eighty can be picked. Smaller number first! Random doesn't mean ‘anything in the universe.’ We choose the limits. A loop can call our flower function several times with new choices, so the garden changes every run, but it still follows our rules. | A choice wheel contains four named accessible colors. A number gate visibly spans 10 through 80. Both feed the flower function inside a loop. **On screen:** import random; random.choice(PALETTE); random.randint(10, 80); Random choices stay inside our limits | Use the actual inclusive randint behavior. Avoid color-only identification by labeling swatches. |
| 2:25–3:35 | **Function-call bug hunt** | Time for a bug hunt! Nova's program runs with no red error, but the screen stays blank. ‘Where's my flower?’ asks Nova. What did we expect? One flower. What actually happened? Nothing. Read the code one line at a time, with your finger. The flower recipe looks perfect. But scan below it: nothing ever calls it. Defining writes the recipe; calling makes it run. Pause: what one line could we add? Flower, open parenthesis, sixty, close parenthesis, at the left edge, below the def, not pushed in. Run again. A blank screen with no error can still be a clue. | A complete function sits unused beside a blank turtle window. Detective scan reaches end-of-file, then one call line connects to the function and drawing begins. **On screen:** Defined ≠ called; No red error can still mean a bug; Add at the left edge: flower(60) | Give a four-second prediction pause before showing the call. Keep all code deterministic. |
| 3:35–4:30 | **Project launch and handoff** | The garden blooms! Functions are your own commands, parameters are their input slots, calls make them run, and random adds surprises inside our limits. Now meet your final project: My Interactive Art Show. It greets the viewer, asks one or two questions, and draws a picture using six ingredients: a question with input, a variable, an if, a loop, something random, and a function you made with def. First, build Flower Stamp and Random Bubble Art. Then fill in your plan sheet. Borrowed an idea? Make it yours, and add a credit comment. Happy coding! | Gallery opens. A project card lists the six ingredients with an icon each; the two exercise cards lead into the plan sheet. **On screen:** PROJECT: My Interactive Art Show; input • variable • if • loop • random • def; Credit borrowed ideas | End with a printable planning-card layout and the voice disclosure. |

**Lesson handoff:** Build Exercise 10.1 Flower Stamp (call the recipe, then add a color parameter) and 10.2 Random Bubble Art. Then fill in the project plan sheet (Milestone M1) and save my_art_show.py with a project name, never a real name.

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
- **Vocabulary:** milestone, iterate, playtest, version, feedback
- **Misconception to prevent:** The fastest way to finish is to type the whole project before running it, or every suggestion must be added.
- **Digital citizenship:** Giving and receiving helpful feedback: be kind, specific and helpful, and make wishes about the program, never the person. When receiving, say thank you, then you decide what to change. Online, if a comment is unkind, don't reply; tell a grown-up.
- **Practice activity:** `1-introduction/project/project-brief.tex`

### Instructional objectives

- Build the final project in small, testable milestones.
- Save useful versions and use a build-run-check cycle.
- Conduct peer testing with normal and unusual safe inputs.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:25 | **Studio hook** | Welcome back to Code Quest! Nova has a brilliant art-show plan, and forty new lines typed without running once. Pixel presses Run. ‘Uh-oh,’ says Nova. One tiny error hides somewhere in the stack. The studio clock is ticking. Would you rather search forty lines, or test each small piece as you build it? Today, we work like project engineers. | Forty code lines form a maze around one tiny bug. The maze transforms into four short, testable stepping stones. **On screen:** STUDIO MISSION; Build small • Test often | Do not imply speed is the goal; frame the clock as choosing a calmer process. |
| 0:25–1:20 | **Plan milestones** | A milestone is a checkpoint you can see and test. Your art show has four. M1, Plan: you finished it last week. M2, Core drawing works: turn the example my_shape function into your own, draw it once, then call it a second time somewhere else, with no red errors. M3, Surprise and polish: add your questions, your if, your loop, something random, and a title. Then a partner tests it. M4 is next week's Showcase. Core first! Extras go on your wish list until the main drawing works. | Project road map with four checkpoints: Plan (checked), Core drawing, Surprise and polish, Showcase. Optional sparkle ideas wait on a wish-list card beside the road. **On screen:** M1 Plan ✓; M2 Core drawing works; M3 Surprise and polish; M4 Showcase | Match milestone language to the project guide; keep optional ideas visually secondary. |
| 1:20–2:25 | **Use build-run-check and versions** | Use a three-beat studio rhythm, like building a LEGO set bag by bag. Build one small change. Run it. Check: did it do what I expected? If something breaks, you know it was the last little change, so look there first. Before a big change, click File, then Save as, and add underscore v2 to the name, like fish_party_v2.py. If the change goes wrong, version one is still safe. A version is a saved checkpoint, not twelve mystery copies named final-final-really-final. | Build, Run, Check triangle rotates slowly. A tidy version ladder replaces chaotic filenames; each rung has a short milestone note. **On screen:** BUILD → RUN → CHECK; Expected vs what happened; Save a _v2 before a big change | Use safe generic paths and filenames. Do not show Git as a student requirement. |
| 2:25–3:35 | **Model peer testing** | Now for the partner swap bug hunt. Swap seats. Run your partner's program twice: once with a normal answer, and once with a strange one, like zero, a giant number, a word instead of a number, or a capital letter. Write down what happened. Don't fix it; just report it! Then swap back and give two stars and a wish: two specific things you liked, and one wish. Make the wish about the program, never the person, like Nova's: ‘I wish the title was bigger.’ The creator says thank you, then decides what to change. It's their art. | Two learners swap seats. A test table fills Normal and Strange rows; two star cards and one wish card cite concrete behaviors. **On screen:** Swap seats • Run twice • Report, don't fix; Normal answer + strange answer; 2 stars + 1 wish (about the program) | Model consent before touching another learner's keyboard and kind neutral facial expressions. |
| 3:35–4:30 | **Safe sharing, recap, and handoff** | Studio checkpoint complete! Milestones keep a big project manageable. Build, run, and check one small change at a time. Save a version before a big change. Test with a normal and a strange answer. Good feedback is kind, specific, and helpful, about the program, never the person. When you get feedback, say thank you, then you decide. Online, if a comment is unkind, don't reply; tell a grown-up. Now: Sprint 1 for M2, the partner swap bug hunt, then Sprint 2 for M3. The goal isn't perfect. It's progress you tested and can explain. Happy coding! | Feedback cards sort into kind, specific, helpful. The studio checklist marks M2, partner swap and M3. **On screen:** Small step • Saved version • Evidence; Kind • Specific • Helpful; NEXT: M2 → Partner swap → M3 | Use a clearly fake desktop without real notifications. Include the voice disclosure. |

**Lesson handoff:** Sprint 1: reach M2 (turn my_shape into your own function and call it twice). Then do the partner swap bug hunt with two stars and a wish. Then Sprint 2: reach M3 (questions, if, loop, random, title).

**Curriculum evidence:**

- `1-introduction/teaching-material/lessons/week11.tex`
- `1-introduction/teaching-material/workbook/week11.tex`
- `1-introduction/teaching-material/homework/week11.tex`
- `1-introduction/project/project-brief.tex`
- `1-introduction/project/project-teacher-guide.tex`
- `1-introduction/project/starter/my_art_show.py`

## Week 12: Showcase and Celebration

- **Driving question:** How can we demonstrate a project and explain the thinking behind it?
- **Planned runtime:** 4:33 (273 seconds)
- **Vocabulary:** showcase, demo, audience, explain, reflection, feedback
- **Misconception to prevent:** A showcase is only entertainment, or a bug encountered during development should be hidden.
- **Digital citizenship:** Showcase safety: projects are shown on the screen only, and nothing is uploaded, posted or emailed. Screens and name cards show nicknames only. Photos of the artwork only if the artist agrees, with no faces or names, and they stay in the family. Say so if you borrowed an idea.
- **Practice activity:** `1-introduction/project/project-brief.tex`

### Instructional objectives

- Prepare a focused two-minute demonstration of the final project.
- Explain one meaningful code choice and one debugging story.
- Reflect on growth and give specific, kind audience feedback.

### Scene-by-scene script

| Time | Purpose | Narration | Visuals and on-screen text | Production notes |
|---|---|---|---|---|
| 0:00–0:28 | **Showcase hook** | Welcome back to Code Quest! All twelve workshop doors open into a gallery. Nova has two minutes to guide visitors through an interactive artwork. ‘Should I show every line of code?’ Nova wonders. No! The best museum guides choose a clear story. What did you make, what should we notice, and what did you learn while building it? | Doors fold into a gallery wall. A two-minute timer appears beside three empty story frames labeled Make, Notice, Learn. **On screen:** FINAL MISSION: Tell your coding story; Make • Notice • Learn | Keep the timer calm and noncompetitive; pause after the guiding question. |
| 0:28–1:23 | **Shape a two-minute demo** | Plan your demo with the script in your workbook. One: ‘Hi! My project is called… It draws…’ Two: invite the visitor to answer your question, then press Run. Three: ‘Because you said rainy, it drew rain. That's my if.’ Four: point to your function or your loop, and say what it does. Five: share one bug you fixed. Six: ask, ‘Do you have a question for me?’ Rehearse once with your partner as the assistant. If it runs long, use fewer words instead of speaking faster. | Six storyboard cards fill a 0:00–2:00 strip with flexible markers. A speedometer stays in a calm zone. **On screen:** 1 Name + what it draws • 2 Visitor answers; 3 That's my if • 4 My function or loop; 5 One bug I fixed • 6 Any questions? | Do not prescribe exact seconds to children; emphasize clarity and flexibility within the two-minute target. |
| 1:23–2:28 | **Explain code and a debugging story** | Showing code isn't reading every symbol. Point to one meaningful part and tell its story, like Nova: ‘This for loop repeats my star function eight times. The function lets one recipe draw different sizes.’ Then tell a bug story with the four detective steps: what I expected, what actually happened, reading line by line, and changing one thing to test again. ‘I expected eight stars, but got seven. I read my loop line by line and saw range seven. I changed it to eight and ran it again.’ A fixed bug shows how you think. It belongs in your story. | A code spotlight highlights only a for-loop and function call. Four detective panels animate the seven-to-eight-star debugging story. **On screen:** Point → Explain → Show result; Expected • Happened • Read • Change one; A fixed bug shows how you think | Use code that matches the project concepts; avoid presenting range(8) as always required. |
| 2:28–3:38 | **Prepare audience feedback and privacy** | Visitors are code explorers, not judges. At each stand, answer the program's question, ask the artist one question, and fill in a feedback card: two stars and a wish. Be specific: ‘The random sizes made each run different. How did you choose the limits?’ Artists may say, ‘I don't know yet,’ and add it to their wish list. Now, the showcase safety check. Projects are shown on the screen only: nothing is uploaded, posted, or emailed. Screens and name cards show nicknames only. Photos of the artwork only if the artist agrees, with no faces or names, and they stay in the family. | Audience cards turn vague praise into a feedback card with two stars and a wish. A privacy shield checks each category, and a camera icon carries the tag ‘Artist agrees • Family only’. **On screen:** Visitor: answer • ask • 2 stars + 1 wish; Nicknames only; On screen only: nothing posted | Do not depict a child being recorded without consent. Use category words, not realistic private data. |
| 3:38–4:33 | **Reflection and celebration** | Level 1 complete! You learned to sequence exact steps, repeat with loops, react to events, choose with conditions, remember with variables, make your own functions, test inputs, and debug like a detective. The short exit quiz isn't pass or fail; it shows what you've learned. Then reflect: What part am I proudest of? Which bug taught me something? What do I want to make next? Rehearse your two-minute demo, run the safety check, and celebrate every creator's progress. The next code quest starts with your curiosity. Happy coding! | All concept badges form a constellation around the learner's project. Three reflection prompts appear with writing space; the gallery doors open toward a blank future map. **On screen:** I'm proudest of…; A bug taught me…; Next I want to make…; SHOWCASE: Rehearse • Check • Share safely | Use warm music with room for applause, five-second reflection hold, and the voice disclosure. |

**Lesson handoff:** Practice the 2-minute demo script with a partner (artist + assistant), do the showcase safety check, present at the gallery walk and fill in feedback cards, take the short exit quiz (not pass or fail), then write the Level 1 reflection (homework 12).

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
(answers and tests excluded)                        │
                                                    v
tracked plan/spec <── deterministic gates <──> scriptwriter agent
       │                 ^                          │
       │                 └──── reviewer agent ──────┘
       v
scene cards / optional illustrations ──> voice provider ──> FFmpeg + captions
       │
       └──> ignored media output and paid-API cache; tracked manifest records curriculum inputs
```

The Python pipeline uses the OpenAI Agents SDK for a typed, traceable three-agent workflow. A curriculum analyst extracts only source-supported outcomes, vocabulary, examples, and safety points, and notes which examples are answers learners must find. A scriptwriter turns that brief into the video contract. Deterministic checks and a reviewer then score each draft; failures go back to the scriptwriter for at most two bounded revisions. Deterministic validators remain the final authority.

### Change and approval flow

1. `check` fingerprints the syllabus, teacher guide, weekly lesson, workbook, homework, public exercise files and project sources (never answers or tests). It names each changed file, per week.
2. A teacher reads the change. If the script still fits, `accept --week N` records the new fingerprints with no paid calls. Otherwise `generate --week N` sends only that week through the agent workflow and refreshes the spec, this plan and that week's fingerprints.
3. A teacher reviews the script and storyboard in the PR. Paid media generation never begins implicitly.
4. `render --voice-provider macos-say` makes a free offline draft (cards, draft voice, captions) for timing review. `render --approved` makes the production version with paid illustrations or narration. Rendering refuses scripts whose lessons have changed.
5. Generated media and API caches remain ignored. Scripts, evidence paths, configuration, and source hashes remain reviewable in Git.

### Commands

```bash
python3 -m venv .venv-videos
source .venv-videos/bin/activate
python -m pip install -r videos/requirements.txt
python -m videos.pipeline.cli check
python -m videos.pipeline.cli accept --week 7          # script still matches a changed lesson
python -m videos.pipeline.cli generate --week 7        # paid: rewrite the script with agents
python -m videos.pipeline.cli render --week 7 --voice-provider macos-say   # free draft
python -m videos.pipeline.cli render --week 7 --approved                   # paid production
```

`OPENAI_API_KEY` is required for agent, illustration, or OpenAI voice calls. `ffmpeg` and `ffprobe` are required for MP4 rendering. Production narration uses the Realtime API (`openai-realtime`), the documented replacement for the Speech API models that shut down on January 6, 2027; its transcript is compared with the script so a paraphrased read is rejected. The legacy `openai-speech` adapter remains available until that date.

### Automated quality gates

- Exactly one episode for each Level 1 week, in order, with stable slugs and scene ids.
- Runtime from 3:00 through 5:00, and every scene's narration within its 145-wpm budget.
- At least two objectives and 4–7 fully specified scenes per episode.
- Evidence files and the practice activity must be part of that week's fingerprinted material; answers and tests never are.
- At most four on-screen text items per scene, each short enough to read; US spelling.
- Human `--approved` gate before paid media calls; refusal to render stale scripts; no automatic publication.
- Caption track plus `.srt` and `.vtt` files timed to the measured narration, voice disclosure, accessible palette, and deterministic code/UI overlays.

### Maintainability decisions

- The JSON spec is the machine-readable source; this Markdown file is reproducible from it.
- Agent prompts and typed output contracts live in code, separate from curriculum content.
- Per-file fingerprints support incremental regeneration and show exactly what changed.
- Media providers are adapters in one registry. Replacing image or voice technology does not change the educational workflow.
- Paid images and narration are cached by their exact inputs, so re-rendering never pays twice.
- Agent traces carry level, week, and source digest metadata for review and troubleshooting.
- The system proposes updates; deterministic checks and a teacher review decide whether they ship.
