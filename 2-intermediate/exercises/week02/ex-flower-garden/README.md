# Exercise 2.2 - Flower Garden

**Goal:** use **parameters** so one function draws many different flowers,
and a function that **returns** the turning angle.

1. Open `starter.py` and press **Run**. All three flowers land on top of
   each other and have the wrong number of petals.
2. **TODO 1:** `petal_turn()` should return `360 / petals`.
3. **TODO 2 and 3:** use `t.goto(x, y)` so each flower appears where it was asked to.
4. **TODO 4:** repeat once for each petal: `range(petals)`.

**Done looks like:** three flowers side by side: 5, 8 and 12 petals, each
with a green stem and a yellow middle.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add more flowers with different sizes. Can you make a whole
row with a `for` loop? Try `for x in range(-200, 201, 100):`
