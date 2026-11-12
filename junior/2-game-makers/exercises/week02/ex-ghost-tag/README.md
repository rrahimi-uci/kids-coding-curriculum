# Exercise 2.3 – Ghost Tag (bug hunt)

**Goal:** find out why Kai's ghost never says "Got you!", and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Kai's plan: the ghost flies from side to side and says "Got you!" when it touches the Ballerina.

## Build steps

1. File > New. Click **Choose a Sprite**. Add **Ghost** and **Ballerina**.
2. Click the Ghost in the sprite list. Build Kai's script below.
3. Drag the Ballerina into the ghost's path: same height, to one side.
4. Click the flag. Watch.
5. Find the bug. Fix it. Test again.

## The script in words (with the bug)

- when green flag clicked (yellow Events)
- point in direction 90 (blue Motion)
- set rotation style left-right (blue Motion)
- if touching Ballerina? then (orange Control, light blue Sensing)
  - say Got you! for 1 seconds (purple Looks)
- forever (orange Control)
  - move 5 steps (blue Motion)
  - if on edge, bounce (blue Motion)

## Expected behavior

With the bug, the ghost flies through the Ballerina and says nothing.
After the fix, it says "Got you!" every time it reaches her.

## Checklist

- [ ] I found the if that checks only once.
- [ ] I moved it into the forever.
- [ ] The ghost says "Got you!" when it touches the Ballerina.
