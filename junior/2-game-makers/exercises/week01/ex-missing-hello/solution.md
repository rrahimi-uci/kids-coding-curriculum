# Teacher reference: Exercise 1.3 - The Missing Hello (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 1 (Forever and Bounce)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 7 minutes
**Big idea:** A forever loop never ends, so blocks placed after it never get their turn. Scratch shows this with a flat bottom on the forever block.

## The finished project
Setup: File > New (or keep the Bounce Cat project and change its script). Keep the cat. Build the buggy version from the workbook first. (Support path: build it yourself before the session.)

Sprite: Sprite1 (the cat), after the fix
- when green flag clicked
- say Watch me! for 2 seconds
- start sound Meow
- forever
  - move 10 steps
  - if on edge, bounce

## What you should see
- With the bug: the cat bounces from side to side. No speech bubble, no meow. The say and sound blocks sit loose under the forever.
- After the fix: the cat stands still and says "Watch me!" for 2 seconds, then meows as it starts to run, then bounces until the red stop sign is clicked.

## Bug-hunt answer
- The say and sound blocks are under the forever loop. They cannot snap on (forever has no bump at the bottom), and even if they could, the loop never finishes, so they would never run.
- Fix: drag both blocks up and snap them between "when green flag clicked" and "forever".

## Talking points
- Link to the warm-up: "Dance until the music stops, then eat a cookie. But the music never stops: no cookie!"
- Blocks for the start of a game go above the forever; blocks that happen all the time go inside.
- A loose block is a Level 1 bug too: a block that is not snapped on never runs.

## Common mistakes and quick fixes
- Putting the say and sound inside the forever: the cat stops every few steps to say "Watch me!" and meows again and again. Ask: "Should it say this once or all the time?"
- Dragging the forever away from the hat block while fixing: snap it back under the sound block.
- The cat walks upside down: this script has no rotation style. Not part of the bug; add "set rotation style left-right" above the forever if the child wants.

## Check-off list
- [ ] Say and sound blocks are between the green flag block and the forever.
- [ ] Nothing loose is left in the code area.
- [ ] The cat talks, meows, then bounces until stop.
- [ ] The child can say why blocks under a forever never run.
