# Homework 4 - Slime Battle

**Goal:** write two `while` loops: one that counts, one that checks answers.

1. Open `starter.py` in Thonny.
2. **TODO 1:** finish `hits_needed()`. Before you code, fill in this trace
   table on paper for `hits_needed(30, 7)`:

| health | hits |
|---|---|
| 30 | 0 |
| 23 | 1 |
| | |

3. **TODO 2:** make `ask_yes_no()` keep asking until the answer is yes or no.
4. Run it. Type `maybe` first: it should ask again.

**Done looks like:**

```
A wobbly slime appears! It has 30 health.
With a sword that does 5 damage you need 6 hits.
With a sword that does 7 damage you need 5 hits.
With a sword that does 12 damage you need 3 hits.
Fight another slime? (yes/no) maybe
Please type yes or no.
Fight another slime? (yes/no) no
You wave goodbye to the slime.
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Stuck in a loop?** Press the red **Stop** button in Thonny. Then check:
does something inside the loop change, so the loop can end?
