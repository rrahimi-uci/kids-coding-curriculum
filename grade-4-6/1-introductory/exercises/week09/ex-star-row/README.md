# Exercise 9.3 - How Many Stars?

**Goal:** ask how many stars to draw (1 to 10), then draw a row of them.
Use `if / elif / else` and comparisons (`>` and `<`) to keep the answer sensible.

1. Open `starter.py` and press **Run** (F5). Type `3`. Three stars!
2. Now try `25`. The stars run off the screen! Try `0`. Nothing at all.
3. Follow the `# TODO`: before drawing,
   * **if** `stars > 10`: print a message and set `stars = 10`,
   * **elif** `stars < 1`: print a message and set `stars = 1`,
   * **else**: print `"Coming right up!"`.
4. Test with `3`, `25` and `0`.

**Done looks like:** 25 becomes 10 stars, 0 becomes 1 star, and the program
always tells you what it is doing.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** ask a second question, "Big or small stars?", and use the answer to
choose the star size (50 or 25).
