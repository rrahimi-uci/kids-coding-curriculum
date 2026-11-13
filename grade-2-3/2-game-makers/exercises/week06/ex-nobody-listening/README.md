# Exercise 6.3 – Nobody Is Listening (bug hunt)

**Goal:** Kai's game should work like this: click the Star, the Balloon floats up and the Ghost says Boo! Find two bugs.
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **File**, then **New**. Add the **Star**, **Balloon1** and the **Ghost**. Delete the cat.
2. Drag the Balloon to the bottom of the stage.
3. Build the Balloon's script **first**. Leave it on **message1**.
4. Build the Star's script. Make a new message called `go`.
5. Build the Ghost's script.
6. **Test:** click the flag, then the Star. **Look.** **Change one thing.** Test again.

## The script in words (with the bugs)

Balloon1:

- when I receive message1 (yellow Events)
- point in direction 0 (blue Motion)
- repeat 10 (orange Control)
  - move 10 steps

Star:

- when this sprite clicked
- broadcast go

Ghost:

- when green flag clicked
- say Boo! for 2 seconds (purple Looks)

## Expected behavior

After the fixes, the flag does nothing. Click the Star: the Balloon floats
up and the Ghost says Boo! at the same time.

## Checklist

- [ ] I found who was not listening.
- [ ] I found the wrong message name.
- [ ] Clicking the Star starts the Balloon and the Ghost.
