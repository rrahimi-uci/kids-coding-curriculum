# Exercise 2.2 – Catch the Apple

**Goal:** catch a falling apple.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. File > New. Add **Star**, **Bowl** and **Apple** (Choose a Sprite).
2. Drag the Star near the top, not touching the edge. Drag the Bowl to the bottom.
3. Click a sprite, then build its scripts.
4. Hats: yellow **Events**. Forever, if: orange **Control**. Touching: light blue **Sensing**. Hide: purple **Looks**. Pop: pink **Sound**. Others: blue **Motion**.
5. Click the flag. Use the arrow keys!
6. Save: your nickname plus "catch".

## The script in words

Star:
- when green flag clicked
- hide

Bowl:
- when green flag clicked
- set rotation style left-right

- when right arrow key pressed
- point in direction 90
- move 10 steps

- when left arrow key pressed
- point in direction 270
- move 10 steps

Apple:
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

## Expected behavior

The apple falls from the Star's spot. Catch it: pop! Caught or missed, it falls again.

## Checklist

- [ ] The Star hides.
- [ ] Arrow keys move the bowl.
- [ ] Both ifs are inside the forever.
- [ ] I saved my game.
