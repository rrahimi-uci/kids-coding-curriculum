# Teacher reference: Exercise 6.3 - Relay C: The Silent Party (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 6 (Review Studio and Checkpoint)  **Kind:** Scratch (offline app)  **Time:** about 6 minutes
**Big idea:** Messages must match exactly, and a loop with no wait can run too fast to see.

## The finished project
Setup: new project, keep the cat, add the Ghost sprite, make two messages (broadcast > New message): `party` and `dance`. Students first build the buggy version exactly as printed.

Sprite: Cat (fixed version)
- when space key pressed
- say [Party time!] for (2) seconds
- broadcast (party)

Sprite: Ghost, script 1
- when green flag clicked
- hide

Sprite: Ghost, script 2 (fixed version)
- when I receive (party)
- show
- repeat 10
  - turn right 36 degrees
  - next costume
  - wait 0.2 seconds
- say [Woo!] for (2) seconds

## What you should see
- After the green flag the Ghost is hidden.
- Pressing space: the cat says "Party time!" for 2 seconds, then the Ghost appears, spins one full turn (10 x 36 = 360 degrees) over about 2 seconds while changing costume, and says "Woo!".
- Buggy version: the cat says "Party time!" and then nothing else happens.

## Bug-hunt answers
- Bug 1, where: the Ghost's hat block "when I receive (dance)" while the cat broadcasts `party`. What goes wrong: nobody receives `party`, so the Ghost never appears. Fix: make the names match, for example change the Ghost's hat to "when I receive party" (or the cat's broadcast to `dance`).
- Bug 2, where: inside the Ghost's repeat 10 loop. What goes wrong: once the Ghost appears, the dance is over in a blink (about a third of a second). Why: there is no wait in the loop. Fix: add "wait 0.2 seconds" inside the repeat (10 x 0.2 = 2 seconds).

## Talking points
- Loudspeaker analogy: the Ghost is listening for "dance" but the announcement said "party".
- Computers are very fast: without a wait, ten steps happen faster than your eye can follow.
- Fix one bug, test, then look for the second.

## Common mistakes and quick fixes
- Ghost appears but only flashes: the wait is missing or outside the loop. Put it inside the repeat.
- Ghost visible at the start: the hide script under the green flag is missing.
- Nothing happens when space is pressed: the cat script is on the wrong sprite or the key is different.
- Two similar message names make it worse: choose the message from the dropdown, do not make a new one.
- Team stops after the message fix: compare the stage with "should do" again; the dance must be watchable.

## Check-off list
- [ ] I built the show exactly as shown and watched what went wrong: the Ghost never showed up.
- [ ] I found bug 1 and wrote it on my relay baton: message names do not match.
- [ ] I found bug 2 and wrote it on my relay baton: no wait in the dance loop.
- [ ] After my fixes, the Ghost appears and I can watch the whole dance.
