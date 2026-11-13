# Bug Hunt 3 - Word Finder (off-by-one binary search)

**Goal:** fix the 2 off-by-one bugs in `find_word`. When it works, Run
prints:

```
apple -> 0
dragon -> 3
lemon -> 11
zebra -> -1
```

**How to hunt:**

1. Press **Run**. Which words are found, which are not?
2. Do a **trace table** on paper for `find_word(["ant", "bee", "cat"], "ant")`:
   write `low`, `high` and `mid` for every loop. Why is "ant" not found?
3. Click **Debug** and step through the same search. Does the
   **Variables** view match your table?

**Hint:** the last index of a list with 12 items is not 12. And when
`low` and `high` are equal, there is still ONE word left to check.

**Check your work:** open `check_my_work.py` and press **Run**.
