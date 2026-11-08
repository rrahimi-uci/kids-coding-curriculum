## Hint 1: Where to look
Read the three `TODO` comments in `starter.py`. A dictionary stores each value under a name, called a key. Run the program and see which part is still empty.

## Hint 2: Try this
`monster.items()` gives you each key with its value, so a loop can use both. An f-string like `f"{____}: {____}"` builds a line of text. To avoid a KeyError, check that the stat is in the monster before you look it up.

## Hint 3: Almost there
In `stat_report()`, use `lines.append(____)` inside the loop. In `level_up()`, copy the pattern of the `level` line: `monster["health"] = monster["health"] + ____`. In `get_stat()`, only look the stat up when your check passes. Otherwise give back the value the docstring names.
