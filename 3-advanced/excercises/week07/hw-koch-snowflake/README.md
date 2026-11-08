# Homework 7 challenge - Koch snowflake

**Goal:** draw a famous fractal: the Koch snowflake.

A **Koch line** of depth 0 is a straight line. A Koch line of depth 1 is four
lines, each a third as long, with a bump in the middle: `___/\___`.
Depth 2 does the same thing to *each* of those four lines, and so on.

1. Open `starter.py` and press **Run**: three triangles appear.
2. In `koch()`, replace the straight line in the recursive case with four
   smaller Koch lines and the turns 60, 120, 60 (follow the TODO).
3. Run again. The triangles should become snowflakes.

**Done looks like:** depth 1 = 4 lines per side, depth 2 = 16, depth 3 = 64.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** what happens if you turn `left(120)` instead of `right(120)` in
`snowflake()`? Try depth 4 (it has 768 lines!).
