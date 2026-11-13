# Teacher reference: Exercise 2.2 - Catch the Apple
> TEACHER ONLY. Keep this file away from students. It is not published on the website.

**Level and week:** Junior Level 2, Week 2 (If Touching...)  **Kind:** Scratch (offline app)  **Time:** about 18 minutes, across both Make it blocks
**Big idea:** Ifs inside a forever loop let a game react: caught or missed, the apple goes back to its start spot. A hidden Star marker gives the start spot without typing any positions.

## The finished project
Setup: File > New. Add Star, Bowl and Apple with the "Choose a Sprite" button. The cat can be deleted. Drag the Star to the top middle, about a finger's width below the top edge. Drag the Bowl to the bottom middle.

Sprite: Star
- when green flag clicked
- hide

Sprite: Bowl, script 1
- when green flag clicked
- set rotation style left-right

Sprite: Bowl, script 2
- when right arrow key pressed
- point in direction 90
- move 10 steps

Sprite: Bowl, script 3
- when left arrow key pressed
- point in direction 270
- move 10 steps

Sprite: Apple
- when green flag clicked
- set rotation style left-right
- go to Star
- point in direction 180
- forever
  - move 5 steps
  - if touching Bowl? then
    - start sound Pop
    - go to Star
  - if touching edge? then
    - go to Star

## What you should see
- Flag: the Star vanishes; the apple appears where the Star was and falls slowly, upright.
- Arrow keys slide the bowl left and right along the bottom; it stays upright.
- Catch: a pop, and the apple starts again from the top. Miss: the apple reaches the bottom edge and starts again from the top, silently.
- The apple always falls in the same place this week. Surprises (random) come in week 4.

## Talking points
- The Star-marker trick: a hidden sprite is still a place to "go to". We reuse it all level.
- Two ifs in one forever: the apple asks two questions, again and again.
- Why the bowl needs "set rotation style left-right": direction 270 would turn it upside down.
- Save now: week 3 adds a score to this game.

## Common mistakes and quick fixes
- The apple flickers at the top and never falls: it touches the top edge at the Star's spot, so "if touching edge" sends it back again and again. Show the Star (eye in the sprite info), drag it lower, click the flag.
- The apple sticks at the bottom: the edge if is missing or outside the forever.
- The apple falls upside down: "set rotation style left-right" missing in the apple's script.
- The apple never moves: "point in direction 180" missing, so it moves right instead and hits the side edge; or "move" is outside the forever.
- The Star is visible: the hide script is in another sprite. Move it to the Star.
- Arrow keys do nothing: click the stage once.
- "go to" still says random position: pick Star in its menu.

## Check-off list
- [ ] Star hides at the flag; the apple starts from the Star's spot.
- [ ] Bowl moves both ways with the arrow keys and stays upright.
- [ ] Apple: both ifs inside the forever, menus say Bowl and edge.
- [ ] Catch gives a pop; catch and miss both send the apple back to the Star.
- [ ] The game is saved as nickname plus "catch".
