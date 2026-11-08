## Hint 1: Where to look
Read the red error from the bottom up. It names a line in `last_item`. Then look at the boxes picture in the README. What is the number of the last box compared to `len`?

## Hint 2: Try this
List positions start at 0, so a list of 4 items ends at index 3. For `add_item`, a list has a method that adds one item to the end. For `has_item`, use a `for` loop to look at each thing and `return True` when one matches.

## Hint 3: Almost there
Use `backpack.append(____)`. For the loop, write `for thing in ____:` and compare `thing` with the item. After the loop, return the other answer. For the crash, work out which index the last box has when `len` is 4, then change the index so it lands there.
