# Homework 6 - Pixel Pet (bug hunt)

**Goal:** use your debugging strategies to fix **three** bugs in a
virtual pet program.

The rules:

* `feed()`: hunger goes down by 3 (never below 0).
* `play()`: happiness goes up by 2 and hunger goes up by 1.
* `mood()`: the pet is "grumpy" if hunger is 8 or more **or** happiness is
  2 or less. Otherwise it is "happy".

1. Open `starter.py` and press **Run**. Read the traceback bottom-up: bug 1.
2. After bug 1 is fixed, look at the printed dictionary. Does it have a key
   it should not have? That is bug 2.
3. Bug 3 does not crash. Look at the last line: Biscuit has hunger 9.
   What do the rules say Biscuit should feel? Read `mood()` out loud and
   compare it with the rules.

**Done looks like:**

```
{'name': 'Pixel', 'hunger': 4, 'happiness': 9}
Pixel feels happy.
Biscuit feels grumpy.
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Write a bug report** for each bug on your homework sheet.
