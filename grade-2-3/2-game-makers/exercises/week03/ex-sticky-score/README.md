# Exercise 3.3 – The Sticky Score (bug hunt)

**Goal:** find out why Kai's score never goes back to 0, and fix it.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

Kai's plan: click the bananas to get points. Every new game starts at 0.

## Build steps

1. Save your catch game first. Then File > New.
2. Click **Variables** (orange-red). Make a variable called `score`, for all sprites.
3. Click **Choose a Sprite**. Pick **Bananas**.
4. Click the Bananas in the sprite list. Build Kai's two scripts below.
5. Click the flag. Click the bananas three times.
6. Click the flag again. What does the score say?
7. Find the bug. Fix it. Test again.

## The script in words (with the bug)

- when green flag clicked (yellow Events)
- change score by 0 (orange-red Variables)

- when this sprite clicked (yellow Events)
- change score by 1 (orange-red Variables)
- start sound Pop (pink Sound)

## Expected behavior

With the bug, the score stays the same when you click the flag.
After the fix, the flag makes the score 0, and each click adds 1.

## Checklist

- [ ] I found the wrong block.
- [ ] I can say how "set" and "change" are different.
- [ ] The flag makes the score 0 now.
