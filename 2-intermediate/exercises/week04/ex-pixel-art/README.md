# Exercise 4.2 - Pixel Art

**Goal:** turn a list of strings into a picture with a **nested loop**
(a loop inside a loop).

```
"..G.....G.."   <- row 0: the inner loop walks along it, pixel by pixel
"...G...G..."   <- row 1: the outer loop moves down to the next row
```

1. Open `starter.py` and press **Run**. Only the top row appears.
2. **TODO 1:** add the outer loop `for row in grid:` so every row is drawn.
   Remember to indent the inner loop and to move down: `y = y - size`.
3. **TODO 2:** finish `count_pixels()` with a loop inside a loop.
4. Design your own picture! Copy `INVADER`, give it a new name and change
   the letters. Every row should be the same length.

**Done looks like:** a green space invader with black eyes, and
`Green pixels: 46` printed in the Shell.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** draw two pictures side by side, or make `draw_grid` take an
`x` and `y` for where the picture starts.
