# Teacher reference: Exercise 7.2 - Boo at Once (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 7 (Two Sprites Talk)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 6 minutes
**Big idea:** All green-flag scripts start at the same moment. Without a wait, two sprites talk at the same time.

## The finished project
Setup: File > New. Keep the cat. Add the Ghost ("Choose a Sprite") and drag it away from the cat. A backdrop is optional.

Sprite: Sprite1 (the cat)
- when green flag clicked
- say Who is there? for 2 seconds

Sprite: Ghost, after the fix
- when green flag clicked
- wait 2 seconds
- say Boo! for 2 seconds

## What you should see
- With the bug: both bubbles, "Who is there?" and "Boo!", appear at the same moment.
- After the fix: "Who is there?" for 2 seconds, then "Boo!" for 2 seconds.

## Bug-hunt answer
The bug is a missing wait. The Ghost talks second, so its script needs "wait 2 seconds" (orange Control) right under its green flag block. In the workbook, the arrow should point to that spot in the Ghost's script.

## Talking points
- Link to the warm-up: both children talked at once until one had a WAIT 2 card.
- Why does the cat not need a wait? It talks first.
- Testing tip: watch for what happens at the same time, not only what happens.

## Common mistakes and quick fixes
- The wait goes into the cat's script: the Ghost says "Boo!" first and spoils the joke. Ask "Who talks second?"
- The wait is snapped under the say block: the Ghost still talks at once. Drag the wait above the say block.
- wait 1 seconds: the bubbles overlap for a moment. Make the wait as long as the cat's line (2).
- The Ghost's script was built in the cat's code: check the blue frame in the sprite list.

## Check-off list
- [ ] The child says what was wrong: "They talk at the same time."
- [ ] The Ghost's script starts with wait 2 seconds; the cat's script has no wait.
- [ ] After the flag, the cat talks first, then the Ghost: watch one run.
