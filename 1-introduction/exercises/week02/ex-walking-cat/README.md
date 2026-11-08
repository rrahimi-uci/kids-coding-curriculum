# Exercise 2.1 – Walking Cat

**Goal:** use a **forever** loop and costumes to make the cat walk back and forth.
**Tool:** Scratch app (offline). **Work in pairs:** swap driver and navigator when the timer rings.

## Build steps

1. Start a new project: **File > New**.
2. Click the **Costumes** tab (top left). The cat has 2 costumes. Switching between
   them looks like walking. Click the **Code** tab to go back.
3. Build the script below. **set rotation style** and **if on edge, bounce** are in
   **Motion**; **forever** and **wait** are in **Control**; **next costume** is in **Looks**.
4. Click the green flag. Click the red stop sign to stop.
5. Experiment: take out the **wait** block. What changes? Put it back.
6. Save as `walking-cat`.

## The script in words

Cat sprite:

- when green flag clicked
- set rotation style left-right
- forever:
  - move 10 steps
  - next costume
  - if on edge, bounce
  - wait 0.1 seconds

## Expected behavior

After the green flag, the cat walks across the stage, moving its legs. At the
edge it turns round (and stays the right way up) and walks back. It keeps going
until you click the red stop sign. Without the wait, the cat zooms and its
legs flicker too fast to see.

## Checklist

- [ ] My script uses a **forever** loop.
- [ ] **next costume** is inside the loop, so the legs move.
- [ ] The cat turns round at the edge and is not upside down.
- [ ] I tried it without **wait** and can say what changed.
- [ ] I saved my project.
