# Exercise 2.1 – Boo Ghost

**Goal:** make the ghost say "Boo!" when the mouse touches it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **Choose a Sprite** (under the stage). Pick **Ghost**.
2. Click **Events** (yellow). Drag in **when green flag clicked**.
3. Click **Control** (orange). Snap on **forever**.
4. Put **if then** (orange Control) inside the forever.
5. Click **Sensing** (light blue). Drag **touching mouse-pointer?** into the pointy hole of the if.
6. Put **say Hello! for 2 seconds** (purple Looks) inside the if. Type `Boo!` and change 2 to `1`.
7. Click the flag. Move the mouse onto the ghost.

## The script in words

- when green flag clicked
- forever
  - if touching mouse-pointer? then
    - say Boo! for 1 seconds

## Expected behavior

When the mouse touches the ghost, it says "Boo!". When the mouse is away,
the ghost says nothing. It keeps checking until you click the red stop sign.

## Checklist

- [ ] The if is inside the forever.
- [ ] The touching block is in the pointy hole.
- [ ] The ghost says "Boo!" only when the mouse touches it.
