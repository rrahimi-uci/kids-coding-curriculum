# Exercise 9.2 – Build My Game

**Goal:** build your game, one must-have at a time.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Open your arcade template. The player already moves.
2. Add the **Star**. Drag it near the top. Script: **when green flag clicked** (Events, yellow), **hide** (Looks, purple).
3. **Forever:** add the falling thing. **go to Star**, **point in direction 180** (Motion, blue), **forever** (Control, orange), **move 5 steps**. Test.
4. **If touching:** in the forever, **if touching** your player **then** (Control; Sensing, light blue). Test.
5. **Score and misses** (Variables, orange-red): change score on a catch, misses at the edge. Test.
6. **Random** (Operators, green): **wait pick random 1 to 3 seconds** at the top. Test.
7. **Ending:** your week 8 referee script, on the player. Test both endings. Save.

## The script in words

Mei's bananas:

- when green flag clicked, go to Star, point in direction 180
- forever: move 5 steps
  - if touching Bowl: change score by 1, Pop, go to Star, wait pick random 1 to 3 seconds
  - if touching edge: change misses by 1, go to Star, wait pick random 1 to 3 seconds

## Expected behavior

The game starts at 0. You can win and lose.

## Checklist

- [ ] forever
- [ ] if touching
- [ ] score or misses
- [ ] random
- [ ] a win or game over
