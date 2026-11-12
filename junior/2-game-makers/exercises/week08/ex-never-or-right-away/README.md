# Exercise 8.2 – Never or Right Away?

**Goal:** find why Leo's game ends at once and why Zoe's game never ends.
**Tool:** Scratch app. **Work with a partner:** Driver, Helper and Player.

## Build steps

1. Look at Leo's and Zoe's scripts in your book. Guess the bugs first.
2. Open your catch game. Click **File**, then **Save to your computer**. Save a copy called your nickname plus `bugs`.
3. **Leo's bug.** On the Bowl, change **misses = 3** to `0`. Click the green flag. What happens?
4. Change it back to `3`. Test.
5. **Zoe's bug.** Drag the lower if, **if score = 10**, out of the forever. Snap it above the forever. Catch 10 apples. What happens?
6. Put it back inside the forever. Test again.

## The script in words

- Leo: forever, if misses = 0 then Game over!, stop all
- Zoe: if score = 10 then You win!, stop all, and then the forever

## Expected behavior

With Leo's bug, the game ends right at the start.
With Zoe's bug, you catch 10 apples and the game goes on.
After the fixes, both endings work.

## Checklist

- [ ] I saw Leo's bug and fixed it.
- [ ] I saw Zoe's bug and fixed it.
- [ ] I can say which block was the clue.
