# Exercise 2.2 – Polygon Party

**Goal:** draw shapes with the Pen using **repeat** and the rule **turn = 360 ÷ sides**.
**Tool:** Scratch app (offline) with the Pen extension. **Work in pairs.**

## Build steps

1. Start a new project: **File > New**.
2. Click the blue **Add Extension** button (bottom left corner) and choose **Pen**.
   A green **Pen** category appears.
3. Make the cat small so you can see the lines: in the sprite pane set **Size** to `40`.
4. Build the square script below and click the green flag.
5. Change the numbers to draw a **triangle**, then a **hexagon**, then a **pentagon**.
   Predict each shape before you click the flag.
6. Bug hunt: Leo wanted a triangle and used repeat 3, move 100, turn 60.
   Predict what it draws, run it, then fix it.
7. Save as `polygon-party`.

## The script in words (square)

- when green flag clicked
- erase all
- go to x: 0 y: 0
- point in direction 90
- pen down
- repeat 4:
  - move 100 steps
  - turn right 90 degrees
- pen up

Tip: put the green **( ) / ( )** block from **Operators** in the turn slot and type
`360` and the number of sides. Scratch does the dividing for you.

| Shape    | Sides | Repeat | Turn |
|----------|-------|--------|------|
| Triangle | 3     | 3      | 120  |
| Square   | 4     | ?      | ?    |
| Pentagon | 5     | ?      | ?    |
| Hexagon  | 6     | ?      | ?    |

## Expected behavior

Each time you click the flag, the old drawing is erased and the cat draws one
closed shape (it ends exactly where it started). The square has 4 equal sides,
the triangle 3, the pentagon 5 and the hexagon 6.

## Checklist

- [ ] I added the Pen extension.
- [ ] **move** and **turn** are both inside the **repeat**.
- [ ] My square, triangle, hexagon and pentagon all close.
- [ ] I can explain what was wrong with Leo's triangle and how to fix it.
- [ ] I saved my project.
