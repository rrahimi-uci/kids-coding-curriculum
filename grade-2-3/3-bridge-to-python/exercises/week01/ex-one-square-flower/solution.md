# Teacher reference: Exercise 1.3 - The One-Square Flower (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 1 (Patterns in Patterns)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 8 minutes
**Big idea:** Where a block sits matters. A repeat placed under another repeat runs once, after it; a repeat placed inside another repeat runs every time round.

## The finished project
Setup: File > New. Keep the cat. Add the Pen extension. Build the buggy version from the workbook first. (Support path: build it yourself before the session.)

Sprite: Sprite1 (the cat), after the fix
- when green flag clicked
- erase all
- pen down
- repeat 6
  - repeat 4
    - move 60 steps
    - turn right 90 degrees
  - turn right 60 degrees

## What you should see
- With the bug: the cat spins on the spot (too fast to notice, and no line because it does not move), then draws one square to the lower right of where it stands.
- After the fix: six squares that share the start point, like petals: the same flower as Exercise 1.2.

## Bug-hunt answer
- The "repeat 4" (the square) is snapped under the "repeat 6", not inside it. So the outside repeat holds only the turn, and the square is drawn once at the end.
- Fix: drag the "repeat 4" up into the mouth of the "repeat 6", above the turn 60. Dragging a repeat also brings the blocks inside it, so the square stays in one piece.

## Talking points
- Link to the warm-up: a card left outside the big REPEAT card is done only once.
- Read the script with your finger: "repeat 6: turn. Done. Then repeat 4: square." Children often hear the bug when they read it aloud.
- Same blocks, different places, different picture. Order and nesting are part of the program.

## Common mistakes and quick fixes
- The child drags only "move 60 steps" into the repeat 6: the blocks come apart. Put the move back (or right-click the code area and choose Undo) and drag the repeat 4 by its top edge.
- The repeat 4 lands under the turn 60 inside the repeat 6: still a flower, only rotated. That is fine.
- The cat was facing another way from earlier play: the flower is tilted but correct. Add "point in direction 90" at the top if you want it straight.
- Nothing is drawn: "pen down" is missing, or the Pen extension was not added in this new project.

## Check-off list
- [ ] The child saw one square with the buggy script.
- [ ] The repeat 4 now sits inside the repeat 6.
- [ ] Clicking the flag draws six squares like a flower.
