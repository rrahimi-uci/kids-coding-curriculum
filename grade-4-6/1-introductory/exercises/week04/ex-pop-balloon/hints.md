## Hint 1: Where to look
You need two scripts on the Balloon. One starts the game when the flag is clicked. The other runs when the balloon is clicked. Look for the Variables category for `pops`.

## Hint 2: Try this
Use the **when this sprite clicked** block (Events category) for the second script. Inside it, use **change pops by** to count. For the surprise spot, drop **pick random** blocks (Operators category) into the slots of **go to x: y:** (Motion category).

## Hint 3: Almost there
The flag script has two blocks: one that sets the counter and one that puts the balloon in a starting place. The click script has three: one that changes the counter, a **start sound** block (Sound category), and one that moves the balloon to a random place using **pick random ____ to ____** twice.
