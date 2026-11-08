# Exercise 4.2 - Guess-the-Number Bot

**Goal:** build a bot that ALWAYS finds your secret number from 1 to 100 in
7 guesses or fewer, by halving the range every time (binary search).

1. Open `starter.py` in Thonny.
2. Press **Run** first. The slow bot guesses 1, 2, 3... Boring!
   (Type `h` again and again, then press **Stop** to end it.)
3. Finish `check` (TODO 1) and make `next_guess` smart (TODO 2).
4. Run again and play: think of a number, answer `h`, `l` or `c`.

**Done looks like:**

```
Think of a whole number from 1 to 100. I will find it!
Is it 50? Type h (higher), l (lower) or c (correct): h
Is it 75? Type h (higher), l (lower) or c (correct): l
Is it 62? Type h (higher), l (lower) or c (correct): c
Got it in 3 tries!
```

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** change the range to 1..1000. How many guesses does the bot need
now, at most? Make a prediction first, then test it.
