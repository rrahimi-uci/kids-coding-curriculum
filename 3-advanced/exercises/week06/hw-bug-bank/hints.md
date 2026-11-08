## Hint 1: Where to look
Run it and compare the output with the expected output. Check the coins line first, then count the lines under it. Each of the three bugs is in a different method.

## Hint 2: Try this
Use Debug and Step over, and watch `self.coins` and `self.log` in the Variables view. After the first deposit, and again after the second, ask whether the total is what you expect. Then check whether taking out all the coins works.

## Hint 3: Almost there
Check three spots. In `deposit`, follow `self.coins` after each deposit: is the total what you expect? In `withdraw`, test the sign in `amount >= self.coins` with exactly all the coins. In `statement`, check which log lines `range(len(self.log) - 1)` skips.
