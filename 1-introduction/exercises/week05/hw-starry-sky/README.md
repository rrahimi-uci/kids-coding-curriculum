# Homework 5 – Starry Sky

**Goal:** make a My Block `star (size)` and use it to fill the night sky.
**Time:** about 10 minutes. **Tool:** Scratch app (offline) with the Pen extension.

## Build steps

1. Open Scratch (**File > New** if an old project is open) and add the **Pen** extension. Choose a dark backdrop
   (for example **Stars**, or paint the backdrop dark blue).
2. **My Blocks > Make a Block**: name it `star`, add an input `size`, click **OK**.
3. Build both scripts. Drag `size` out of the define hat into the move block.
4. For the pen color, click the color circle and drag the sliders until they show
   **Color 16, Saturation 72, Brightness 94** (yellow from the color-safe paint box).
5. Click the green flag. Save as `starry-sky`.

## The scripts in words

**define star (size)**

- pen down
- repeat 5:
  - move (size) steps
  - turn right 144 degrees
- pen up

(**turn right** is the **Motion** block **turn ↻ (15) degrees**.)

**when green flag clicked**

- erase all
- set pen color to (yellow)
- set pen size to 3
- pen up
- hide
- repeat 10:
  - go to random position
  - star (pick random 10 to 60)

## Expected behavior

Each click on the green flag clears the sky and draws 10 yellow five-pointed
stars in surprise places, each a different size. There are no lines joining
the stars. The cat is hidden.

**Think about it:** why does the star block turn 144 degrees and not 72?
Hint: count how many times the pen goes all the way round while it draws one star.
Write your answer on your homework sheet.

## Checklist

- [ ] My `star` block has an input `size`, and I used it inside.
- [ ] Each click draws 10 stars of different sizes in different places.
- [ ] There are no lines between the stars.
- [ ] My stars are easy to see on the dark sky.
- [ ] I saved my project.
