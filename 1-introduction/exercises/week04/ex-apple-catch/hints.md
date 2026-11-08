## Hint 1: Where to look
Read the Bowl script and the Apple script separately. The Bowl only follows the mouse. The Apple does the falling, the counting, and the restarting.

## Hint 2: Try this
Inside the Apple's **forever** loop, use two **if** blocks from the Control category. One asks if the apple touches the bowl (Sensing category). The other asks if the apple's **y position** (Motion category) is less than a low number (Operators category).

## Hint 3: Almost there
Use **change y by** with a negative number so the apple falls. In the catch **if**, put **change score by ____**, then a sound, then a **go to x: ____ y: ____** block. For the bug hunt, think about what the apple is doing right after you catch it.
