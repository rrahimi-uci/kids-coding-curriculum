## Hint 1: Where to look
Read the goal and the steps in words. The sprite starts on the left, moves to the middle, then moves to the right. It talks at the start, in the middle and at the end.

## Hint 2: Try this
Under **when green flag clicked**, use **go to x: ( ) y: ( )** from **Motion** to place your sprite on the left. Use **glide ( ) secs to x: ( ) y: ( )**, also from **Motion**, for each walk. Use **say ( ) for ( ) seconds** from **Looks** for each talk.

## Hint 3: Almost there
Talking and walking take turns, so they alternate in your stack. Each **glide** block moves the sprite to a new spot, and only the x number changes if you want to stay at the same height. Left is a negative x, and right is a positive x.
