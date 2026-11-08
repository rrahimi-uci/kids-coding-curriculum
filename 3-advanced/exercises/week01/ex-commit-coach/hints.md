## Hint 1: Where to look
Find the five `TODO` comments in `starter.py`. Each one is a small job. Pick the first one and read its comment slowly. The comments already tell you what to compare.

## Hint 2: Try this
For the checks in `is_good_message`, use `if` with `return False`. Use `len(...)` to count characters, and `in` to ask whether something is inside a list. For `find_secrets`, use a `for` loop on `lines`, with a second loop inside it.

## Hint 3: Almost there
Each check has this shape: `if ____:` then `return False`. For `make_message`, join two pieces with `+` and put `" "` between them. For `find_secrets`, use `if ____ in lower:` then `found.append(____)`. Add `break` so a line is only added once.
