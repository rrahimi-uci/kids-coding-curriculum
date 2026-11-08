# Exercise 4.1 - Guess My Number

**Goal:** a guessing game built from two `while` loops: a **game loop** and
an **input-checking loop**.

1. Open `starter.py` and press **Run**. Guess the number... It never stops,
   even when you are right! Press the red **Stop** button. That is an
   infinite loop - this week's bug.
2. **TODO 1:** add 1 to `tries` every time through the loop.
3. **TODO 3:** `break` out of the loop when the result is `"Correct"`.
4. **TODO 2:** now type `banana` as a guess - crash! Make `ask_number()`
   keep asking until the answer is a whole number from low to high.
   `answer.isdigit()` is True only when the answer is made of digits.

**Done looks like:**

```
I am thinking of a number from 1 to 20...
Guess a number from 1 to 20: banana
Oops! Please type a whole number from 1 to 20.
Guess a number from 1 to 20: 10
Too low
Guess a number from 1 to 20: 15
Correct
You got it in 2 tries!
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** give the player only 5 tries. Can you make it fair, so a smart
player can always win? (Hint: always guess the middle!)
