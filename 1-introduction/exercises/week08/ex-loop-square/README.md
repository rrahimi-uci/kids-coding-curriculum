# Exercise 8.1 - Loop Square

**Goal:** draw a square with a `for` loop - 3 lines of code instead of 8.

1. Open `starter.py` in Thonny and press **Run** (F5). The turtle goes in a
   straight line. Why? Nothing inside the loop turns it!
2. Add `t.left(90)` **inside** the loop. Inside means: pushed in by 4 spaces,
   lined up exactly under `t.forward(100)`.
3. Press **Run** again.

**Done looks like:** a closed square, drawn by a loop that repeats 4 times.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** change `4` and `90` to draw a triangle (3, 120) or a hexagon (6, 60).
The secret rule: the turn is always 360 divided by the number of sides.
