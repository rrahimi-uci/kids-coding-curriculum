# Homework 9 - Stamp Studio

**Goal:** an art program you play with the keyboard: move, stamp, change the
shape and the colour.

1. Open `starter.py` and press **Run**. Click the window. Arrows move the
   turtle and `s` stamps a copy. But `p` and `n` do nothing yet.
2. **TODO 1** `next_index()`: return the next position in a list, and go back
   to 0 after the last one. `(index + 1) % length` does exactly that.
3. **TODO 2** write `next_colour()`, a twin of `next_shape()`.
4. **TODO 3** connect `p` to `next_shape` and `n` to `next_colour`.
   Remember: no `()` after the function name!
5. Make a picture: a flower, a robot, a pattern, a city...

**Keys:** arrows move, `s` stamps, `p` next shape, `n` next colour, `c` clears.

**Done looks like:** every key works, and pressing `p` or `n` many times goes
round all the shapes or colours and starts again.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a key that makes the stamps bigger and smaller
(`stamper.shapesize(...)`), or a key that stamps a ring of 8 copies.
