# Exercise 9.1 - Monster sorter

**Goal:** build a tiny machine-learning program that sorts monsters into
**friendly** and **grumpy** by learning from example cards.

Each card has two **features** - `fluff` and `teeth` (0 to 10) - and a
**label**. To guess a mystery monster, find the training card that is
**nearest** on the chart and copy its label.

**Steps**

1. Open `starter.py`. Look at the `TRAINING` cards at the top.
2. TODO 1: finish `distance(a, b)` with Pythagoras:
   `math.sqrt(dx * dx + dy * dy)`.
3. TODO 2: finish `nearest(training, mystery)` - keep the closest card so
   far, just like finding the smallest number in a list.
4. Press **Run**. The chart shows friendly cards (circle, F) and grumpy cards
   (square, G). Each mystery monster (white circle, ?) has a line to its nearest neighbor and a guess.

**Done looks like:** `(5, 2) -> friendly` and `(3, 6) -> grumpy`.
What does the program guess for `(5, 5)`? Do you agree?

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add your own mystery monsters to `MYSTERY`.
