# Exercise 8.3 - Bar chart

**Goal:** draw a bar chart of the survey with turtle - and make it readable
for everyone.

A good chart never uses color alone: every bar has its **name** underneath
and its **number** on top.

**Steps**

1. Open `starter.py` and press **Run**. All the bars are the same height and
   there are no labels. Not very useful!
2. TODO 1: make `bar_height()` scale the value so the biggest bar is
   `MAX_HEIGHT` pixels tall.

   **Math helper:** a bar gets the same fraction of `MAX_HEIGHT` (250) as
   its votes are of the biggest votes (5). Kart Dash has 4 votes, so its
   bar is 4/5 of 250: 250 / 5 x 4 = 200 pixels. In Python that is
   `value / biggest * MAX_HEIGHT`.

   On the turtle screen (0, 0) is the center. `BOTTOM = -150` means the
   bars stand 150 steps *below* the center (the minus sign means "below").
3. TODO 2 and TODO 3: write the number on top of each bar and the name
   underneath, using `write_at()`.

**Done looks like:** six bars, tallest first: Block Craft 5, Kart Dash 4,
Puzzle Drop 3, Sky Islands 2, Pixel Pets 2, Space Chess 1. Each bar has its
name underneath and its number on top. The title "Our favorite games
(votes)" is at the top.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** chart the `genre` column instead, or add a y-axis line with tick
marks every 1 vote.
