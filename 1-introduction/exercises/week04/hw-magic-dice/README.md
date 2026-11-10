# Homework 4 – Magic Dice

**Goal:** make a dice roller with **pick random** and two **variables**.
**Time:** about 10 minutes. **Tool:** Scratch app (offline).

## Build steps

1. Open Scratch (**File > New** if an old project is open). Make two variables: `roll` and `rolls` (**For all sprites**).
2. Build the two scripts below. **join** and **pick random** are in **Operators**.
   Type a space after "You rolled" so the words don't squash together.
3. Click the green flag, then press **space** to roll.
4. Roll 10 times and write the numbers in your homework sheet.
5. Save as `magic-dice`.

## The scripts in words

1. when green flag clicked
   - set rolls to 0
   - say "Press space to roll!"
2. when space key pressed
   - set roll to (pick random 1 to 6)
   - change rolls by 1
   - say (join "You rolled " (roll))
   - if roll = 6 then
     - start sound (any)

## Expected behavior

After the green flag, `rolls` shows 0 and the sprite says "Press space to
roll!". Each time you press space, the sprite says a number from 1 to 6, like
"You rolled 4", and `rolls` goes up by 1. Rolling a 6 also plays a sound.
You can never predict the next number.

## Checklist

- [ ] I made the variables `roll` and `rolls`.
- [ ] `rolls` starts at 0 every time I click the green flag.
- [ ] Each roll says a number from 1 to 6.
- [ ] A 6 plays a sound.
- [ ] I saved my project.
