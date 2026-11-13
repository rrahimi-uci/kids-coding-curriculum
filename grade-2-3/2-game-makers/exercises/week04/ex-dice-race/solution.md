# Teacher reference: Exercise 4.1 - Dice Race
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 4 (Surprise! Random)  **Kind:** Scratch (offline app)  **Time:** about 13 minutes
**Big idea:** pick random is a die inside the computer. Keep the roll in a variable and use it as often as you like.

## The finished project
Setup: File > New. Keep the cat and add the Ballerina. Make one variable, "roll", For all sprites. Drag both sprites to the left side of the stage, one above the other, with a small gap before the edge.

Sprite: Sprite1 (the cat)
- when c key pressed
- set roll to (pick random 1 to 6)
- say (roll) for 1 seconds
- repeat (roll)
  - move 20 steps
  - next costume

Sprite: Ballerina (copied from the cat by dragging the script onto her in the sprite list)
- when b key pressed
- set roll to (pick random 1 to 6)
- say (roll) for 1 seconds
- repeat (roll)
  - move 20 steps
  - next costume

## What you should see
- Each press of c: the cat says a number from 1 to 6 for one second, then dashes to the right in that many quick hops, changing costume each hop. The "roll" box on the stage shows the same number.
- Each press of b: the same for the Ballerina, who changes dance pose as she hops.
- A race takes about four or five turns each. Different racers win different races.

## Talking points
- Before each roll, ask "How far will it go?" The honest answer is "I don't know": that is random.
- The variable remembers the roll so the say block and the repeat use the same number. Two separate pick random blocks would roll two different numbers.
- The die decides the winner, not the player. Link to the good-sport talk in Share.
- A real die goes from 1 to 6. Children may try 1 to 10: a ten-sided die makes a faster race.

## Common mistakes and quick fixes
- The cat says the word "roll": the word was typed. Drag the round orange-red roll block into the slot.
- A pick random block in the say block and another in the repeat: the cat says one number and hops another. Use the roll variable in both.
- The Ballerina moves when c is pressed: her copy still says c. Pick b.
- Nothing happens: click the stage once so the keyboard goes to Scratch.
- A racer starts touching the left edge or ends at the right edge and cannot go further: drag both back to the left side to race again.

## Check-off list
- [ ] One variable, "roll", For all sprites.
- [ ] The round roll block is in the say block and in the repeat.
- [ ] The Cat listens for c and the Ballerina for b.
- [ ] Each racer hops as many times as the number it says.
