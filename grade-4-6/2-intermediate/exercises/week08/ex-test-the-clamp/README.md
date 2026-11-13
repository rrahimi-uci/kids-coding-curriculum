# Exercise 8.1 - Test the Clamp

**Goal:** write your first pytest tests, and learn to read PASSED and FAILED.

`clamp(value, low, high)` in `clamp_tools.py` keeps a number between two
limits. Games use it to stop a player walking off the screen:
`clamp(99, 0, 10)` gives `10`.

`-3` means "minus three": 3 below zero. It is smaller than 0, so
`clamp(-3, 0, 10)` goes UP to `0`.

1. Install pytest once (ask an adult): **Tools > Manage packages...**,
   type `pytest`, click **Search on PyPI**, click `pytest` in the results,
   then **Install**. No account needed.
2. Read `clamp_tools.py`. Do not change it: it is correct.
3. Open `starter.py`. This is YOUR test file. Press **Run**. You will see one
   line per test, ending in `PASSED` or `FAILED`.
4. **TODO 1** and **TODO 2**: write an `assert` line in each empty test.
5. **TODO 3**: write a fourth test for a value exactly on a limit.
6. Try it: change one expected answer to something wrong and press **Run**.
   Read the `FAILED` message. Then change it back.

**Done looks like:**

```text
starter.py::test_middle_value_stays_the_same PASSED
starter.py::test_too_small_goes_up_to_low PASSED
starter.py::test_too_big_comes_down_to_high PASSED
...
```

**The programmer way:** press **Run** once first, then choose
**Tools > Open system shell...** and type
`python -m pytest starter.py -v` and press Return. (If it says
"command not found", type `python3` instead of `python`.)

**Check your work:** open `check_my_work.py` and press **Run**. It tries your
tests on three BROKEN versions of `clamp()`. Good tests catch every one.
It also checks that one of your tests uses a value exactly ON a limit (TODO 3).
Careful: `check_my_work.py` tests YOUR TESTS. To run your tests themselves,
press **Run** in `starter.py`.
