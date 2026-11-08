## Hint 1: Where to look
The bag comes back empty because both loops are missing. Look at the two TODO lines in `fill_bag` and `count_item`. Each one needs a `for` loop.

## Hint 2: Try this
To repeat a set number of times, use `for _ in range(____):` with the number you were given. Inside it, `append` adds one item to the bag. To count, loop over the bag, use `if` to compare each thing to the item, and add 1 to `count` for each match.

## Hint 3: Almost there
For filling, append the item that `open_chest` gives you. For counting, use `for thing in ____:`, then `if thing == ____:`, then make `count` one bigger. Keep `return` after the loop, not inside it.
