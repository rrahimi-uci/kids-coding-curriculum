# Teacher reference: Exercise 6.3 - Nobody Is Listening (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 6 (Messages)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 8 minutes
**Big idea:** A message only starts scripts that listen for exactly that name. If nobody listens, or the name is different, nothing happens.

## The finished project
Setup: File > New. Add the Star, Balloon1 and the Ghost; delete the cat. Drag the Balloon to the bottom of the stage. Build the Balloon's script first (so its hat keeps "message1"), then the Star's (New message "go"), then the Ghost's, all as printed with the bugs. Then fix.

Sprite: Balloon1, after the fix
- when I receive go
- point in direction 0
- repeat 10
  - move 10 steps

Sprite: Star
- when this sprite clicked
- broadcast go

Sprite: Ghost, after the fix
- when I receive go
- say Boo! for 2 seconds

## What you should see
- With the bugs: the flag makes the Ghost say "Boo!" at once; clicking the Star does nothing at all.
- After the fixes: the flag does nothing visible. Clicking the Star makes the Balloon turn to face up and float a good way up the stage, and the Ghost says "Boo!" for 2 seconds at the same time.
- To play again, drag the Balloon back down.

## Bug-hunt answer
- Bug 1, nobody is listening: the Ghost's script starts with "when green flag clicked", so the Ghost talks at the flag and no sprite listens for "go" from the Ghost. Fix: drag "say Boo!" off the flag block, snap it under a new "when I receive go" hat (yellow Events), and delete the empty flag block.
- Bug 2, wrong message name: the Balloon listens for "message1", a name Scratch puts in new blocks. Fix: click the arrow in its hat block and pick "go".
- Both bugs match the warm-up: the HOP note nobody held, and the SPIN note sent to the child who waited for TWIRL.

## Talking points
- Ask "Who is listening for go?" before any fix. Pointing at each hat block is the "look" step.
- Always pick message names from the dropdown rather than typing a new, similar name.
- The Ghost "worked" but at the wrong time: a bug can be a right action at the wrong moment.

## Common mistakes and quick fixes
- The Balloon's hat already says "go" when built: the child made the Star's message first. Pick "message1" (or any other name) to rebuild the bug, or explain it from the printed picture.
- The child fixes the Ghost by adding "broadcast go" to the Ghost: that sends, it does not listen. Ask "Which block listens?"
- The Balloon floats up only a little, or sideways: "point in direction 0" is missing or says 90.
- The Balloon starts at the top and cannot float up: drag it down first.

## Check-off list
- [ ] The Ghost's say block is under "when I receive go".
- [ ] The Balloon's hat block says "go".
- [ ] The flag alone does nothing; clicking the Star starts both.
- [ ] The child tested before and after each fix.
