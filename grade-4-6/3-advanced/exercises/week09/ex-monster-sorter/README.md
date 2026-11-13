# Exercise 9.1 - Monster sorter

**Goal:** build a tiny machine-learning program that sorts monsters into
**friendly** and **grumpy** by learning from example cards.

Each card has two **features** - `fluff` and `teeth` (0 to 10) - and a
**label**. To guess a mystery monster, find the training card that is
**nearest** on the chart and copy its label.

**Steps**

1. Open `starter.py`. Look at the `TRAINING` cards at the top.
2. TODO 1: finish `distance(a, b)`. Use the **steps distance**: pretend
   the monsters are game pieces on a grid that can only step across or up
   and down. The distance is the gap in fluff plus the gap in teeth.
   From `(5, 2)` to `(6, 1)` the gaps are 1 and 1, so it is 1 + 1 = 2 steps.
   `abs()` gives the gap between two numbers: `abs(2 - 5)` is 3, and
   `abs(5 - 2)` is 3 too.
3. TODO 2: finish `nearest(training, mystery)` - keep the closest card so
   far, just like finding the smallest number in a list.
4. Press **Run**. The chart shows friendly cards (circle, F) and grumpy cards
   (square, G). Each mystery monster (white circle, ?) has a line to its nearest neighbor and a guess.

**Done looks like:** the Shell shows

```
(5, 2) -> friendly
(3, 6) -> grumpy
(5, 5) -> friendly
```

Is `(5, 5)` really friendly? Count the steps from `(5, 5)` to `(7, 3)`, to
`(8, 4)` and to `(2, 6)`. What do you notice? Do you agree with the guess?

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add your own mystery monsters to `MYSTERY`.

**Extra for math fans:** grown-up AI often uses the straight "ruler"
distance instead. It uses a rule called Pythagoras, which you will learn in
middle school: `math.sqrt(gap_fluff * gap_fluff + gap_teeth * gap_teeth)`.
Try it. Do any of the guesses change?
