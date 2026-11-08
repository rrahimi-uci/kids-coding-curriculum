# Bug Hunt 4 - Shape Party (inheritance bugs)

**Goal:** fix the 3 bugs so 4 hexagons and 3 diamonds (squares standing on
a corner) appear in 7 colours.

**How to hunt** - the bugs show up one after another:

1. Press **Run**. The window opens, but NOTHING is drawn and there is no
   error. A silent bug! Click **Debug** and **Step into** `draw_party`.
   Does Thonny ever go inside a `draw` method? (Hint: how do you CALL a
   method?)
2. Fix it and run again. Now it crashes. Read the last line of the red
   error. Which attribute is missing? Which `__init__` should have set it?
3. Fix it and run again. Look closely: are the diamonds really diamonds,
   or plain dots? Compare the method names in `Diamond` and `Shape`
   letter by letter.

**Check your work:** open `check_my_work.py` and press **Run**.
