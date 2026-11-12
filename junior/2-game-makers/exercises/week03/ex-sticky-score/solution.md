# Teacher reference: Exercise 3.3 - The Sticky Score (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 3 (Keep Score)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 7 minutes
**Big idea:** "set" puts a new number in a variable; "change" adds to the number already there. Every new game must set the score back to 0.

## The finished project
Setup: save the catch game first, then File > New. Make a variable "score", For all sprites. Add Bananas with the "Choose a Sprite" button. Build the buggy version from the workbook in the Bananas' code. (Support path: build it yourself before the session.)

Sprite: Bananas, after the fix
- when green flag clicked
- set score to 0

- when this sprite clicked
- change score by 1
- start sound Pop

## What you should see
- With the bug: flag, three clicks: score 3. Flag again: still 3. The next click makes 4. The score is "sticky".
- After the fix: flag gives 0; each click on the bananas adds 1 with a pop; the flag always brings it back to 0.

## Bug-hunt answer
- The green-flag script uses "change score by 0". Changing by 0 adds nothing, so the old score stays.
- Fix: drag "change score by 0" back to the block list to delete it, and snap "set score to 0" under the green flag.

## Talking points
- Link to the warm-up: the SCORE box was not emptied before the next player.
- Fair scoring: a score that does not reset gives the next player someone else's points.
- Test like a player: play two games in a row, not only one. Some bugs only show up the second time.

## Common mistakes and quick fixes
- The child changes 0 to another number in the change block: the score then jumps at the start of each game. Ask: "Do we want to add, or start fresh?"
- The variable in a new project is missing: Kai's blocks show "my variable" instead. Make score first, then pick it in each menu.
- The child adds "set score to 0" to the click script: the score then never gets past 1. Put it under the green flag only.
- Dragging the bananas instead of clicking: a quick click, without moving the mouse.

## Check-off list
- [ ] "set score to 0" under the green flag; no "change score by 0" left.
- [ ] "change score by 1" and the pop under "when this sprite clicked".
- [ ] Two games in a row both start at 0.
- [ ] The child can say how set and change differ.
