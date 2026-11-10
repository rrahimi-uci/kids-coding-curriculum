# Exercise 8.2 - Test the Best Score

**Goal:** write tests that catch bugs hiding at the edges.

`best_score(scores)` in `score_tools.py` finds the highest score in a list.
It is correct. Your job is to write tests that would catch it if somebody
broke it one day.

1. Read `score_tools.py`. What should `best_score([])` give?
2. Open `starter.py`. One normal test is done for you. Press **Run**: pytest
   says `PASSED` for every test. (The empty ones pass too: a test with no
   `assert` checks nothing!)
3. **TODO 1** test the empty list. **TODO 2** test a list where the best
   score is the last one. **TODO 3** write one more edge-case test.
4. Press **Run** again. Every test should say `PASSED`.

**Done looks like:** at least 3 tests, all `PASSED`.

**Check your work:** open `check_my_work.py` and press **Run**. It tries your
tests on three BROKEN versions of `best_score()`. Your tests should catch
(fail on) every one of them. When they do, it says
`Amazing! All 5 checks passed.`

**Edge cases to think about:** an empty list, one item, the first item, the
last item, all the same.
