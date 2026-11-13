## Hint 1: Where to look
Both TODOs are in the two file functions near the top. When you type `a`, the idea only lives in memory. It needs to go into the file. When you type `l`, the program needs to read the file back.

## Hint 2: Try this
Open the file with `"a"` to add to the end. Reading needs `try:` and `except FileNotFoundError:`. That way the program does not crash on the very first run, when the file does not exist yet.

## Hint 3: Almost there
Shapes to fill in: `with open(filename, "____") as file:` and `file.write(____ + "\n")`. For loading, put `with open(filename, "r")` and a `for line in file:` loop inside `try:`. In the `except` part, open the file with `"____"`.
