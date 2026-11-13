# Homework 9 - Stamp Studio

**Goal:** an art program you play with the keyboard: move, stamp, change the
shape and the color.

1. Open `starter.py` and press **Run**. Click the window. Arrows move the
   turtle and `s` stamps a copy. But `p` and `n` do nothing yet.
2. **TODO 1** `next_index()`: return the next position in a list, and go back
   to 0 after the last one. `(index + 1) % length` does exactly that.
   Remember: `%` gives the **remainder** (week 5). The list of shapes has 4
   items, at positions 0, 1, 2 and 3. From position 2: 2 + 1 = 3, and
   3 / 4 is 0 remainder 3, so the answer is 3. From the last position, 3:
   3 + 1 = 4, and 4 / 4 is 1 remainder **0**, so we go back to 0.
3. **TODO 2** write `next_color()`, a twin of `next_shape()`.
4. **TODO 3** connect `p` to `next_shape` and `n` to `next_color`.
   Remember: no `()` after the function name!
5. Make a picture: a flower, a robot, a pattern, a city...

**Keys:** arrows move, `s` stamps, `p` next shape, `n` next color, `c` clears.

**Done looks like:** every key works, and pressing `p` or `n` many times goes
around all the shapes or colors and starts again.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a key that makes the stamps bigger and smaller
(`stamper.shapesize(...)`), or a key that stamps a ring of 8 copies.
