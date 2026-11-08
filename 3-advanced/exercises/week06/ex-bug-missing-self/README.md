# Bug Hunt 1 - Score Keeper (forgot self)

**Goal:** fix the 3 bugs in `starter.py`. When it works, Run prints:

```
Comet has 10 points
```

**How to hunt:**

1. Press **Run**. Read the LAST line of the red error. Which line number?
2. Click the **Debug** button (the bug icon, next to Run).
3. Press **Step into** (F7) to go inside a method, and **Step over** (F6)
   to run one line at a time. Watch the **Variables** view
   (menu **View > Variables**).
4. Fix one bug, run again, and repeat.

**Hint (only if you are stuck):** all three bugs are the same kind of
mistake. Inside a class, the object's own data is always reached
through... `self`.

**Check your work:** open `check_my_work.py` and press **Run**.
