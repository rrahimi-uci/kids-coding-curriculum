## Hint 1: Where to look
Read the traceback bottom up and find the function name and line number. Then draw the list on paper with its index numbers, like the picture in the README. Count carefully where the list starts and ends.

## Hint 2: Try this
An IndexError means you asked for a spot that is not in the list. A list of 4 items has indexes 0 to 3, so `len` is one more than the last index. For bug 2, print `best` and compare its length with how many times the loop runs.

## Hint 3: Almost there
For bug 1, compare the index used in `highest()` with the last index in your drawing. For bug 2, the loop runs three times even when `best` holds only two scores. What could the loop use instead of a fixed number?
