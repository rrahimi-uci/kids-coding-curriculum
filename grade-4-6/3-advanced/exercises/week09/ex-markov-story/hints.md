## Hint 1: Where to look
Look at `build_chain` and its TODO. The story is just "the" because the chain is empty. Read the example in the README: each word points to a list of the words that came right after it.

## Hint 2: Try this
Go through the words with a `for i in range(...)` loop that stops one short of the end, because the last word has nothing after it. In each step, `words[i]` is the current word and `words[i + 1]` is the one after it. A dictionary can hold a list for each word. Use `.append()` to add to that list.

## Hint 3: Almost there
Inside the loop, name the current word and the next word. If the current word is not in `chain` yet, give it an empty list. Then add the next word to its list. Should that last step be inside the `if` or outside? Think about repeats.
