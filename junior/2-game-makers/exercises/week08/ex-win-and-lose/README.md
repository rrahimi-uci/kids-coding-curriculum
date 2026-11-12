# Exercise 8.1 – Win and Lose

**Goal:** give your catch game a start, a way to win and a way to lose.
**Tool:** Scratch app. **Work with a partner:** Driver, Helper and Player.

## Build steps

1. Open your catch game.
2. Click **Variables** (orange-red). Make a variable called `misses`, **For all sprites**.
3. Click the **Apple**. In its **if touching edge?**, snap **change misses by 1** (Variables, orange-red) above **go to Star**.
4. Click the **Bowl**. Drag in a new **when green flag clicked** (Events, yellow).
5. Snap **set score to 0** and **set misses to 0** (Variables). Add **say Catch 10 apples! for 2 seconds** (Looks, purple).
6. Snap a **forever** (Control, orange). Put two **if then** blocks inside.
7. In each if, put an **=** block (Operators, green), a **say** block and **stop all** (Control). Misses first, then score.

## The script in words

Bowl:

- when green flag clicked
- set score to 0
- set misses to 0
- say Catch 10 apples! for 2 seconds
- forever
  - if misses = 3 then
    - say Game over! for 2 seconds
    - stop all
  - if score = 10 then
    - say You win! for 2 seconds
    - stop all

## Expected behavior

Catch 10 apples: You win! Miss 3: Game over! Then everything stops.

## Checklist

- [ ] The game starts at 0 and 0.
- [ ] I tested the win.
- [ ] I tested the game over.
