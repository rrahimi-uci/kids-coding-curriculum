## Hint 1: Where to look
Look at the top of `starter.py` for the three TODOs. `save_score()` is the first one. It has to put a line in the file so the game can remember it next time.

## Hint 2: Try this
`open(filename, "a")` opens a file so new text is added at the end. `file.write(...)` puts text in it. For reading, `line.strip()` removes the hidden newline, and `split(",")` cuts a line into pieces.

## Hint 3: Almost there
Use `with open(filename, "____") as file:` then `file.write(f"{____},{____}\n")`. When reading, turn the second piece into a number with `int(parts[____])`. Missing file? Open it with `"____"` and write nothing.
