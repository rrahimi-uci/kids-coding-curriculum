# Teacher reference: Exercise 1.2 - Square Flower
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 1 (Patterns in Patterns)  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A My Block can hide a repeat. Using the block inside another repeat is still a repeat inside a repeat, and it keeps the main script short.

## The finished project
Setup: keep the Window project from Exercise 1.1 (Pen extension already added). Keep the cat.

Sprite: Sprite1 (the cat), My Block
- define square
- repeat 4
  - move 60 steps
  - turn right 90 degrees

Sprite: Sprite1 (the cat), main script
- when green flag clicked
- set size to 40 %
- point in direction 90
- erase all
- pen down
- repeat 6
  - square
  - turn right 60 degrees
- pen up

## What you should see
- The cat draws one square, turns a little, draws the next square, and so on: six squares.
- All six squares share the start point, so they overlap like petals around the middle of a flower.
- The cat ends where it started, facing right again (six turns of 60 make one full spin, read from the turn card; children do not need to work this out).

## Talking points
- The My Block is a name for a group of steps, like "do the chorus" in a song.
- Ask: "Where is the inside repeat now?" (Under "define square".) It is still a repeat inside a repeat.
- The 6 and the 60 go together on the turn card. Other pairs that close the flower: 4 and 90, 3 and 120.

## Common mistakes and quick fixes
- "define square" has nothing under it: the cat only turns and draws nothing. Snap the repeat 4 under the define block.
- The child drags "define square" into the flag script: it will not snap. The define block stays on its own; the round-ish "square" block from the palette goes in the script.
- The old nested repeats are still in the flag script: the cat draws a window and then the flower. Delete the old repeats.
- Turn 90 instead of 60 in the outside repeat: four of the six squares land on top of each other. Read the turn card again.
- The flower runs off the stage: drag the cat to the middle, or change 60 steps to 40.

## Check-off list
- [ ] A "define square" block with repeat 4 of move 60 and turn 90 under it.
- [ ] The flag script has repeat 6 with "square" and "turn 60" inside.
- [ ] Clicking the flag draws six squares around the middle, like a flower.
