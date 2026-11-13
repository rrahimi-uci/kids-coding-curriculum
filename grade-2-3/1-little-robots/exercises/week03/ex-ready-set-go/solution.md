# Teacher reference: Exercise 3.1 - Ready, Set, Go!
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 3 (Bugs Are Clues)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** The computer is too fast to see each step; a wait block pauses so we can see it. Test, look, change one thing.

## The finished project
Setup: File > New. Keep the cat.

Sprite: Sprite1 (the cat)
- when green flag clicked
- say Ready
- wait 1 seconds
- say Set
- wait 1 seconds
- say Go!
- glide 1 secs to random position

## What you should see
- Before the fix: only "Go!" in the speech bubble, and the cat glides to a random place.
- After one wait (under Ready): "Ready" for 1 second, then "Go!" (Set is still invisible).
- After both waits: "Ready", "Set", "Go!", one second apart, then the glide. The "Go!" bubble stays on after the glide; that is normal.

## Bug-hunt answer
The bug is "too fast to see": with no wait, Scratch runs all three say blocks in one blink and only the last word stays on screen. Fix: a "wait 1 seconds" between Ready and Set, and another between Set and Go!.

## Talking points
- The debugging loop: test (click the flag), look (what happened?), change one thing, test again.
- Link to the warm-up robot that got dressed in a blur, and to the WAIT cards.
- The plain "say" block keeps going straight away; "say ... for 2 seconds" waits by itself.

## Common mistakes and quick fixes
- Used "say Hello! for 2 seconds": the words show without any wait, so there is no bug to find. Swap in the plain "say Hello!" block.
- Wait snapped at the very end: nothing changes. Waits go between the words.
- Both waits added before testing: fine, but ask the child to say which clue each wait fixed.
- Real name typed in a bubble: change it to a nickname.

## Check-off list
- [ ] The child tested before adding a wait and said what was missing: ask "what did you see?"
- [ ] Two waits sit between the say blocks: read the script top to bottom together.
- [ ] Ready, Set and Go! all show, one at a time: watch one run.
