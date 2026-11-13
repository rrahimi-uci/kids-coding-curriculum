# Teacher reference: Exercise 3.1 - Arrow-Key Explorer
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1 (Introductory), Week 3  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** An event block is a doorbell: its script waits quietly until the key is pressed, then runs.

## The finished project
Sprite: Cat (or any sprite). Four separate scripts, no green flag needed.

Script 1
- when [right arrow] key pressed
- change x by (10)

Script 2
- when [left arrow] key pressed
- change x by (-10)

Script 3
- when [up arrow] key pressed
- change y by (10)

Script 4
- when [down arrow] key pressed
- change y by (-10)

Setup: drag four "when [space] key pressed" blocks from Events and change each dropdown. The child clicks the stage once so Scratch listens to the keyboard. Save as `explorer` (it is used again in Exercise 3.3).

## What you should see
- Right arrow moves the sprite 10 steps right, left arrow 10 left, up arrow 10 up, down arrow 10 down.
- Holding a key down keeps the sprite moving.
- Nothing needs the green flag. Each key is its own doorbell.

## Talking points
- "x is left and right, y is up and down. Bigger y means higher." (Answer to the checklist question: the up arrow makes y bigger.)
- "One sprite can have many scripts, each waiting for a different doorbell."
- "Predict before each test: which way will the sprite move?"

## Common mistakes and quick fixes
- Arrow keys do nothing: click the stage once so Scratch hears the keyboard.
- A key does the wrong thing: the dropdown still says "space", or the wrong arrow is chosen. Check each hat block.
- Up goes down (or left goes right): the sign is wrong. Up is change y by +10, down is -10; right is +10 in x, left is -10.
- Only one key works: the four blocks were snapped into one stack instead of four separate scripts.
- Scripts are on the wrong sprite: click the sprite you want to move and check the code area.

## Check-off list
- [ ] Four scripts, one for each arrow key: four separate hat blocks.
- [ ] Each key moves the sprite the right way: press each key.
- [ ] Can say which key makes y bigger: the up arrow.
- [ ] Saved as `explorer`.
