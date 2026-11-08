## Hint 1: Where to look
Look at `build_chain` and its TODO. The story is just "the" because the chain is empty. Read the example in the README: each word points to a list of the words that came right after it.

## Hint 2: Try this
Go through the list of words with `for i in range(len(words) - 1):`. In each step, `words[i]` is the current word and `words[i + 1]` is the one after it. A dictionary can hold a list for each word. Use `.append()` to add to that list.

## Hint 3: Almost there
Inside the loop: `word = words[____]`, then `next_word = words[____]`. Then `if word not in chain:` start a fresh list with `chain[word] = ____`. After the `if`, `chain[word].____(next_word)`. The `append` goes outside the `if`, so repeats are kept.
