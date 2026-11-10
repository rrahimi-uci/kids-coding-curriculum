## Hint 1: Where to look
Run it and see which words are found and which are not. Then look at the lines that set up the search, right before the loop and at the top of the loop. Think about the very last word in the list.

## Hint 2: Try this
Counting from 0, a list of 3 items has indexes 0, 1 and 2. Write a trace table on paper for `["ant", "bee", "cat"]` and `"ant"`. Add columns for `low`, `high` and `mid`, and fill in one row per loop.

## Hint 3: Almost there
Look at the starting value of `high`. Counting from 0, is it the index of the last word? Then think about the loop condition. When `low` and `high` are the same number, is there still one word left to look at? Try your trace table again after each change.
