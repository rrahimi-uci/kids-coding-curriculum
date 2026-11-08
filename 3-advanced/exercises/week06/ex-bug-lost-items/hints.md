## Hint 1: Where to look
Run it and compare with the expected output. Which numbers are missing? Also look at the second line. The original list should still have all 5 scores, but it does not.

## Hint 2: Try this
Use the Thonny debugger and press Step over again and again. Watch `remaining`, `result` and `scores` in the Variables view. Ask: when does the loop stop? And what does `remaining = scores` really do to the list?

## Hint 3: Almost there
Look at three lines. First, `remaining = scores` gives the same list a second name. Python can make a separate copy of a list. Second, check the `while` condition for the last item. Third, read the `if smallest not in result:` line and think about the two 10s.
