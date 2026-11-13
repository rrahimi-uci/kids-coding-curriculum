# Exercise 4.1 – Dice Race

**Goal:** race the Cat and the Ballerina with a computer die.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **Variables** (orange-red). Make a variable called `roll`.
2. **Events** (yellow): drag in **when space key pressed**. Pick **c**.
3. Variables: snap on **set roll to 0**.
4. **Operators** (green): drop **pick random 1 to 10** into the 0. Change 10 to `6`.
5. **Looks** (purple): snap on **say Hello! for 2 seconds**. Drag the round **roll** block into it. Change 2 to `1`.
6. **Control** (orange): snap on **repeat 10**. Drag **roll** into the 10.
7. Inside the repeat: **move 20 steps** (blue Motion) and **next costume** (Looks).
8. Add the Ballerina. Drag the cat's script onto her in the sprite list. Change her c to **b**. Drag both racers to the left side.

## The script in words

- when c key pressed
- set roll to (pick random 1 to 6)
- say (roll) for 1 seconds
- repeat (roll)
  - move 20 steps
  - next costume

## Expected behavior

Press c: the Cat says a number and hops that many times. Press b for
the Ballerina. Nobody can guess who wins!

## Checklist

- [ ] The Cat says a number from 1 to 6.
- [ ] The Cat hops that many times.
- [ ] The Ballerina races with the b key.
- [ ] We said "good game" at the end.
