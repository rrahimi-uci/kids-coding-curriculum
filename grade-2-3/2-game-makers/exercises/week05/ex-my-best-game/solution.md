# Teacher reference: Exercise 5.3 - My Best Game
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 5 (Play Day and Show Me)  **Kind:** Scratch (offline app), free build with show-me checklist  **Time:** about 15 minutes
**Big idea:** A game is a forever loop, an if that reacts, a score that counts and a surprise, all working together.

## The finished project
Setup: the fixed leg 3 of Exercise 5.2 (or rebuild it from the workbook). Make one variable, "score", For all sprites.

Sprite: Sprite1 (the cat)
- when green flag clicked
- forever
  - go to mouse-pointer

Sprite: Apple
- when green flag clicked
- set score to 0
- forever
  - if touching Sprite1? then
    - change score by 1
    - start sound Pop
    - go to random position

Children add their own ideas on top: a backdrop, a "say Yum! for 1 seconds" in the cat when it touches the Apple, a different sprite to catch (Bananas), or a second sprite to catch with its own copy of the Apple's script.

## What you should see
- Flag: score 0. The cat follows the mouse everywhere.
- Each catch: one pop, the score goes up by exactly 1, the Apple jumps to a surprise place.
- Flag again: the score is back to 0.

## Talking points
- Show-me rows to watch here: a forever keeps the cat moving; an if-touching makes the Apple react; the score starts at 0 and goes up by 1; go to random position is the surprise; the child explains the script.
- Ask "Why does the Apple jump away after a catch?" (So one catch counts once.)
- Ask "Is your game fair? Does everyone know how to score?" (week 3).

## Common mistakes and quick fixes
- The score goes up by lots in one catch: "go to random position" is missing or outside the if, so the cat touches the Apple for many loops.
- The score keeps last game's points: "set score to 0" is missing or inside the forever (then it never goes above 1).
- The set block will not go under the forever: it belongs above it, right under the hat block.
- The score blocks landed in the cat's code: click the Apple in the sprite list (blue frame) before adding blocks, and move them over by dragging them onto the Apple.

## Check-off list
- [ ] A forever loop keeps the cat following the mouse.
- [ ] An if touching check is inside a forever.
- [ ] The score starts at 0 and goes up by 1 for each catch.
- [ ] go to random position (or another pick random) gives a surprise.
- [ ] The child can say how the game works.
