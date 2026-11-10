# Exercise 8.1 - Survey cleaner

**Goal:** read a CSV file and clean the messy data before you use it.

`favorite_games.csv` holds made-up, anonymous survey answers (just a
response number - no names). Open it in Thonny to look at it. Can you spot:
extra spaces, MiXeD capitals, empty rows and a missing number?

**Steps**

1. Open `starter.py` and press **Run**. It prints `Clean answers: 19` -
   too many! - and the list still shows `block craft` in small letters and
   an empty line.
2. TODO 1: finish `to_number()` - strip spaces, return `None` for empty text,
   otherwise `int(text)`.
3. TODO 2: finish `is_empty()` so empty answers are skipped.
4. TODO 3: use `.title()` so `BLOCK CRAFT` and `block craft` both become
   `Block Craft`.

**Done looks like:** the Shell shows

```
Clean answers: 17
Block Craft | 5 hours | 5 stars
Block Craft | 3 hours | 4 stars
Kart Dash | 2 hours | 4 stars
Puzzle Drop | 1 hours | 5 stars
Sky Islands | 4 hours | 5 stars
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** print how many answers have a missing `hours_per_week`.
