# Teacher reference: Exercise 2.1 - Walking Cat
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introductory), Week 2  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** A forever loop repeats steps until you stop it, and a short wait makes each frame visible.

## The finished project
Sprite: Cat (the cat has 2 costumes)
- when green flag clicked
- set rotation style [left-right]
- forever
  - move (10) steps
  - next costume
  - if on edge, bounce
  - wait (0.1) seconds

Setup: no extension. Costumes tab shows 2 costumes; switching between them looks like walking. "set rotation style" and "if on edge, bounce" are in Motion, "forever" and "wait" are in Control, "next costume" is in Looks. Save as `walking-cat`.

## What you should see
- After the flag the cat walks across the stage, moving its legs (it flips between its 2 costumes every 0.1 seconds).
- At the edge it turns round and stays the right way up, then walks back.
- It keeps going until the red stop sign is clicked.
- Without the wait block: the cat zooms and the legs flicker so fast the walk looks blurry. Putting the wait back fixes it.

## Talking points
- "A loop is like running laps. Forever is like a hamster wheel: it keeps going until someone stops it."
- "Why does the cat need a wait? Each costume needs a moment on screen so our eyes can see it."
- "Rotation style left-right means the cat flips like a mirror and does not turn upside down."

## Common mistakes and quick fixes
- The cat walks upside down after bouncing: "set rotation style left-right" is missing. This is a good bug to discuss, not a fail.
- The legs do not move: "next costume" is outside the forever loop, or is missing.
- The cat flickers and zooms: no wait block (or the wait is outside the loop). Put wait 0.1 inside the loop.
- The cat will not stop: forever never ends by itself. Click the red stop sign.
- The cat walks off the stage and sticks at the edge: "if on edge, bounce" is outside the loop or missing.
- Blocks are not snapped under the hat block: drag until the gray shadow appears.

## Check-off list
- [ ] Script uses a **forever** loop: the C-shaped block wraps the blocks inside it.
- [ ] **next costume** is inside the loop, so the legs move.
- [ ] The cat turns round at the edge and is not upside down: watch it bounce.
- [ ] Tried it without **wait** and can say what changed: it zooms and flickers.
- [ ] Saved as `walking-cat`.
