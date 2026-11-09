## Hint 1: Where to look
Read the top of `cipher_tools.py`. It shows what `encode()` does when letters wrap around and when there are spaces or symbols. Your cipher wheel can check each answer.

## Hint 2: Try this
Each test needs an `assert` line that calls `encode()` and compares the result to the answer you worked out by hand. Use `==` to compare. Strings go inside quotes, so the secret message does too.

## Hint 3: Almost there
Shape to fill in: `assert encode("____", 3) == "____", "message"`. For the wrap test, work out where `x`, `y` and `z` land after moving 3 places. For the symbols test, include a space and a `!` in the message and check that they stay put.
