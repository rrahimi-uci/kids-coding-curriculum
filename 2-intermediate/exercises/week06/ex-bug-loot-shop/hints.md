## Hint 1: Where to look
Run it and compare the output with your paper answers. Each of the three functions has one bug, so check them one at a time. Start with `total_price()`: is it adding all three prices?

## Hint 2: Try this
Add `print()` lines inside the loop to see what happens each round. Read each function out loud, line by line. Ask: does the loop finish before the function hands back its answer? Does `return` give back the right variable?

## Hint 3: Almost there
Check where the `return` sits compared with the `for` line, since the indent decides when it runs. In `cheapest()`, return the variable the loop worked on, not `prices[____]`. In `can_buy()`, `print` only shows a value, so use `____` to give it back.
