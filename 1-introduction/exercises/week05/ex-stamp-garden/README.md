# Exercise 5.2 – Stamp Garden

**Goal:** break a picture into named parts with two My Blocks (`grass` and
`flower (size)`) and stamp a garden that is different every time.
**Tool:** Scratch app (offline) with the Pen extension. **Work in pairs.**

## Build steps

1. Start a new project and add the **Pen** extension. Delete the cat.
2. Hover over **Choose a Sprite** and click the **Paint** brush. Draw a flower in
   the middle of the canvas (a circle for the center and circles for petals).
   Name the sprite `Flower`.
3. Make a My Block `flower` with an input `size`.
4. Make a My Block `grass` with no input.
5. Build the three scripts below.
   For the grass color, click the color circle in **set pen color to** and drag the
   sliders until they show **Color 45, Saturation 100, Brightness 62** (bluish green from the color-safe paint box).
6. Click the green flag a few times: a new garden grows each time.
7. Save as `stamp-garden`.

## The scripts in words

**define flower (size)**

- set size to (size) %
- change color effect by 25
- stamp

**define grass**

- set pen color to (bluish green)
- set pen size to 60
- go to x: -240 y: -150
- pen down
- go to x: 240 y: -150
- pen up

**when green flag clicked**

- erase all
- clear graphic effects
- show
- grass
- repeat 12:
  - go to x: (pick random -220 to 220) y: (pick random -140 to 120)
  - flower (pick random 30 to 100)
- hide

## Expected behavior

Each click on the green flag clears the stage, draws a thick strip of grass
along the bottom, and stamps 12 flowers in surprise places. The flowers have
different sizes and different colors. At the end the Flower sprite hides, so
only the stamped garden is left. Every garden is different.

## Checklist

- [ ] I painted my own flower sprite.
- [ ] I made two My Blocks: `flower` (with the input `size`) and `grass`.
- [ ] My green-flag script reads like a plan: grass, then 12 flowers.
- [ ] Flowers have different sizes and colors each time.
- [ ] I used a color from the color-safe paint box for the grass.
- [ ] I saved my project.
