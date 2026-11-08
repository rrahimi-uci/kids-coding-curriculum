## Hint 1: Where to look
Run it and see which words are found. Then look at the two lines that set up the search: `high = ...` and `while ...`. Both are about the very last word in the list.

## Hint 2: Try this
Counting from 0, a list of 3 items has indexes 0, 1 and 2. Write a trace table on paper for `["ant", "bee", "cat"]` and `"ant"`. Add columns for `low`, `high` and `mid`, and fill in one row per loop.

## Hint 3: Almost there
Check `high = len(words)`. Is that the index of the last word? Then check `while low < high:`. When `low` and `high` are the same number, is there still one word left to look at? Compare the comparison sign with `<` and `<=`.
