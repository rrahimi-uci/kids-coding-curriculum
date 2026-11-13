## Hint 1: Where to look
Look at the bottom of `starter.py`. The recipe called `flower` is written, but nothing ever uses it, so the screen stays empty. Making a recipe and using it are two different jobs.

## Hint 2: Try this
To use a recipe, write its name followed by parentheses with the values inside. Each call puts a flower in a new spot. For colors, give the recipe a third slot in its first line, and use that slot instead of the fixed color inside.

## Hint 3: Almost there
A call looks like `flower(____, ____, PALETTE[____])`. The first two blanks are where the middle goes. The last is a spot in the list, counting from 0. The recipe's first line needs `color` added, and `t.color( )` needs to use it.
