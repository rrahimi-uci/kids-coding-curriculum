## Hint 1: Where to look
Run it and count the stripes. Only one shows up. Look at `draw_stripes` and see how many times `draw_stripe` is called. Also check how many colors `build_palette` makes.

## Hint 2: Try this
`palette.append(x)` adds one item to the end of a list. A `for` loop with `range(len(colors))` gives you each index number, one at a time. Use that index to pick a color with square brackets. `-1` means the last item.

## Hint 3: Almost there
Add with `palette.append("____")`. In the loop, use `for i in range(len(____)):`, then call `draw_stripe(...)` with `colors[____]` and `str(____)`. Then add `width` to `x`. Print with `palette[0]` and `palette[____]`.
