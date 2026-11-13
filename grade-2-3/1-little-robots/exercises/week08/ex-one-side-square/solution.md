# Teacher reference: Exercise 8.2 - The One-Side Square (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 8 (Draw With the Pen)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 6 minutes
**Big idea:** Only the blocks inside a repeat are done again; a turn outside the repeat happens once.

## The finished project
Setup: the Pen extension is added (Add Extension > Pen).

Sprite: Sprite1 (the cat), after the fix
- when green flag clicked
- erase all
- pen down
- repeat 4
  - move 100 steps
  - turn ↻ 90 degrees

## What you should see
- With the bug: the cat draws one long straight line to the right (100 steps four times; it stops at the edge of the stage), then turns once and faces down.
- After the fix: the cat draws a square with four sides and ends where it started.

## Bug-hunt answer
The bug is "turn ↻ 90 degrees" sitting under the repeat instead of inside it. The repeat only does "move 100 steps" four times, so there is one long line, then one turn. Fix: drag the turn up into the repeat, under the move.

## Talking points
- Link to the warm-up: when the quarter-turn card was outside the repeat card, the robot walked 12 steps in a straight line.
- Testing tip: count out loud while the cat draws. "One side, turn. Two sides, turn..." helps find where it goes wrong.

## Common mistakes and quick fixes
- The turn lands above the move inside the repeat: that still draws a square (it turns first, then moves). Praise it, then read the script top to bottom together.
- The cat faces down after the buggy run: the next square still works. To reset, snap "point in direction 90" (Motion) under the green flag.
- The line runs off the stage: drag the cat back and click the flag again.

## Check-off list
- [ ] The child says the turn was outside the repeat: they point to it.
- [ ] The turn is now inside "repeat 4": dragging the repeat moves the turn with it.
- [ ] The cat draws four sides after the fix: watch one run.
