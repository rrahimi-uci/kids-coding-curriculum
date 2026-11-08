# Exercise 2.1 - Game Math

**Goal:** write functions that **return** their answer, so the game can use it.

1. Open `starter.py` and press **Run**. Look for the word `None`. Bug hunt:
   why does `xp_needed` show the number on its own line and then say `None`?
2. **TODO 1:** change `print(...)` into `return ...`.
3. **TODO 2 and 3:** finish `damage()`: never less than 0, then `return result`.
4. **TODO 4:** finish `is_critical()`. Tip: `return roll >= 19` gives back
   True or False all by itself.
5. **TODO 5:** remove the `#` from the two health lines and run again.

**Done looks like:**

```
To reach level 5 you need 500 XP.
The dragon attacks with 12 against your shield of 5: 7 damage!
The goblin attacks with 3 against your shield of 5: 0 damage.
Health left: 33
Roll 7: critical hit? False
Roll 19: critical hit? True
Roll 20: critical hit? True
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** write `heal(health, potion)` that returns the new health, but
never more than 100.
