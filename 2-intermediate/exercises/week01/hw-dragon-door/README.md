# Homework 1 - Dragon Door

**Goal:** practice `and`, `or` and f-strings.

The dragon door opens if:

* you have the golden key **and** you are level 3 or more, **or**
* you are level 10 or more (legends do not need keys).

1. Open `starter.py` in Thonny.
2. **TODO 1:** change the `if` line in `door_opens()`. Brackets help:
   `(has_key and level >= 3) or level >= 10`.
3. **TODO 2:** make the welcome message use an f-string with the hero name.
4. Run it with these answers and check the door does the right thing:
   key yes + level 5 (opens), key yes + level 2 (shut), key no + level 12 (opens).

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** add a third way in: a secret password typed by the player.
(Only a made-up game password, never a real one!)
