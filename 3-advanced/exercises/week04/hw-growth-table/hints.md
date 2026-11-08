## Hint 1: Where to look
Two functions need work: `linear_worst` and `halving_steps`. Read the sentence above each one. Linear search might look at every item, so ask yourself how many items that is. Then look at the `TODO 2` note.

## Hint 2: Try this
`linear_worst(n)` only needs to hand back a number it already has. For `halving_steps`, use a `while` loop that keeps going as long as `n` is above 0. Inside it, cut `n` in half with `//` and count one more step.

## Hint 3: Almost there
Start with `while n ____ 0:`. Inside the loop, halve `n` and count one more step. After the loop, give back `steps`. Try `n = 10` on paper first: 10, then 5, then 2, and keep going until you reach 0.
