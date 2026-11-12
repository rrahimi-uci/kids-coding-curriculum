# Teacher reference: Exercise 6.2 - Keyboard Cat
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 1, Week 6 (When I Click...)  **Kind:** Scratch (offline app)  **Time:** about 7 minutes
**Big idea:** Each key can start its own script. One sprite can have several scripts, each waiting for a different event.

## The finished project
Setup: File > New (or keep working in the Click the Cat project). Keep the cat.

Sprite: Sprite1 (the cat), script 1
- when right arrow key pressed
- move 10 steps
- next costume

Sprite: Sprite1 (the cat), script 2
- when space key pressed
- repeat 24
  - turn right 15 degrees

## What you should see
- Each press of the right arrow: the cat moves a little to the right and switches costume, so it looks as if it walks. Holding the key keeps it walking.
- Each press of the space bar: the cat spins once all the way round, quickly, and stops facing right again (24 small turns of 15 make one full spin; children do not need to work this out).

## Talking points
- Two hat blocks, two scripts. Each one waits for its own key, like the clap card and the stomp card.
- The repeat from week 4 is back: the spin is one small turn, repeated.
- Why no "move left" key? Moving left needs ideas from later grades. Dragging the cat back with the mouse is the Level 1 way.

## Common mistakes and quick fixes
- Keys do nothing: the keyboard is busy elsewhere. Click once on the stage, then press the key.
- The dropdown still says "space" on both scripts: then space makes the cat walk and spin at once. Pick "right arrow" in the first one.
- The turn block is under the repeat, not inside: the cat turns only a little. Drag it into the mouth of the repeat.
- A number other than 24 in the repeat: the cat ends up tilted, and the right arrow then walks it in a slanted line. Change the repeat back to 24, or reset with "point in direction 90" (blue Motion) clicked once.
- The cat walks off the right edge: drag it back with the mouse.

## Check-off list
- [ ] Two separate scripts, each with its own yellow key hat block.
- [ ] The dropdowns say "right arrow" and "space".
- [ ] The turn block is inside the repeat.
- [ ] Right arrow walks, space spins: test both keys.
