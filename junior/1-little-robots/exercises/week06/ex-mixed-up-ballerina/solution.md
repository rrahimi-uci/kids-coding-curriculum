# Teacher reference: Exercise 6.3 - The Mixed-Up Ballerina (bug hunt)
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 6 (When I Click...)  **Kind:** Scratch (offline app), bug hunt  **Time:** about 8 minutes
**Big idea:** Each sprite has its own scripts, and each event block waits for one exact event. A script in the wrong sprite, or waiting for the wrong key, never runs when you expect it to.

## The finished project
Setup: File > New. Keep the cat. Add the Ballerina with the "Choose a Sprite" button. Build the buggy version from the workbook first. (Support path: build it yourself before the session.)

Sprite: Sprite1 (the cat), after the fix
- (no scripts)

Sprite: Ballerina, after the fix
- when this sprite clicked
- say Hi! for 2 seconds

- when space key pressed
- repeat 4
  - next costume
  - wait 1 seconds

## What you should see
- With the bugs: clicking the Ballerina does nothing; clicking the cat makes the cat say "Hi!"; space does nothing; pressing the a key makes the Ballerina dance.
- After the fixes: clicking the Ballerina makes her say "Hi!" for 2 seconds; space makes her change costume four times, once a second; clicking the cat does nothing.

## Bug-hunt answer
- Bug 1, script under the wrong sprite: "when this sprite clicked, say Hi!" is in the cat's code. "This sprite" always means the sprite whose code it is in. Fix: drag the script from the cat's code area onto the Ballerina in the sprite list (she wiggles, and the script is copied), then delete the cat's copy by dragging it back onto the block palette. Rebuilding it in the Ballerina's code is also fine.
- Bug 2, wrong key: the Ballerina's hat block says "when a key pressed". Fix: click the dropdown and pick "space".

## Talking points
- Link to the warm-up: the clap card in the wrong hands, and "banana" that nobody listens for.
- Which sprite am I coding? Look for the sprite with the blue frame in the sprite list before you build.
- A good test tries both: click every sprite, press every key in the plan.

## Common mistakes and quick fixes
- The child moves the script but forgets to delete the cat's copy: the cat still talks when clicked. Not wrong, but not Kai's plan; delete it.
- The script is dropped on the stage instead of the sprite list: it does not copy. Drop it on the Ballerina's picture under the stage.
- Space still does nothing after the fix: click the stage once so the keyboard goes to the project.
- The child changes the cat's hat to "when green flag clicked": that is a different bug. Read Kai's plan again.

## Check-off list
- [ ] The click script is in the Ballerina's code, and the cat has no "Hi!" script.
- [ ] The Ballerina's key block says "space".
- [ ] Click the Ballerina: "Hi!". Press space: four costume changes.
