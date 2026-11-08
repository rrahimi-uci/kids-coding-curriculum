## Hint 1: Where to look
The game says "I have no words yet!" because `load_words()` gives back an empty list. Start there. Then look at `show_progress()`, which builds the `_ _ _` picture one letter at a time.

## Hint 2: Try this
Open the file in `"r"` mode with a `with` block and loop over its lines. Clean each line with `strip()` and `lower()`. In `show_progress()`, use `if letter in guessed:` to choose between the letter and an underscore.

## Hint 3: Almost there
Shapes to fill in: `for line in file:`, then `word = line.____().____()`, then an `if` that checks the word is not empty, and `words.append(____)`. For the progress, think about what to add to `shown` when the letter was guessed, and what to add when it was not.
