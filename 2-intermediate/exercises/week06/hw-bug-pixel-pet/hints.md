## Hint 1: Where to look
Read the red text from the bottom up to find bug 1. Then compare the rules in the README with each function: `feed()`, `play()` and `mood()`. Look closely at every word inside the quote marks.

## Hint 2: Try this
Dictionary keys must match exactly, including capital letters and spelling. A key that is not there causes a KeyError, and a misspelled key you assign to makes a new one. For `mood()`, think about what `and` means compared with `or`.

## Hint 3: Almost there
Run the program and compare the keys in the printed dictionary with the ones in `make_pet()`. Fix each key so it matches exactly. For bug 3, the rule says hungry `____` unhappy, so check whether the word between the two conditions in `mood()` says that.
