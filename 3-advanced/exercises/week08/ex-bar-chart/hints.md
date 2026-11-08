## Hint 1: Where to look
Run the program and look at the bars. They are all the same height because `bar_height()` ignores its inputs. After that, look inside the loop in `draw_bar_chart` for TODO 2 and TODO 3. `middle` is already worked out for you.

## Hint 2: Try this
For the height, make a fraction: this bar's `value` compared with the `biggest` value. Multiply that fraction by the tallest allowed height. For the labels, call `write_at()` with the turtle, an x, a y and some text. Turn each number into text with `str()` before you write it.

## Hint 3: Almost there
Height: `return ____ / ____ * MAX_HEIGHT`. Number label: `write_at(t, ____, BOTTOM + ____ + 5, str(____))`. Name label: `write_at(t, ____, BOTTOM - ____, ____)`. The x for both labels is the middle of the bar.
