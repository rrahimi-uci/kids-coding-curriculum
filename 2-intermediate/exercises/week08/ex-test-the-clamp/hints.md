## Hint 1: Where to look
Look at the first test in `starter.py`. It is finished, so copy its pattern. Then read the examples at the top of `clamp_tools.py` to work out the right answers for your own tests.

## Hint 2: Try this
Each test needs an `assert` line. It calls `clamp()` with numbers you choose and checks the answer using `==`. Work out the right answer by hand first. Then write it after the `==`.

## Hint 3: Almost there
Shape to fill in: `assert clamp(____, 0, 10) == ____, "message"`. For a too-big value, pick a number above 10. For a value on a limit, use 0 or 10 as the first number. A new test needs a name that starts with `test_`.
