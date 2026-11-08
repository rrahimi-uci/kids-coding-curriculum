## Hint 1: Where to look
Run the program and read the line "First row now looks like". The nickname is still there because `anonymize` hands back the original `rows`. Look at the Core TODO first, and leave the Challenge for later.

## Hint 2: Try this
Build a brand new dictionary for each row, so the old one is never copied whole. Start it with an `id`. Then use a loop over the `keep` list to copy only those columns. An f-string like `f"R{number}"` can build the ID text.

## Hint 3: Almost there
Loop over the rows with `enumerate`, counting from ____. Build a small dictionary that starts with the `id`. Loop over `keep` and copy each column from the old row. Add the new dictionary to `safe_rows` and return it. For the Challenge, follow the steps in the TODO 2 comments.
