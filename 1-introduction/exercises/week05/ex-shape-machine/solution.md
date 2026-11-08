# Teacher reference: Exercise 5.1 - Shape Machine
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 5 (Messages and My Blocks)  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A My Block with inputs is a named recipe: one short line can draw many different shapes.

## The finished project
Setup: new project, Add Extension > Pen, set the cat's Size to 40. My Blocks > Make a Block, name `polygon`, add inputs `sides` and `length` (leave "Run without screen refresh" unticked). Drag the `sides` and `length` ovals out of the define hat into the slots. The "/" block is in Operators.

Sprite: Cat, define script
- define polygon (sides) (length)
- pen down
- repeat (sides)
  - move (length) steps
  - turn right (360 / sides) degrees
- pen up

Sprite: Cat, main script
- when green flag clicked
- erase all
- go to x: 0 y: 0
- point in direction 90
- polygon 3 120
- polygon 4 100
- polygon 6 60
- polygon 8 40

Extra step: add one more block, polygon 5 70, for a pentagon. Save as `shape-machine`.

## What you should see
- Each flag click erases the stage and draws four closed shapes that all start at the middle and hang below and to the right of it.
- A big triangle (sides 120), a square (100), a hexagon (60) and a small octagon (40).
- Adding polygon 5 70 adds a pentagon.
- Question answer: without the My Block each shape needs pen down, repeat, move, turn, pen up (5 blocks), so 4 shapes need about 20 blocks (accept 16 to 20); with it the main script uses 4.

## Talking points
- A My Block is a recipe card with a name; the main script only lists the names, so anyone can read it.
- The inputs are the blanks on the card: "polygon 3 120" and "polygon 6 60" are the same recipe with different numbers.
- 360 divided by the number of sides is the turn that brings you exactly back to the start.

## Common mistakes and quick fixes
- Typing the word `sides` into a slot: the input must be dragged out of the define hat.
- Nothing is drawn: the define block exists but no pink polygon block is used in a script that starts with an event.
- Shape does not close: the turn is a fixed number, not 360 / sides.
- Shapes drawn on top of each other in odd places: go to x: 0 y: 0 or point in direction 90 is missing.
- Old shapes stay on the stage: "erase all" is missing.

## Check-off list
- [ ] I made a My Block called `polygon` with the inputs `sides` and `length`: the define hat shows both inputs.
- [ ] I dragged the inputs from the define hat (I did not type them): the ovals are round, colored blocks.
- [ ] My turn uses 360 / sides: look at the turn block.
- [ ] My green-flag script uses the polygon block at least 4 times with different numbers.
- [ ] I saved my project: file `shape-machine`.
