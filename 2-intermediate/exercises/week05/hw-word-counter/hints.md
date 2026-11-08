## Hint 1: Where to look
Run the program. Every word says 1, even `the`, which shows up three times. Look at the line `counts[word] = 1` and ask yourself what it does when the word was already counted.

## Hint 2: Try this
Use `in` to ask whether the word is already a key in the dictionary. If it is, make its number bigger. If it is not, give it a starting value. For `most_common()`, use an `if` to compare each `count` with `best_count`.

## Hint 3: Almost there
Ask `if ____ in counts:` and make that word's count go up by one step. In the `else:` part, give a new word its first count. In `most_common()`, use `if count > ____:` and set both `best_word` and `best_count` inside it.
