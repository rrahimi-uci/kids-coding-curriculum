# Bug Hunt 2 - Lost Scores (the sort that loses items)

**Goal:** fix the 3 bugs in `sort_scores`. When it works, Run prints:

```
Sorted:   [10, 10, 30, 40, 50]
Original: [40, 10, 30, 10, 50]
```

**How to hunt:**

1. Press **Run** and compare with the expected output. What is missing?
2. Click **Debug**. Press **Step over** (F6) again and again. In the
   **Variables** view, watch `remaining`, `result` AND `scores`.
3. Ask: when does the loop stop? Is something left behind? What happens
   to the second 10? Why does `scores` shrink too?

**Check your work:** open `check_my_work.py` and press **Run**.
