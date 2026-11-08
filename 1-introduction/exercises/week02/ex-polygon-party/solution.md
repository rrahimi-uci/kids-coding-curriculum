# Teacher reference: Exercise 2.2 - Polygon Party
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introduction), Week 2  **Kind:** Scratch (offline app, Pen extension)  **Time:** about 10 minutes
**Big idea:** To draw a closed shape with repeat, all the turns must add up to one full turn, so turn = 360 / sides.

## The finished project
Sprite: Cat (set Size to 40 in the sprite pane so the lines are easy to see)
- when green flag clicked
- erase all
- go to x: 0 y: 0
- point in direction 90
- pen down
- repeat (4)
  - move (100) steps
  - turn right (90) degrees
- pen up

Setup: click Add Extension (blue button, bottom left) and choose Pen. Tip: the turn slot can hold the Operators block ( (360) / (4) ) so Scratch does the dividing. Save as `polygon-party`.

Table (repeat = number of sides, turn = 360 / sides):
- Triangle: repeat 3, turn 120
- Square: repeat 4, turn 90
- Pentagon: repeat 5, turn 72
- Hexagon: repeat 6, turn 60

## What you should see
- Each flag click erases the old drawing and draws one closed shape that ends exactly where it started.
- The square has 4 equal sides of 100 steps. It starts in the middle and hangs below and to the right of the center (the cat turns right).
- The triangle has 3 sides, the pentagon 5, the hexagon 6.

## Bug-hunt answers
- Where: Leo's triangle script, repeat 3, move 100, turn 60.
- What goes wrong: it draws three sides of a hexagon, an open bowl-like shape that does not close.
- Why: 60 degrees is the turn for 6 sides. The three turns add up to only 180, not 360.
- Fix: change the turn to 120 (360 / 3).

## Talking points
- "Walk it on the floor: walk 4 steps, turn right a quarter turn, four times. You turned all the way round once, which is 360 degrees."
- "Four turns share 360 equally, so each is 360 / 4 = 90. Three turns: 360 / 3 = 120, a big sharp turn."
- "Before you click, predict the shape out loud."

## Common mistakes and quick fixes
- Child uses the inside corner angle (60 for a triangle): the sprite turns by how much it changes direction. Use 360 / sides.
- Only one long line is drawn: "turn" is below the repeat instead of inside it. Drag it into the mouth of the repeat.
- Drawings pile up or start in odd places: erase all, go to and point in direction are missing at the top.
- The shape does not close (turn 80 instead of 90 and so on): the turns do not add up to 360.
- No lines appear: pen down is missing, or the Pen extension was not added.
- Only part of the shape is drawn: the repeat number is not equal to the number of sides.

## Check-off list
- [ ] Added the Pen extension: a green Pen category is in the block list.
- [ ] **move** and **turn** are both inside the **repeat**.
- [ ] Square, triangle, hexagon and pentagon all close: the end touches the start.
- [ ] Can explain Leo's bug: 60 is for 6 sides, so use 120.
- [ ] Saved as `polygon-party`.
