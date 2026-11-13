# Exercise 7.2 - Fractal tree

**Goal:** draw a tree where every branch has two smaller trees on top of it.

A **fractal** is a picture made of smaller copies of itself. A tree is a
trunk with two smaller trees on top. Each smaller tree is a trunk with two
even smaller trees on top... until the **depth** reaches 0 (the base case).

**Steps**

1. Open `starter.py` and press **Run**. You see only the trunks.
2. Inside `branch()`, after the trunk is drawn, follow TODO 1 to TODO 5:
   turn left, draw a smaller tree, turn right twice as far, draw another
   smaller tree, turn back to face up.
   With `ANGLE = 25` that is left 25, right 50, left 25 degrees.
3. Run again. Three trees should grow: depth 3 on the left, depth 7 in the
   middle and depth 5 on the right.

**Math helper:** `SHRINK = 0.7` means **7 tenths**. Each smaller tree is
`length * SHRINK` long, so a branch of 100 steps grows branches of
100 x 0.7 = 70 steps, then 70 x 0.7 = 49 steps, and so on. Multiplying by a
number smaller than 1 always makes it smaller.

**Done looks like:** depth 1 = 1 line, depth 2 = 3 lines, depth 3 = 7 lines.
Each extra level doubles the twigs!

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** change `ANGLE` and `SHRINK` at the top. What happens with
`ANGLE = 90`? Can you make a tree that leans in the wind (different left
and right angles)?
