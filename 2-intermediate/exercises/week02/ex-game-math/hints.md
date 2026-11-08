## Hint 1: Where to look
Look at `xp_needed` first. It shows a number on its own line, and then your message says `None`. Ask yourself what `print` does with an answer and what `return` does.

## Hint 2: Try this
`print` only shows something on the screen. `return` hands a value back to the code that called the function. For `damage`, use an `if` to fix a number below zero. For `is_critical`, a comparison like `>=` already gives True or False.

## Hint 3: Almost there
Change the word `print(...)` to `return ____`. In `damage`, use `if result < ____:` and set `result` to a new number. Finish with `return ____`. For `is_critical`, write `return roll >= ____`.
