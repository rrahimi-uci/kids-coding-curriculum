## Hint 1: Where to look
Read the red error from the bottom up. It names a line in `last_item`. Then look at the boxes picture in the README. What is the number of the last box compared to `len`?

## Hint 2: Try this
List positions start at 0, so a list of 4 items ends at index 3. For `add_item`, a list has a method that adds one item to the end. For `has_item`, use a `for` loop to look at each thing and `return True` when one matches.

## Hint 3: Almost there
Use `backpack.append(____)`. For the loop, write `for thing in ____:` then `if thing == ____:` and `return True`. After the loop, `return False`. For the crash, change the index to `len(backpack) ____ 1`.
