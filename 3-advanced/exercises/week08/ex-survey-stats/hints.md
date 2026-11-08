## Hint 1: Where to look
Work on one TODO at a time and run the program after each one. Read the example in each function's docstring (the text in triple quotes). It shows what the finished function should give back.

## Hint 2: Try this
A dictionary works like a tally chart. Use `counts.get(value, 0)` to read a count, which gives 0 if the value is new. For the average, use `sum()` and `len()`, and check for an empty list first. For `most_popular`, keep a `best` key and swap it when a bigger count shows up.

## Hint 3: Almost there
Tally: `counts[value] = counts.get(value, ____) + ____`. Average: check for an empty list first, then divide `____` by `____` and round to 1 place. Winner: loop over `counts` and compare each key's count with the count of `best`. Decide when `best` should change.
