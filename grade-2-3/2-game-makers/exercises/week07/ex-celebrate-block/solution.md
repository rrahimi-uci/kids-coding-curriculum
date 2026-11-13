# Teacher reference: Exercise 7.1 - Celebrate Block
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 7 (My Own Blocks)  **Kind:** Scratch (offline app)  **Time:** about 8 minutes
**Big idea:** A My Block gives a group of blocks a name. You make it once and use it wherever you need it; change the recipe once and every use changes.

## The finished project
Setup: File > New. Keep the cat.

Sprite: Sprite1 (the cat), the My Block
- define celebrate
- start sound Pop
- repeat 4
  - turn right 90 degrees (a quarter turn)
- say Hooray! for 1 seconds

Sprite: Sprite1 (the cat), using it
- when this sprite clicked
- celebrate

- when space key pressed
- celebrate

## What you should see
- Click the cat or press space: a pop, one quick full spin (the cat ends facing the same way), then "Hooray!" in a speech bubble for 1 second.
- The green flag does nothing: there is no flag script.
- Change the sound in the define script (for example to Meow): both the click and the space key now use the new sound. This is the point of a My Block.

## Talking points
- Link to the warm-up: the define script is the MAKE TOAST envelope; the small celebrate block is saying its name.
- The define hat has no flag and no key. It runs only where the named block is used.
- Splitting a game into named parts (get ready, celebrate, game over) makes long scripts short and easy to read. This is called decomposition; children do not need the word.

## Common mistakes and quick fixes
- Clicking Make a Block twice gives "celebrate" and "celebrate2": delete the empty define script (drag it to the block palette) and use the one with blocks.
- The celebrate block is snapped under its own define script: the cat celebrates on and on. Drag it out and put it under a hat block.
- The turn is under the repeat, not inside it: the cat turns only a little. Drag it into the mouth of the repeat.
- The block was made while another sprite was selected: My Blocks belong to one sprite. Click the cat in the sprite list and make it there.
- Space does nothing: click the stage once, then press space.

## Check-off list
- [ ] One "define celebrate" script with the sound, the repeat (turn inside) and the say block under it.
- [ ] "celebrate" is used under "when this sprite clicked": click the cat to test.
- [ ] "celebrate" is used under "when space key pressed": press space to test.
- [ ] The child changes the sound once in the define script and shows that both uses change.
