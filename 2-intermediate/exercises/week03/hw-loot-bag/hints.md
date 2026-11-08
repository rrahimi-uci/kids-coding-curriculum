## Hint 1: Where to look
The bag comes back empty because both loops are missing. Look at the two TODO lines in `fill_bag` and `count_item`. Each one needs a `for` loop.

## Hint 2: Try this
To repeat a set number of times, use `for _ in range(how_many):`. Inside it, `append` adds one item to the bag. To count, loop over the bag, use `if` to compare each thing to the item, and add 1 to `count` for each match.

## Hint 3: Almost there
Shape for filling: `for _ in range(____):` then `bag.append(____(chest))`. Shape for counting: `for thing in ____:` then `if thing == ____:` then `count = count + ____`. Keep `return` after the loop, not inside it.
