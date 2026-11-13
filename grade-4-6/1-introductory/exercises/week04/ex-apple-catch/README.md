# Exercise 4.2 – Apple Catch

**Goal:** build a catch game with a **score** variable, **random** start places,
a **forever** loop and **if** blocks.
**Tool:** Scratch app (offline). **Work in pairs:** swap, then play each other's game.

## Build steps

1. Start a new project. Delete the cat. Add the **Bowl** and **Apple** sprites
   (**Choose a Sprite**). Choose any backdrop.
2. Make a variable `score` (**For all sprites**).
3. Click the **Bowl** and build the Bowl script. **mouse x** is in **Sensing**.
4. Click the **Apple** and build the Apple script. **y position** is in **Motion**;
   the **<** block is in **Operators**.
5. Play: move the mouse left and right to catch the apples.
6. Bug hunt: take the **go to x: (pick random ...) y: 170** block out of the
   **touching Bowl?** block. Catch one apple. What happens to the score? Why?
   Put the block back.
7. Add a credits comment and save as `apple-catch`.

## The scripts in words

**Bowl**:

- when green flag clicked
- go to x: 0 y: -140
- forever:
  - set x to (mouse x)

**Apple**:

- when green flag clicked
- set score to 0
- go to x: (pick random -200 to 200) y: 170
- forever:
  - change y by -5
  - if touching Bowl? then
    - change score by 1
    - start sound (any)
    - go to x: (pick random -200 to 200) y: 170
  - if (y position) < -170 then
    - go to x: (pick random -200 to 200) y: 170

**Math helper:** the sign `<` means "is less than". A smaller y is lower down,
and the bottom edge of the stage is y: -180. With minus numbers, the bigger the
number after the minus sign, the lower the spot: y: -175 is lower than y: -170.
So "(y position) < -170" means "the apple has fallen almost to the bottom".

## Expected behavior

The score starts at 0. The bowl stays at the bottom and follows the mouse
left and right. Apples fall from a different place at the top each time.
Each apple you catch adds exactly 1 to the score and plays a sound; then a
new apple falls. A missed apple starts again at the top. Without the
"go to the top" block after a catch, one catch adds lots of points, because
the apple keeps touching the bowl while the loop keeps checking.

## Checklist

- [ ] The bowl follows the mouse and stays at the bottom.
- [ ] Apples start from a random place at the top.
- [ ] The score starts at 0 every game.
- [ ] Each catch adds exactly 1.
- [ ] I can explain Mei's bug (one catch, many points).
- [ ] I added a credits comment and saved my project.
