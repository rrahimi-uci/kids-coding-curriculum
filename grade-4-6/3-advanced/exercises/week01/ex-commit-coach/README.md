# Exercise 1.2 - Commit Coach

**Goal:** finish a small helper that checks commit messages and warns you
about secrets before you commit. (It also warms up your Level 2 skills:
functions with `return`, lists and loops.)

1. Open `starter.py` in Thonny.
2. Finish the five `TODO`s:
   - `is_good_message(message)` returns `False` for messages that are empty,
     longer than 50 characters, boring (`stuff`, `update`, `fix`...) or only
     one word.
   - `make_message("add", "star shape")` returns `"Add star shape"`.
   - `find_secrets(lines)` returns the lines that contain a secret word such
     as `password` or `api_key` (any capitals).
3. Press **Run** and type some messages to try your coach. Type `q` to quit.

**Done looks like:**

```
Message: stuff
Be specific: say WHAT changed, like 'Add jump to hero'.
Message: Add jump to hero
Great message!
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add your own boring words to `BORING_MESSAGES`, or make
`coach_tip` warn when a message does not start with a capital letter.
