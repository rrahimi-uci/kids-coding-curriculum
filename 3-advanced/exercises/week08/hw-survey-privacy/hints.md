## Hint 1: Where to look
Run the program and read the line "First row now looks like". The nickname is still there because `anonymize` hands back the original `rows`. Look at the Core TODO first, and leave the Challenge for later.

## Hint 2: Try this
Build a brand new dictionary for each row, so the old one is never copied whole. Start it with an `id`. Then use a loop over the `keep` list to copy only those columns. An f-string like `f"R{number}"` can build the ID text.

## Hint 3: Almost there
Shape: `for number, row in enumerate(rows, start=____):`, then `safe = {"id": f"R{____}"}`, then `for column in ____:` with `safe[column] = row[____]`. Finish with `safe_rows.____(safe)` and return `safe_rows`. For the Challenge, look up `csv.DictWriter`, `writeheader()` and `writerows()`.
