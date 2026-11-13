## Hint 1: Where to look
Open your `apple-catch` project and click the Apple. You are adding a second counter, so look in the Variables category and at the missed-apple **if** block.

## Hint 2: Try this
Make a variable named `lives`. Set it at the start of the game, just like `score`. Lose a life only in the **if** block for a missed apple, not in the catch block. Then add a new **if** at the bottom of the **forever** loop to check for zero lives.

## Hint 3: Almost there
The game-over check is an **if** block (Control category) with an **=** block (Operators category) and the `lives` variable in it. Inside it, put a **say** block (Looks category), then **stop all** (Control category). Use **set lives to ____** and **change lives by ____**.
