# Exercise 7.2 - The Lonely Turn (bug hunt)

**Goal:** find the line that is outside the repeat, and move it inside.
**Tool:** Thonny. **Work with a partner:** Driver and Helper.

## Steps

1. Click **Load**. Open `starter.py` in the `ex-lonely-turn` folder.
2. Click **Run**. It should draw a square. What does it draw?
3. Count the turns. The turtle turns only once!
4. Look at the lines under `for i in range(4):`. Which ones are pushed in?
5. Click at the very start of the line that should be inside.
6. Press the **Tab** key once. Thonny pushes the line in by 4 spaces.
7. Click **Save**, then **Run**.

## What you should see

Before the fix: one long straight line, then one turn at the end.

After the fix: a black square with 4 equal sides. The turtle turns at
every corner and ends where it started.

## Checklist

- [ ] I said which line was outside the repeat.
- [ ] I pushed it in so it lines up with the line above.
- [ ] I see a square.
