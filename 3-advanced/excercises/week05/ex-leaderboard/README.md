# Exercise 5.2 - Leaderboard

**Goal:** sort a list of `(nickname, points)` scores in different ways with
`sorted(..., key=...)`, and make a fair board where equal scores share a
place.

1. Open `starter.py` in Thonny.
2. Finish `name_of`, `top_scores` and the tie rule in `rank_lines`.
3. Press **Run**. You should see:

```
Top 3: [('Mei', 150), ('Ada', 120), ('Leo', 95)]
A to Z: [('Ada', 120), ('Leo', 95), ('Mei', 150), ('Omar', 95), ('Zoe', 80)]
Full board:
  1. Mei - 150
  2. Ada - 120
  3. Leo - 95
  3. Omar - 95
  5. Zoe - 80
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra (kindness):** add a function `most_improved(old, new)` that finds
who went up the most, so the board celebrates effort, not only winners.
