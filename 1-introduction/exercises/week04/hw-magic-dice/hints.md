## Hint 1: Where to look
Make two variables first: `roll` and `rolls`. One holds the number you just rolled. The other counts how many times you rolled. You need two scripts: one for the flag and one for the space key.

## Hint 2: Try this
Use **pick random** (Operators category) to choose the number and store it in `roll`. Use the **join** block (Operators category) to glue words and the `roll` variable together inside a **say** block. Use an **if** block for the sound.

## Hint 3: Almost there
The space script starts with **set roll to (pick random ____ to ____)**. Next, change `rolls` by a small number. Then **say (join "____ " (____))**. Last, an **if** block that checks whether `roll` is the lucky number, with a **start sound** inside. Remember the space after the words.
