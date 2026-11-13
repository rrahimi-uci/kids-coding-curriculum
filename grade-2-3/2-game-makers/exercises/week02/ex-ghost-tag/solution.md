# Teacher reference: Exercise 2.3 - Ghost Tag (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 2 (If Touching...)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 7 minutes
**Big idea:** An if outside a forever loop checks only once, at the start. To keep checking, the if must be inside the loop.

## The finished project
Setup: File > New. Add the Ghost and the Ballerina with the "Choose a Sprite" button. Build the buggy version from the workbook in the Ghost's code first. Drag the Ballerina to the same height as the ghost, to one side. (Support path: build it yourself before the session.)

Sprite: Ghost, after the fix
- when green flag clicked
- point in direction 90
- set rotation style left-right
- forever
  - move 5 steps
  - if on edge, bounce
  - if touching Ballerina? then
    - say Got you! for 1 seconds

Sprite: Ballerina
- (no scripts)

## What you should see
- With the bug: the ghost flies from side to side, straight through the Ballerina, and never says anything.
- After the fix: each time the ghost reaches the Ballerina, it stops and says "Got you!" for 1 second, then flies on. It may say it two or three times while passing through her.

## Bug-hunt answer
- The "if touching Ballerina? then" block is above the forever. It runs once, right after the flag, when the ghost is far from the Ballerina, so the answer is no and the say block is skipped. It never asks again.
- Fix: drag the if into the forever, under "if on edge, bounce". (Above the move, inside the forever, also works.)

## Talking points
- Link to the warm-up: the once-only robot looked once, at the start, and missed the star.
- Questions that can change during a game belong inside the forever.
- A good test: put the Ballerina in the ghost's path, watch, and ask "what did I expect? what happened?"

## Common mistakes and quick fixes
- Only the say block is moved into the forever, leaving the if empty above: the ghost says "Got you!" all the time. Move the whole if.
- The Ballerina is not in the ghost's path: the ghost never touches her, even after the fix. Drag her to the ghost's height.
- The touching menu says Sprite1: that is the cat. Pick Ballerina.
- The script is built in the Ballerina's code: the Ballerina flies instead. Drag the script onto the Ghost in the sprite list.

## Check-off list
- [ ] The if is inside the forever, with the say block inside the if.
- [ ] The touching menu says Ballerina.
- [ ] The ghost says "Got you!" every time it reaches the Ballerina.
- [ ] The child can say why the old if checked only once.
