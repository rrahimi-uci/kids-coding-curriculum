# Exercise 2.2 – Party Time

**Goal:** build the party plan one part at a time, and test each part.
**Tool:** Scratch app, plan card. **Work with a partner:** Driver and Helper.

## Build steps

1. **Variables** (orange-red): make `pops`, **For all sprites**.
2. Part 1: build the cat's script. In **broadcast**, pick **New message**: `balloons`.
3. Test Part 1: click the flag. Check its box on the plan card.
4. **Choose a Sprite**: **Balloon1**. Build Part 2 (two scripts).
5. Test Part 2: click the **when I receive** script.
6. Build Part 3. Test it: click the balloon.
7. Click the flag. Test all the parts together.

## The script in words

Cat:

- when green flag clicked
- set pops to 0
- say Party time! for 2 seconds
- broadcast balloons

Balloon1:

- when green flag clicked
- hide

- when I receive balloons
- go to random position
- show

- when this sprite clicked
- start sound Pop
- change pops by 1
- go to random position

## Expected behavior

The cat says "Party time!". Then a balloon appears. Click it: pop! Pops
goes up and the balloon jumps.

## Checklist

- [ ] I tested each part before I built the next one.
- [ ] The balloon comes after "Party time!".
- [ ] Each pop adds 1 to pops.
