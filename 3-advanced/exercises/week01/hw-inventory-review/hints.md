## Hint 1: Where to look
Look at the three functions with a `TODO`. Each one loops over `items`. Compare the list you get back with the "You should see" lines in the README. Does yours match?

## Hint 2: Try this
Use a `for` loop to visit each item, then `if` to compare it with `name`. Use `==` to ask "is it equal?" and `!=` to ask "is it different?". For `most_common`, `tally(items)` already counts everything for you.

## Hint 3: Almost there
Counting and filtering share this shape: `for ____ in items:` then `if ____ ____ name:`. Inside, either add `1` to `count` or `kept.append(____)`. For `most_common`, loop with `for ____, ____ in tally(items).items():` and compare `count` with `best_count`.
