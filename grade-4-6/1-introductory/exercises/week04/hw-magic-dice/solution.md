# Teacher reference: Homework 4 - Magic Dice
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 4 (Keeping Score) homework  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** "pick random" gives a surprising number, and two variables can show the roll and count the rolls.

## The finished project
Setup: make two variables, `roll` and `rolls` (For all sprites). Any sprite works (the cat is fine). "join" and "pick random" are in Operators. Type a space after "You rolled".

Sprite: any sprite, script 1
- when green flag clicked
- set rolls to 0
- say [Press space to roll!]

Sprite: any sprite, script 2
- when space key pressed
- set roll to (pick random 1 to 6)
- change rolls by 1
- say (join [You rolled ] (roll))
- if roll = 6 then
  - start sound (any)

Save as `magic-dice`.

## What you should see
- After the green flag: `rolls` shows 0 and the sprite says "Press space to roll!".
- Each space press: the sprite says "You rolled" and a number from 1 to 6 (for example "You rolled 4"), and `rolls` goes up by 1.
- A roll of 6 also plays a sound. After 10 rolls, `rolls` shows 10.
- Nobody can predict the next number: the numbers are random.

## Talking points
- pick random 1 to 6 works like rolling a real die: you cannot know the answer before it happens.
- `roll` remembers this roll; `rolls` counts how many times we rolled. Two boxes, two jobs.
- join glues words and a number together into one message.

## Common mistakes and quick fixes
- "You rolled4" with no space: add a space inside the quotes after "rolled".
- `rolls` shows 1 every time: "set rolls to 0" is inside the space script. It belongs under the green flag, once.
- Roll can be 0 or 7: the pick random range is wrong; use 1 to 6.
- Sound plays on every roll: the "if roll = 6" block is missing around the sound.
- Sprite says the word "roll": the variable block was not dropped into the join block.

## Check-off list
- [ ] I made the variables `roll` and `rolls`: both visible in the Variables palette.
- [ ] `rolls` starts at 0 every time I click the green flag.
- [ ] Each roll says a number from 1 to 6: roll 10 times and check the homework sheet.
- [ ] A 6 plays a sound: only on a 6.
- [ ] I saved my project: file `magic-dice`.
