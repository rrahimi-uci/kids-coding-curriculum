# Teacher reference: Exercise 1.2 - Mixed-Up Jump (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introductory), Week 1  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** When steps are in the wrong order the program still runs, but it does the wrong thing, so we read it one block at a time to find the bug.

## The finished project
Sprite: Cat (the fixed script)
- when green flag clicked
- go to x: 0 y: -100
- say [Watch me jump!] for (2) seconds
- change y by (50)
- wait (0.5) seconds
- change y by (-50)
- say [Ta-da!] for (2) seconds

Setup: no extension. "change y by" is in Motion, "wait" is in Control. The child first builds the buggy version exactly as in the README (change y by -50, wait 0.5, change y by 50), then fixes it. Save as `mixed-up-jump`.

## What you should see
- Buggy version: the cat says "Watch me jump!", then drops 50 down to y: -150 (near the bottom edge), waits half a second, comes back up to y: -100, then says "Ta-da!". It never jumps up.
- Fixed version: the cat says "Watch me jump!", rises to y: -50, waits half a second, comes back down to y: -100, then says "Ta-da!".

## Bug-hunt answers
- Where: the two blocks "change y by -50" and "change y by 50".
- What goes wrong: the cat goes down first and then up, so it looks like it sinks instead of jumping.
- Why: y means up and down, and a bigger y means higher. A negative number moves the cat down.
- Fix: swap the two blocks so "change y by 50" comes before the wait, and "change y by -50" comes after it. Accept any order that makes the cat go up, pause, come down, then say "Ta-da!".

## Talking points
- "Say what you expected. Say what happened. Act out each block with your finger, then change one thing and test again."
- "Like a recipe: flipping the pancake before pouring the batter makes a mess, even though every step is real."
- "Bugs are normal. Every coder makes them every day."

## Common mistakes and quick fixes
- Child fixes it by changing the numbers instead of the order: that also works (-50 becomes 50 and 50 becomes -50), but ask them to also describe the order idea.
- Child changes two things at once and cannot tell which fixed it: change one thing, then test.
- The jump cannot be seen: the wait block was removed or set to 0.
- The cat ends higher or lower than it started: the two change y numbers are not opposites (+50 and -50).
- It does nothing: blocks not snapped to the hat block, or the wrong sprite is selected.

## Check-off list
- [ ] Built the buggy script first and saw what went wrong: ask "what did the cat do the first time?" (It went down.)
- [ ] Can say which two blocks were in the wrong order: the two change y blocks.
- [ ] After the fix the cat jumps up and lands back on the ground: it ends at y: -100.
- [ ] Tested more than once: ask them to click the flag again.
