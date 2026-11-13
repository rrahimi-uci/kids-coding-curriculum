# Teacher reference: Exercise 1.1 - Bounce Cat
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 1 (Forever and Bounce)  **Kind:** Scratch (offline app)  **Time:** about 7 minutes
**Big idea:** A forever loop keeps going until you press stop. "if on edge, bounce" turns the sprite around at the edge so it can keep moving.

## The finished project
Setup: File > New. Keep the cat.

Sprite: Sprite1 (the cat)
- when green flag clicked
- point in direction 90
- set rotation style left-right
- forever
  - move 10 steps
  - if on edge, bounce

## What you should see
- After the flag: the cat runs right, reaches the edge, turns to face left and runs back, and so on, quickly, until the red stop sign is clicked.
- It never walks upside down, because the rotation style is left-right (it flips to face left instead of turning over).

## Talking points
- Forever never stops by itself: who stopped the cat? We did, with the stop sign. Link to the freeze dance.
- Point at the flat bottom of the forever block: nothing can go after it.
- Repeat from Level 1 counts and stops; forever does not count.
- Without "if on edge, bounce", Scratch stops the cat at the edge and it runs on the spot.

## Common mistakes and quick fixes
- The cat sticks at the edge: "if on edge, bounce" is missing or outside the forever.
- The cat walks upside down after the first bounce: add "set rotation style left-right", then click "point in direction 90" once to turn it back.
- The cat only moves a little: "move 10 steps" is above the forever instead of inside it.
- The cat moves in a slanted line: an old turn from Level 1 is left over. "point in direction 90" at the start fixes it.
- Clicking the flag again and again: show the red stop sign next to it.

## Check-off list
- [ ] Green flag hat block on top.
- [ ] "point in direction 90" and "set rotation style left-right" above the forever.
- [ ] "move 10 steps" and "if on edge, bounce" inside the forever.
- [ ] The child stops the project with the red stop sign.
