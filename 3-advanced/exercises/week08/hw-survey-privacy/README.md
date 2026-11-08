# Homework 8 - Survey privacy

**Goal:** make survey data safe to share by **anonymizing** it.

`snack_survey.csv` is made up, but it has a `nickname` and a `club` column.
Together they could tell someone exactly who gave each answer. Before data is
shared, we keep only what the question needs and give each row a plain ID.

1. Open `starter.py` and press **Run**. Look at "First row now looks like":
   the nickname is still there!
2. **Core** - TODO 1: finish `anonymize(rows, keep)`. Each new row gets an
   `id` (R1, R2, ...) and only the columns in `keep`.
3. **Challenge** - TODO 2: finish `save_csv(rows, filename)` with
   `csv.DictWriter`. Run again and open `snack_survey_anonymous.csv` in
   Thonny to see the safe file.

**Done looks like:**
`First row now looks like: {'id': 'R1', 'favorite_snack': 'apple slices', 'minutes_reading': '20'}`

**Check your work:** open `check_my_work.py` and press **Run**.
