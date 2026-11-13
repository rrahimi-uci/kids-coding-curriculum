# Exercise 8.3 - Fix the Bugs the Tests Found

**Goal:** use failing tests as a map to find and fix four bugs.

`starter.py` has four small game helpers. Each one has ONE bug. This time
the tests are already written for you: they are in `test_fix_the_bugs.py`.

1. Open `check_my_work.py` and press **Run**. Some checks say
   **TRY AGAIN**. Read each hint: it says what was expected and what
   happened.
2. Open `test_fix_the_bugs.py` and find the failing test. Read it like a
   sentence: "lives_after_hit(1, 5) should be 0".
3. Open `starter.py`, find that function and fix ONE bug.
4. Run `check_my_work.py` again. One more check should say **PASS**.
5. Repeat until every check passes.

**Done looks like:** `Amazing! All 5 checks passed.`

**Rules of the bug hunt:**

- Fix the function, never the test. The test describes what the function
  SHOULD do.
- Change one thing at a time, then run the checks again.

**Hint words:** `>=` (more than or equal), `return`, `if len(scores) == 0:`.

**Math helper - the average:** add up all the scores, then divide by how
many scores there are. For 10, 20 and 40: 10 + 20 + 40 = 70, and 70 / 3 is
23.33..., which `round()` turns into 23. With no scores at all you would
divide by 0, which is impossible: Python crashes with `ZeroDivisionError`.

**Before you start:** press **Run** on `starter.py`. It prints a few lines,
and some are wrong (it even prints `None` and then crashes). Each wrong line
is a clue. The comment on each line says what it SHOULD print.
