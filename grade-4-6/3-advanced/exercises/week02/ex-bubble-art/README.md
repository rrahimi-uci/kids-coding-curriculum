# Exercise 2.2 - Bubble Art

**Goal:** finish a `Bubble` class and use it to paint a picture full of
bubbles. Each bubble is an object that remembers its own `x`, `y`, `size`
and `color`.

1. Open `starter.py` in Thonny.
2. Finish the `TODO`s: `__init__`, `grow`, `move`, the big dot in `draw`,
   and `make_bubbles`.
3. Press **Run**. A black window fills with 40 colorful bubbles, each with a
   little white shine.

**Math helper:** `(0, 0)` is the middle of the turtle window. A minus sign
means "left of the middle" for `x` and "below the middle" for `y`. So
`x = -300` is 300 steps to the left, and `y = -200` is 200 steps down.

**Done looks like:** 40 round bubbles of different sizes and colors, spread
over the whole window, and every check in `check_my_work.py` passes. The
picture is random, so it is different every time you press Run.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a method `pop(self, t)` that draws a ring of small dots
around the bubble, or make bubbles near the top of the screen bigger.
