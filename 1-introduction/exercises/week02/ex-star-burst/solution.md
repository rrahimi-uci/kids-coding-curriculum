# Teacher reference: Exercise 2.3 - Star Burst
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 2  **Kind:** Scratch (offline app, Pen extension)  **Time:** about 8 minutes
**Big idea:** A loop with a small change inside it (a turn and a color step) can make beautiful art.

## The finished project
Sprite: Cat (small, Size 40, as in Exercise 2.2)
- when green flag clicked
- erase all
- go to x: -75 y: 0
- point in direction 90
- pen down
- repeat (36)
  - move (150) steps
  - turn right (170) degrees
  - change pen color by (5)
- pen up

Setup: use the Polygon Party project or a new project with the Pen extension added. "change pen color by" is in Pen. Save as `star-burst`.

## What you should see
- 36 long lines criss-cross to make a round, spiky star about 150 steps wide, near the middle of the stage.
- The color of the lines changes a little after every line, like a rainbow.
- The cat ends where it started, at x: -75 y: 0. Check: 36 x 170 = 6120 degrees, which is 17 whole turns, so the path closes.

## Talking points
- "Each line is the same length, and each turn is almost a U-turn. Thirty-six of them make a star."
- "The color block is inside the loop, so the color changes after every line. Outside the loop it would change once."
- "Change one number at a time and predict what happens."

## Common mistakes and quick fixes
- The star is lopsided or off the stage: the go to x: -75 y: 0 block is missing, so it starts wherever the cat was.
- The lines are all one color: "change pen color by" is outside the repeat or missing.
- A messy picture: erase all or point in direction 90 is missing, so old drawings stay or the angle is different.
- No lines at all: pen down is missing or the Pen extension was not added.
- The picture is a plain shape, not a spiky star: the turn is far from 170 (a turn that divides evenly into 360 gives a simple shape). Set it back to 170.

## Check-off list
- [ ] Star has lots of spiky points (36 lines) and is near the middle of the stage: check the repeat number (36) and look at the picture.
- [ ] Color changes as it draws: the lines go through different colors.
- [ ] Tried at least one set of own numbers: ask which ones.
- [ ] Wrote favorite numbers in the workbook: look at the page.
- [ ] Saved as `star-burst`.

## Extension answers
Step 4 is open-ended: any numbers are fine. Good discoveries to praise: turns close to 180 make spiky stars; turns that divide evenly into 360 make simple shapes; a small move with a small turn makes a circle (for example repeat 36, move 10, turn 10).
