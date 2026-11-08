## Hint 1: Where to look
You have two TODOs: `label_counts` and `accuracy`. Look at `classify`, which is already written. It takes the training pile and one card, and gives back a guess. Each card is a group of three things: fluff, teeth and label.

## Hint 2: Try this
`label_counts` is a tally chart, just like `count_by` from week 8. Count each card's label in a dictionary. For `accuracy`, loop over the test cards and keep a score in `correct`. Add 1 whenever the guess matches the card's real label.

## Hint 3: Almost there
Tally: `label = card[____]`, then `counts[label] = counts.get(label, ____) + 1`. Score: loop over the test cards, ask `classify` for a guess using the training pile, and compare it with the card's real label. Add 1 to `correct` when they match. Count from 0 to find the label's place on a card.
