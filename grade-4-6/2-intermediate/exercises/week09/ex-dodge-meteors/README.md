# Exercise 9.2 - Dodge the Meteors

**Goal:** finish an arcade game with arrow keys, a game loop and collisions.

You are the sky-blue turtle at the bottom. Orange-red round meteors fall from the
sky. Dodge them with the Left and Right arrows. Each meteor that reaches the
ground is 1 point. One hit and it is GAME OVER.

1. Open `starter.py` and press **Run**. The meteors move once and stop, and
   the turtle cannot move. Let's fix that!
2. **TODO 1** `move_player()`: return the new x, using `clamp()` so the
   player stops at the walls. (You wrote tests for `clamp()` last week!)
   `direction` is `1` for right and `-1` for left, so `direction * step` is
   `1 * 20 = 20` (20 steps right) or `-1 * 20 = -20` (20 steps left). The
   walls are at `-270` (left) and `270` (right): the middle of the window is 0.
3. **TODO 2** `is_touching()`: use `math.dist()` to see if two points are
   closer than `how_close`. `math.dist((0, 0), (30, 40))` is `50.0`: it
   measures how far apart two points are in a straight line, like a ruler.
   Now run `check_my_work.py`: the first two checks should say `[PASS]`.
4. **TODO 3** connect the arrow keys with `screen.onkey(...)` and call
   `screen.listen()`.
5. **TODO 4** at the end of `game_loop()`, plan the next frame with
   `screen.ontimer(game_loop, FRAME_MS)`. Now the meteors keep falling!
6. Play! Click the window first so it hears your keys.

**Done looks like:** the meteors keep falling, the score goes up, the turtle
stops at the walls, and a hit shows `GAME OVER! Score: ...`.

**Check your work:** open `check_my_work.py` and press **Run**.

**Extra:** make the meteors fall faster every 5 points, give the player 3
lives, or save the high score in a file (like week 7).
