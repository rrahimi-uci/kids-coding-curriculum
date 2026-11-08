# Exercise 9.1 - Square of Any Size

**Goal:** the program asks "How big?" and draws a square that size.

1. Open `starter.py` and press **Run** (F5).
2. Click in the **Shell** (the bottom part of Thonny), type `120` and press
   **Return**. Oh no - a red error! This is the bug hunt.
3. The clue: `input` always gives back **text**, like `"120"`, not the number
   `120`. The turtle cannot walk `"120"` steps.
4. Fix it: turn the text into a number with `int(...)`:
   `size = int(answer)`
5. Run it again and try different sizes: 50, 150, 250.

**Done looks like:** whatever number you type, the turtle draws a square with
sides that long.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** ask a second question, "How thick is the pen? (1 to 10)", and use
the answer in `t.pensize(...)`.
