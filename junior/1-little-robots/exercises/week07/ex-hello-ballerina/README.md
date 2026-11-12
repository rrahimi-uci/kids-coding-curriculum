# Exercise 7.1 – Hello, Ballerina!

**Goal:** make the cat and the Ballerina take turns to say hi.
**Tool:** Scratch app. **Work with a partner:** one sprite each.

## Build steps

1. Click **Choose a Sprite** (the cat-face button under the stage). Pick **Ballerina**. Drag her to a spot you like.
2. Click **Choose a Backdrop** (bottom right corner). Pick a backdrop you like.
3. Click the **cat** in the sprite list. Click **Events** (yellow). Drag in **when green flag clicked**.
4. Click **Looks** (purple). Snap on **say Hello! for 2 seconds**. Type `Hi, Ballerina!`.
5. Swap Driver. Click the **Ballerina** in the sprite list.
6. Click **Events** (yellow). Drag in **when green flag clicked**.
7. Click **Control** (orange). Snap on **wait 1 seconds**. Change 1 to `2`.
8. Click **Looks** (purple). Snap on a say block. Type `Hi, Cat!`.
9. Click the green flag.

## The script in words

Cat:

- when green flag clicked
- say Hi, Ballerina! for 2 seconds

Ballerina:

- when green flag clicked
- wait 2 seconds
- say Hi, Cat! for 2 seconds

## Expected behavior

The cat says "Hi, Ballerina!". Then the Ballerina says "Hi, Cat!".
They take turns.

## Checklist

- [ ] The cat and the Ballerina each have their own script.
- [ ] The Ballerina waits before she talks.
- [ ] I picked a backdrop.
