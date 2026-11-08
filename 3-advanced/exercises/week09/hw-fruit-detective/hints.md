## Hint 1: Where to look
Run the program and see how `k = 1` and `k = 3` give different answers. Then look at the two TODOs. `k_nearest` should pick the closest cards. `vote` should pick the label that shows up the most.

## Hint 2: Try this
`sorted()` with `key=` lets you sort cards by a number you work out for each one, like a distance. A slice such as `my_list[:3]` keeps just the first few items. For `vote`, count each label in a dictionary. Then look for the label with the biggest count.

## Hint 3: Almost there
Sorting: `by_distance = sorted(training, key=lambda card: ____(card, ____))`, then `return by_distance[:____]`. Voting: `counts[label] = counts.get(label, ____) + 1` in a loop. Then start with `winner = labels[0]` and swap it when a label's count is `____` than `counts[winner]`.
