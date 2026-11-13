## Hint 1: Where to look
Read `parse_line` first, since it is already done. It turns one line into a pair: the commit id and the message. The other three jobs all start by turning the whole text into a list of those pairs.

## Hint 2: Try this
`text.splitlines()` gives you a list of lines. Loop over it, skip any line that is empty, and use `parse_line` on the rest. For the later jobs, call `parse_log(text)` instead of repeating yourself. Lists have a `.reverse()` method.

## Hint 3: Almost there
Unpack each pair in the loop like this: `for ____, ____ in parse_log(text):`. Then use `if` to test the message, and `.append(____)` to collect the right piece. For the last job, collect first, then reverse the list before you `return`.
