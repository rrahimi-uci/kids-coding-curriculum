## Hint 1: Where to look
Start with `parse_line()`. A line from a file is always text, even the numbers. Look at what it returns right now and compare it to the list in its description.

## Hint 2: Try this
`int()` turns text like `"-150"` into a number you can do math with. After `parse_line()` works, `load_dots()` needs a `with open(...)` block and a `for` loop over the file. `save_dots()` is the same idea, but it writes.

## Hint 3: Almost there
Shapes to fill in: `with open(filename, "____") as file:` and then `for line in file:`. Use `line.strip()` to find empty lines. For saving, use `file.write(f"____,____,____,____\n")` for each dot. The `\n` ends the line.
