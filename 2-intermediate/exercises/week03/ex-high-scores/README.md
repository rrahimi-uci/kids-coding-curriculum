# Exercise 3.3 - Top 3 High Scores

**Goal:** keep a list of scores and print only the best three.

Two new list tricks:

* `sorted(scores, reverse=True)` makes a new list, biggest first.
* `best[:3]` takes the first three items. If there are fewer, it takes them all.

1. Open `starter.py` and press **Run**. The "top three" are not the best!
2. **TODO 1:** sort first, then take three.
3. **TODO 2:** print `1st: 300`, `2nd: 120`, `3rd: 80`. Use the `places` list.

**Done looks like:**

```
1st: 300
2nd: 120
3rd: 80
What did you score this time? 500
New leaderboard:
1st: 500
2nd: 300
3rd: 120
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** store a made-up nickname with each score, e.g. print `1st: 300 (Comet)`.
