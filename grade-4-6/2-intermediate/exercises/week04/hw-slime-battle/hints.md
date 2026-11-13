## Hint 1: Where to look
Do the trace table on paper first for `hits_needed(30, 7)`. Watch how `health` and `hits` change each round. Then read the `TODO` comments in `starter.py`.

## Hint 2: Try this
Use a `while` loop that keeps going as long as the slime still has health. Inside it, two things change every round. For `ask_yes_no()`, use `while True:` and `return` only when the answer is good.

## Hint 3: Almost there
Try `while health ____ 0:` and, inside it, change `health` and `hits`. For the second function, use `while True:`, then `if answer == ____ or answer == ____:` with `return answer`. Otherwise print the "Please type yes or no." message.
