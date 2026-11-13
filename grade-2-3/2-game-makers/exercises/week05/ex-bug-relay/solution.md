# Teacher reference: Exercise 5.2 - Bug-Hunt Relay (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 5 (Play Day and Show Me)  **Kind:** Scratch (offline app), bug hunt relay  **Time:** about 13 minutes (about 4 per leg)
**Big idea:** Test, look, change one thing (then test again) fixes loop bugs, if bugs and score bugs alike.

## The finished project
Setup: File > New for each leg. Keep the cat. For leg 2 add the Ghost and make a "score" variable (For all sprites). For leg 3 add the Apple and drag it away from the cat. Build each leg as printed, with the bug, then fix it.

Leg 1, Stuck at the Edge (after the fix), Sprite1 (the cat)
- when green flag clicked
- set rotation style left-right
- forever
  - move 10 steps
  - if on edge, bounce

Leg 2, The Stuck Score (after the fix), Ghost
- when green flag clicked
- set score to 0

- when this sprite clicked
- change score by 1
- start sound Pop

Leg 3, The Apple That Won't Pop (after the fix)

Sprite1 (the cat)
- when green flag clicked
- forever
  - go to mouse-pointer

Apple
- when green flag clicked
- forever
  - if touching Sprite1? then
    - start sound Pop
    - go to random position

## What you should see
- Leg 1: with the bug, the cat walks to the right edge and stops there. After the fix, it walks back and forth forever, the right way up (the rotation style block from week 1 does that).
- Leg 2: with the bug, the score shows 1 after every click. After the fix, 1, 2, 3 and so on; the flag puts it back to 0.
- Leg 3: with the bug, the cat follows the mouse but touching the Apple does nothing. After the fix, a pop and the Apple jumps to a surprise place every time the cat touches it.

## Bug-hunt answer
- Leg 1: "if on edge, bounce" is above the forever, so it runs once at the start (week 1 and week 2 idea: what runs once, what runs again and again). Fix: drag the forever away, drop the bounce block into the forever under move, snap the forever back on.
- Leg 2: "set score to 1" instead of "change score by 1" (week 3). Fix: drag the set block out and put "change score by 1" in its place, above "start sound Pop".
- Leg 3: the touching block checks "edge" instead of the cat (week 2). Fix: pick Sprite1 in the dropdown. The dropdown lists the other sprites by their names in the sprite list.

## Talking points
- Each leg is a different kind of bug: a loop bug, a score bug and an if bug. The detective steps work for all three.
- Leg 3 is the start of Exercise 5.3: a fixed game becomes your own game.
- Kind words when a partner finds the bug: "You found it!" or "Good detective work!"

## Common mistakes and quick fixes
- Leg 1: dragging the bounce block drags the forever too. Take the forever away first.
- Leg 1: the cat is upside down after a bounce: the "set rotation style left-right" block was left out. Snap it under the green flag block and click "point in direction 90" once.
- Leg 2: the child changes 1 to another number in the set block. Ask: "Which block adds one more?"
- Leg 3: the cat jumps to the mouse but does not follow it: "go to mouse-pointer" is not inside the forever.
- Leg 3: the Apple pops by itself at the edges with the bug: it landed on an edge. That is a clue that the if checks the edge.

## Check-off list
- [ ] Leg 1 fixed: the bounce block is inside the forever and the cat walks back and forth.
- [ ] Leg 2 fixed: "change score by 1" and the score counts up.
- [ ] Leg 3 fixed: the touching block says Sprite1 and the Apple pops.
- [ ] The child tested before and after each fix.
