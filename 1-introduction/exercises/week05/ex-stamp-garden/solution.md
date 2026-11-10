# Teacher reference: Exercise 5.2 - Stamp Garden
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Level 1, Week 5 (Messages and My Blocks)  **Kind:** Scratch (offline app)  **Time:** about 12 minutes
**Big idea:** Break a picture into named parts (grass, flower) so the main script reads like a plan.

## The finished project
Setup: new project, add the Pen extension, delete the cat. Paint your own sprite (Paint brush button): a circle center with circle petals in the middle of the canvas; name it `Flower`. Make two My Blocks: `flower` with an input `size`, and `grass` with no input. Grass color: click the color circle in "set pen color to" and use Color 45, Saturation 100, Brightness 62 (color-safe bluish green).

Sprite: Flower, define flower
- define flower (size)
- set size to (size) %
- change color effect by 25
- stamp

Sprite: Flower, define grass
- define grass
- set pen color to (Color 45, Saturation 100, Brightness 62)
- set pen size to 60
- go to x: -240 y: -150
- pen down
- go to x: 240 y: -150
- pen up

Sprite: Flower, main script
- when green flag clicked
- erase all
- clear graphic effects
- show
- grass
- repeat 12
  - go to x: (pick random -220 to 220) y: (pick random -140 to 120)
  - flower (pick random 30 to 100)
- hide

Save as `stamp-garden`.

## What you should see
- Each flag click erases the old garden and draws a thick bluish-green strip of grass along the bottom.
- Then 12 copies of the flower are stamped in random places, each a random size from 30% to 100% and each a different color (the color effect changes by 25 on every stamp).
- At the end the sprite hides, so only the stamps remain. Every garden is different.

## Talking points
- The main script reads like a plan: grass, then 12 flowers.
- "flower (size)" is one recipe with a blank: same flower, different size.
- Stamp leaves a picture behind; the sprite itself can then hide.

## Common mistakes and quick fixes
- The flower sprite cannot be seen moving on the second run: "show" is missing at the start. The stamps still appear (a hidden sprite still stamps in Scratch 3), but add show before grass so the child can watch the garden grow.
- No stamps appear: "erase all" comes after the stamps (it wipes them), or the stamp block is missing from define flower.
- All flowers the same color: "change color effect" is not inside the flower block or loop, or "clear graphic effects" is missing at the start.
- Grass is thin or in the wrong place: check pen size 60 and the two go-to y values (-150).
- Flower is huge or tiny: the size input was typed into the wrong slot; drag `size` from the define hat.

## Check-off list
- [ ] I painted my own flower sprite: the sprite is named Flower and has its own costume.
- [ ] I made two My Blocks: `flower` (with the input `size`) and `grass`.
- [ ] My green-flag script reads like a plan: grass, then repeat 12 flowers.
- [ ] Flowers have different sizes and colors each time.
- [ ] I used a color from the color-safe paint box for the grass: Color 45, Saturation 100, Brightness 62.
- [ ] I saved my project: file `stamp-garden`.
