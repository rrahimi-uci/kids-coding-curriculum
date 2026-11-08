## Hint 1: Where to look
Run the program. Right now both `k = 1` and `k = 3` say apple, but a working version makes them differ. Then look at the two TODOs. `k_nearest` should pick the closest cards. `vote` should pick the label that shows up the most.

## Hint 2: Try this
`sorted()` with `key=` lets you sort cards by a number you work out for each one, like a distance. A slice such as `my_list[:3]` keeps just the first few items. For `vote`, count each label in a dictionary. Then look for the label with the biggest count.

## Hint 3: Almost there
Sorting: use `sorted(training, key=lambda card: ____(card, ____))`, then slice off the first `k`. Voting: in a loop, `counts.get(label, ____) + 1` builds the tally. Then walk through the labels and change `winner` when another label's count beats the current winner's.
