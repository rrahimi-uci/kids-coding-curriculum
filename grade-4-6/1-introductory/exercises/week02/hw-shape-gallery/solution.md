# Teacher reference: Homework 2 - Shape Gallery
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introductory), Week 2  **Kind:** Scratch (offline app, Pen extension)  **Time:** about 10 minutes
**Big idea:** Pen up before you move means you can travel without drawing, so separate shapes stay separate.

## The finished project
Sprite: Cat (Size 40)
- when green flag clicked
- erase all
- point in direction 90
- pen up
- go to x: -200 y: 50
- pen down
- repeat (3)
  - move (80) steps
  - turn right (120) degrees
- pen up
- go to x: -60 y: 50
- pen down
- repeat (4)
  - move (80) steps
  - turn right (90) degrees
- pen up
- go to x: 80 y: 50
- pen down
- repeat (6)
  - move (50) steps
  - turn right (60) degrees
- pen up

Setup: Add Extension > Pen. The two missing hexagon numbers are repeat 6 and turn 60 (360 / 6). Save as `shape-gallery`.

## What you should see
- The stage is cleared, then three closed shapes appear in a row near the top: a triangle on the left, a square in the middle and a hexagon on the right.
- No lines join the shapes.
- Each shape hangs below and to the right of its start point, because the cat turns right. They do not overlap.

## Talking points
- "Pen up is like lifting a marker off the paper so you can move without drawing."
- "Each shape is the same recipe with different numbers: repeat = sides, turn = 360 / sides."
- "Predict the hexagon before you click: how many sides, and how big is each turn?"

## Common mistakes and quick fixes
- A line joins two shapes: pen up is missing before a go to block. Add pen up after each shape.
- The hexagon is open or has a gap: the turn is not 60, or the repeat is not 6.
- All shapes start from the same place: a go to block is missing.
- A shape is only a line: move and turn are not both inside the repeat.
- Old drawings stay on screen: erase all is missing at the top.

## Check-off list
- [ ] Used **repeat** for every shape: three repeat blocks (3, 4 and 6).
- [ ] Every shape closes: the end meets the start.
- [ ] No lines join the shapes: pen up comes before each go to.
- [ ] Hexagon uses repeat 6 and turn 60.
- [ ] Saved as `shape-gallery`.
