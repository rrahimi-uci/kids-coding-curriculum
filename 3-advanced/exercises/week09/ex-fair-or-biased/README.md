# Exercise 9.2 - Fair or biased?

**Goal:** test how good the monster sorter really is - and see how
**biased training data** makes it worse.

To test a learning program fairly, split the cards into two piles:

* a **training** pile it learns from, and
* a **test** pile it never sees while learning. We use it to mark the guesses.

**Accuracy** = correct guesses / number of test cards.

**Math helper:** the program shows accuracy as a **percent**, which means
"out of 100". 4 right out of 4 is 100% (all of them). 2 right out of 4 is
50% (half). 3 out of 4 is 75%.

**Steps**

1. Open `starter.py`. The classifier from Exercise 9.1 is already there.
2. TODO 1: finish `label_counts(cards)` - how many friendly, how many grumpy?
3. TODO 2: finish `accuracy(training, test)`.
4. Press **Run** and compare the fair and the biased training piles.

**Done looks like:** among the lines in the Shell you see
```
Training pile: 12 cards {'friendly': 6, 'grumpy': 6}
Fair training   -> accuracy 100%
Biased pile:    {'friendly': 1, 'grumpy': 8}
Biased training -> accuracy 50%
```
and then one line for each of the 4 test cards with the biased guess.

**Check your work:** open `check_my_work.py` and press **Run**.

**Think:** the biased pile only had one friendly monster. Who could be
treated unfairly if a real app learned from unbalanced examples like this?
