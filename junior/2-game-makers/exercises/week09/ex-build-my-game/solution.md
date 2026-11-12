# Teacher reference: Exercise 9.2 - Build My Game
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 9 (Project Studio)  **Kind:** Scratch (offline app), project build  **Time:** about 25 minutes
**Big idea:** Plan on the game plan card, then build and test one must-have at a time: forever, if touching, score or misses, random, an ending.

## The finished project
Setup (core path, done by the grown-up before the lesson): the arcade template from the Project Teacher Guide, a backdrop plus a player sprite that already moves with the four arrow keys, saved as "arcade-" plus the nickname. Two sample games follow; every child's game will differ.

**Catch game: Mei's Banana Drop**

Sprite: Star (the hidden marker, dragged near the top)
- when green flag clicked
- hide

Sprite: Bananas
- when green flag clicked
- set rotation style left-right
- go to Star
- point in direction 180
- forever
  - move 5 steps
  - if touching Bowl? then
    - change score by 1
    - start sound Pop
    - go to Star
    - wait (pick random 1 to 3) seconds
  - if touching edge? then
    - change misses by 1
    - go to Star
    - wait (pick random 1 to 3) seconds

Sprite: Bowl (template arrow-key scripts, plus the week 8 referee)
- when green flag clicked
- set score to 0
- set misses to 0
- say Catch 10 bananas! for 2 seconds
- forever
  - if misses = 3 then
    - say Game over! for 2 seconds
    - stop all
  - if score = 10 then
    - say You win! for 2 seconds
    - stop all

**Maze game: Omar's Ghost Maze**

Sprites: Star (hidden start marker at the maze entrance, script: when green flag clicked, hide); Walls (painted with thick lines, no scripts); Apple (the goal, dragged to the end, no scripts).

Sprite: Ghost
- when green flag clicked
- forever
  - go to random position
  - wait 2 seconds

Sprite: Cat (the player: template arrow-key scripts, plus)
- when green flag clicked
- set size to 30 %
- set misses to 0
- go to Star
- say Reach the apple! for 2 seconds
- forever
  - if touching Walls? then
    - change misses by 1
    - go to Star
  - if touching Ghost? then
    - change misses by 1
    - go to Star
    - wait 1 seconds
  - if misses = 3 then
    - say Game over! for 2 seconds
    - stop all
  - if touching Apple? then
    - say You win! for 2 seconds
    - stop all

## What you should see
- Catch game: bananas fall from the Star, pause 1 to 3 seconds at the top before each fall, score and misses start at 0; "You win!" at 10, "Game over!" at 3 misses.
- Maze game: the cat starts at the entrance, is sent back on touching a wall or the ghost (one miss each), wins on reaching the apple, loses at 3 misses. The ghost jumps to a new place every 2 seconds.
- Other valid choices: a different goal (5, 15), lives counted as misses, random as "go to random position" or "pick random" in a move or a wait (always 1 to 10).

## Talking points
- One must-have at a time: build, test, check off. A bug in one small part is quick to find.
- Every must-have maps to a week: forever (1), if touching (2), score and misses (3), random (4), ending (8).
- Design choices: why 10? why 3 misses? why this speed? Children explain one at the showcase.

## Common mistakes and quick fixes
- Misses count at the start: the Star touches an edge. Show the Star, drag it lower and away from the sides, hide it again.
- The score jumps by many: "go to Star" must follow "change score by 1" straight away.
- Game over at once on a second game: "set misses to 0" missing from the top of the referee.
- The maze cat is too big to fit: "set size to" a smaller number, or paint wider paths.
- The ghost lands on the start: the "wait 1 seconds" after a ghost hit stops three misses in a row.
- A sprite is upside down: "set rotation style left-right" at the start of its flag script.

## Check-off list
- [ ] Game plan card filled in (M1).
- [ ] A forever loop keeps the game running.
- [ ] An if-touching check makes something happen.
- [ ] A score or misses variable starts at 0 and changes during play.
- [ ] Random is used (pick random 1 to 10 or go to random position).
- [ ] A win or game-over ending with "stop all"; both tested (M2).
- [ ] A Player playtested it, and one bug from the list is fixed.
