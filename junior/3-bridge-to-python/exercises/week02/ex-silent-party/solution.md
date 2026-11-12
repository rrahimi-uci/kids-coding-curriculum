# Teacher reference: Exercise 2.3 - The Silent Party (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 3, Week 2 (Plan It on Paper)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 7 minutes
**Big idea:** Parts can each pass their own test and still fail together. After testing each part, test the parts together, and look first where they meet.

## The finished project
Setup: the Party Time project from Exercise 2.2. The child changes the cat's broadcast to a new message called "party" to make Leo's buggy version.

Sprite: Sprite1 (the cat), after the fix
- when green flag clicked
- set pops to 0
- say Party time! for 2 seconds
- broadcast balloons

Sprite: Balloon1 (unchanged)
- when green flag clicked
- hide

- when I receive balloons
- go to random position
- show

- when this sprite clicked
- start sound Pop
- change pops by 1
- go to random position

## What you should see
- With the bug: clicking the cat's script makes it say "Party time!" (Part 1 passes). Clicking the balloon's "when I receive balloons" script shows the balloon (Part 2 passes). But the green flag hides the balloon, the cat says "Party time!", and then nothing: the balloon never comes.
- After the fix: the green flag runs the whole party, as in Exercise 2.2.

## Bug-hunt answer
- The cat sends "party" but the balloon waits for "balloons". A message only reaches scripts whose "when I receive" uses exactly the same name.
- Fix: click the arrow on the cat's broadcast block and choose "balloons". (Changing the balloon's hat block to "party" also works; then both say "party".)

## Talking points
- Link to the warm-up: the invitations said 3 o'clock and the food list said 4 o'clock. Each part was fine; together they did not fit.
- Testing each part is the first test. Testing the parts together is the second test. Both go on the plan card.
- In week 9 (project studio) partners check each other's build against the plan card: the same idea.

## Common mistakes and quick fixes
- The child fixes the bug by deleting the broadcast and adding "when green flag clicked" to the balloon: the balloon then appears at once, before "Party time!". Not the plan; put the message back.
- The child types "balloons " with a space or "baloons": it is a new, different message. Pick the existing name from the dropdown instead of typing.
- The balloon is still hidden from an earlier test: click "show" in purple Looks, then test with the flag.

## Check-off list
- [ ] The child tested each part alone and saw that both parts work.
- [ ] The child found the mismatched message names.
- [ ] Broadcast and "when I receive" now use the same name.
- [ ] The green flag runs the whole party.
