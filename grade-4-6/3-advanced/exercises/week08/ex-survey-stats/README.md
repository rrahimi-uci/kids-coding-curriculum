# Exercise 8.2 - Survey stats

**Goal:** ask questions of the clean data: what is most popular, and what is
the average?

The loading code from Exercise 8.1 is already done for you.

**Steps**

1. TODO 1: finish `count_by(rows, column)`. It builds a dictionary that counts
   each value, like a tally chart: `{"Block Craft": 5, "Kart Dash": 4, ...}`.
2. TODO 2: finish `average(numbers)`: add them up, divide by how many.
   An empty list gives 0 (you cannot divide by zero!).

   **Math helper:** the average is a fair share. For 2, 4 and 6: put them
   in one pile, 2 + 4 + 6 = 12, then share it between the 3 numbers:
   12 / 3 = 4. So `average([2, 4, 6])` is 4. Often the answer has digits
   after the point: `round(3.125, 1)` keeps one digit after the point and
   gives 3.1.
3. TODO 3: finish `most_popular(counts)`: the key with the biggest count.
4. Press **Run** and read your detective report.

**Done looks like:** among the lines in the Shell you see
```
Answers: 17
Most popular game: Block Craft with 5 votes
Average hours per week: 3.1
Average stars: 4.4
```
and a line for each genre, such as `adventure: 5.0 stars on average`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** which age group gives the most stars on average?
