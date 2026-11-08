# Teacher reference: Homework 5 - Starry Sky
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 5 (Messages and My Blocks) homework  **Kind:** Scratch (offline app)  **Time:** about 10 minutes
**Big idea:** A My Block with a size input lets one short recipe fill the whole sky with stars of different sizes.

## The finished project
Setup: add the Pen extension and choose a dark backdrop (for example Stars, or paint it dark blue). Make a My Block `star` with an input `size`; drag `size` out of the define hat into the move block. Pen color: click the color circle and set Color 16, Saturation 72, Brightness 94 (color-safe yellow).

Sprite: Cat, define star
- define star (size)
- pen down
- repeat 5
  - move (size) steps
  - turn right 144 degrees
- pen up

Sprite: Cat, main script
- when green flag clicked
- erase all
- set pen color to (Color 16, Saturation 72, Brightness 94)
- set pen size to 3
- pen up
- hide
- repeat 10
  - go to (random position)
  - star (pick random 10 to 60)

Save as `starry-sky`.

## What you should see
- Each flag click clears the sky and draws 10 yellow five-pointed stars in random places.
- Each star has a random size from 10 to 60 steps; there are no lines joining the stars; the cat is hidden.
- Why 144 and not 72: drawing a five-pointed star goes round twice, so the turns add up to 720 degrees; 720 / 5 = 144. With 72 you get a pentagon.

## Talking points
- "star (size)" is a recipe with one blank, so every star is the same shape but a different size.
- The pen goes up before moving to a new place, so no line is drawn between stars.
- Yellow on a dark sky is easy to see: good design does not rely on a hard-to-see color.

## Common mistakes and quick fixes
- Lines joining the stars: "pen up" is missing (before the loop or at the end of the define script).
- Five-sided shape instead of a star: the turn is 72 instead of 144.
- All stars the same size: the size input is a typed number, not "pick random 10 to 60", or the move block uses a number instead of `size`.
- Stars hard to see: dark color on a dark backdrop. Use the color-safe yellow.
- Old stars stay: "erase all" is missing.

## Check-off list
- [ ] My `star` block has an input `size`, and I used it inside: the move block holds the `size` oval.
- [ ] Each click draws 10 stars of different sizes in different places.
- [ ] There are no lines between the stars.
- [ ] My stars are easy to see on the dark sky.
- [ ] I saved my project: file `starry-sky`.
