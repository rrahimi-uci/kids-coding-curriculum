# Teacher reference: Exercise 5.2 - Bug-Hunt Relay (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 5 (Play Day and Show Me)  **Kind:** Scratch (offline app), bug hunt relay  **Time:** about 12 minutes (about 4 per leg)
**Big idea:** Test, look, change one thing (then test again): the detective steps from week 3 fix every kind of bug.

## The finished project
Setup: File > New for each leg. Keep the cat. Build the leg exactly as printed in the workbook, with the bug, then fix it.

Leg 1, The Quiet Cat (after the fix), Sprite1 (the cat)
- when green flag clicked
- say Hi! for 2 seconds
- play sound Meow until done

Leg 2, Bye Before Hi (after the fix), Sprite1 (the cat)
- when green flag clicked
- say Hi! for 2 seconds
- say Bye! for 2 seconds

Leg 3, Too Many Meows (after the fix), Sprite1 (the cat)
- when green flag clicked
- repeat 3
  - play sound Meow until done

## What you should see
- Leg 1: with the bug, "Hi!" and silence. After the fix, "Hi!" for 2 seconds, then a meow.
- Leg 2: with the bug, "Bye!" then "Hi!". After the fix, "Hi!" then "Bye!", 2 seconds each.
- Leg 3: with the bug, ten meows in a row. After the fix, three meows.

## Bug-hunt answer
- Leg 1: "play sound Meow until done" is not snapped on, so it is not part of the script. Fix: drag it until it clicks on under the say block. (Revisits week 2.)
- Leg 2: the say blocks are in the wrong order. Fix: drag the bottom block, "say Hi!", and drop it right under the green flag block; it clicks in above "say Bye!". (Revisits week 3.)
- Leg 3: the repeat number is wrong. Fix: change 10 to 3. (Revisits week 4.)

## Talking points
- The detective steps from week 3: test, look, change one thing, then test again.
- The "should do" line is the plan. A bug is any place where the project does something different from the plan.
- Too Many Meows links to the Share talk: sounds that go on too long are not fun for everyone.

## Common mistakes and quick fixes
- In leg 2 the child drags the top say block: every block under it comes along. Show that dragging the bottom block moves only that one.
- In leg 3 the child adds a second repeat or deletes blocks: ask "Which number says how many times?"
- The child "fixes" the leg before testing it: ask them to rebuild the bug first and click the flag, so they practice spotting it.
- Ten meows are loud: the red stop sign stops them. Turn the volume down before the relay.

## Check-off list
- [ ] Leg 1 fixed: dragging the green flag block moves both blocks, and the cat meows after "Hi!".
- [ ] Leg 2 fixed: "Hi!" comes first, then "Bye!".
- [ ] Leg 3 fixed: the repeat says 3 and you count three meows.
- [ ] The child tested before and after each fix.
