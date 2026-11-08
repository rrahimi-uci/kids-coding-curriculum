## Hint 1: Where to look
Two sprites take turns, like actors passing a note. Look at the Events category. Find the block that sends a message and the block that waits for one.

## Hint 2: Try this
One sprite uses **broadcast**, which sends a message. The other sprite starts its script with **when I receive**, which listens. A message only works if the listener picks the very same name that was sent.

## Hint 3: Almost there
If the dancer does nothing, click the dropdown on its **when I receive** block and look at the name. Compare it, letter by letter, with the name in the **broadcast** block. Do they match? Then build the dance with **repeat ____**, **next costume** and **wait ____ seconds**.
