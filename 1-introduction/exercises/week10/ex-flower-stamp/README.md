# Exercise 10.1 - Flower Stamp (make your own command)

**Goal:** use `def` to make a new command, `flower(x, y, color)`, then use it
to stamp flowers all over the screen.

1. Open `starter.py` and press **Run** (F5). Nothing is drawn! Read the code:
   the recipe `def flower(x, y):` is there, but nobody ever **calls** it.
   (That is this week's bug hunt.)
2. At the bottom, call it three times, e.g. `flower(-200, 0)`. Run it.
3. All the flowers are orange. Give the recipe a third **parameter**:
   change the first line to `def flower(x, y, color):` and change
   `t.color("#E69F00")` to `t.color(color)`.
4. Now each call needs a color too: `flower(-200, 0, PALETTE[0])`,
   `flower(0, 0, PALETTE[6])`, `flower(200, 0, PALETTE[4])`.

**Done looks like:** at least 3 flowers, in at least 2 different colors,
each with a yellow middle.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a `size` parameter and use `t.circle(size)` for the petals.
Or make a meadow: call `flower` 10 times!
