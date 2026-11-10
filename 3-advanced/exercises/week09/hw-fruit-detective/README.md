# Homework 9 - Fruit detective

**Goal:** make your classifier harder to fool by letting the **k nearest**
cards vote.

One card in `TRAINING` has the wrong label - a lemon was labeled "apple".
With **k = 1** the classifier trusts the single closest card, mistakes and
all. With **k = 3** the three closest cards vote, so one wrong card is
outvoted.

1. **Core** - TODO 1: finish `k_nearest(training, point, k)`. Sort the
   cards by distance (remember `sorted(..., key=...)` from week 5) and keep
   the first `k`.
2. **Core** - TODO 2: finish `vote(labels)` with a counting dictionary.
3. Press **Run**. (Distance is the steps distance from Exercise 9.1:
   gap in size + gap in sweetness. It is already written for you.)

**Done looks like:** the Shell shows
```
Closest 3 cards: [(5, 3, 'apple'), (5, 2, 'lemon'), (4, 2, 'lemon')]
k = 1 says: apple
k = 3 says: lemon
(7, 7) -> apple
(2, 8) -> grape
(6, 2) -> lemon
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Challenge:** what happens with k = 13 (every card votes)? Why is a very
big k a bad idea too?
