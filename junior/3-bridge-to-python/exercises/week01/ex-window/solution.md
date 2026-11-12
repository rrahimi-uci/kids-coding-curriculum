# Teacher reference: Exercise 1.1 - The Window
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 1 (Patterns in Patterns)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** A repeat inside a repeat runs the whole inside pattern each time the outside repeat goes round once. Four squares with a quarter turn between them make a window.

## The finished project
Setup: File > New. Keep the cat. Add the Pen extension (Add Extension, bottom left, then Pen).

Sprite: Sprite1 (the cat)
- when green flag clicked
- set size to 40 %
- point in direction 90
- erase all
- pen down
- repeat 4
  - repeat 4
    - move 60 steps
    - turn right 90 degrees
  - turn right 90 degrees
- pen up

## What you should see
- The cat draws a square to the lower right of its start point, then one to the lower left, then the upper left, then the upper right.
- The four squares share the middle corner and look like one big square window with four panes.
- The cat ends in the middle, facing right. Clicking the flag again erases and redraws the same window.

## Talking points
- Link to the clap pattern: the inside repeat is the (clap, clap, stomp) part; the outside repeat is the part with the jump.
- Count together: 4 squares, and 4 lines in each square. The cat really drew 16 lines.
- The last turn decides where the next square goes. Without it, all four squares land on top of each other.

## Common mistakes and quick fixes
- The last turn is missing or ends up inside the inside repeat: without it, the cat draws the same square four times (it looks like one square); inside it, each move is followed by a half turn and the cat draws one short line. Drag the turn so the gray shadow is under the inside repeat.
- No green Pen circle: add the Pen extension.
- Lines from earlier tries stay on the stage: "erase all" is missing from the top of the script.
- The window is cut off: drag the cat to the middle of the stage before clicking the flag.
- The cat starts tilted from earlier play: "point in direction 90" fixes it; check it is snapped on.

## Check-off list
- [ ] One repeat 4 is inside another repeat 4.
- [ ] Inside: move 60 and turn 90. Between: one more turn 90.
- [ ] Pen down before the repeats, pen up after.
- [ ] Clicking the flag draws a window of four squares.
