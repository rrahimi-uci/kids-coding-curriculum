## Hint 1: Where to look
Read the traceback bottom up and find the function name and line number. Then draw the list on paper with its index numbers, like the picture in the README. Count carefully where the list starts and ends.

## Hint 2: Try this
An IndexError means you asked for a spot that is not in the list. A list of 4 items has indexes 0 to 3, so `len` is one more than the last index. For bug 2, print `best` and compare its length with how many times the loop runs.

## Hint 3: Almost there
For bug 1, the last item can be reached with a negative index, or with `len(in_order) ____ 1`. For bug 2, `range(3)` always runs three times. Try `range(____)` with something that tells you how many scores are really in `best`.
