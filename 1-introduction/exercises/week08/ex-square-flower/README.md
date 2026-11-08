# Exercise 8.3 - Square Flower (a loop inside a loop)

**Goal:** draw 8 squares, each turned a little, in 8 different colors.
Together they make a flower.

1. Open `starter.py` and press **Run**. It draws ONE square.
2. Put the square loop **inside** a new loop:
   ```
   for color in PALETTE:
       t.color(color)
       (the square loop goes here, pushed in 4 MORE spaces)
       t.left(45)
   ```
3. Press **Run** (F5). Tip: `t.speed(0)` makes the turtle draw super fast.

**Why 45?** There are 8 colors in the palette, and 8 x 45 = 360: one full turn.

**Done looks like:** 8 squares in 8 colors, spinning round the middle.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** try `t.left(30)` with `for i in range(12):` instead. Or make the
squares into triangles!
