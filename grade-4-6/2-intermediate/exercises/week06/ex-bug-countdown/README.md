# Bug Hunt Station 3 - Rocket Countdown (infinite loop)

**Goal:** find out why the loop never ends, using a **trace table**.

1. Open `starter.py` and press **Run**. The rocket never launches. After a
   moment the **safety net** stops the loop with a `RuntimeError`.
   (Without a safety net, you would press the red **Stop** button.)
2. Make a trace table on paper. Follow the code line by line and write down
   the value of each variable every time through the loop:

| round | n | numbers |
|---|---|---|
| 1 | 5 | [5] |
| 2 | | |
| 3 | | |

3. What should change every time through the loop, but never does? Fix it.

**Done looks like:**

```
5...
4...
3...
2...
1...
LIFT OFF!
```

**Check your work:** open `check_my_work.py` and press **Run**.
