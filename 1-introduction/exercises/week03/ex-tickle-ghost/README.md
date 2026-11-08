# Exercise 3.2 – Tickle the Ghost

**Goal:** use **if-else** with a **sensing** question inside **forever**.
**Tool:** Scratch app (offline). **Work in pairs.**

## Build steps

1. Start a new project: **File > New**.
2. Delete the cat: right-click it in the sprite pane and choose **delete**.
3. Click **Choose a Sprite** and pick **Ghost** (or any sprite you like).
4. Build the script below. **if ... then ... else** and **forever** are in **Control**.
   The pointy **touching (mouse-pointer)?** block is in **Sensing**.
   **set size to** and **say** are in **Looks**.
5. For the last **say**, delete the text so the box is empty.
6. Click the flag. Move your mouse over the ghost, then away.
7. Predict, then test: what happens if you take away the **forever**? Put it back.
8. Save as `tickle-ghost`.

## The script in words

Ghost sprite:

- when green flag clicked
- forever:
  - if touching mouse-pointer? then
    - set size to 150 %
    - say "Boo! That tickles!"
  - else
    - set size to 100 %
    - say "" (empty)

## Expected behavior

After the green flag, whenever the mouse pointer touches the ghost, it grows
bigger and says "Boo! That tickles!". When the mouse moves away, it goes back
to normal size and the speech bubble disappears. Without **forever**, nothing
happens, because the question is asked only once.

## Checklist

- [ ] The ghost grows and talks when the mouse touches it.
- [ ] It shrinks back and goes quiet when the mouse moves away.
- [ ] My **if-else** is inside **forever**.
- [ ] I can explain what happens without **forever**.
- [ ] I saved my project.
