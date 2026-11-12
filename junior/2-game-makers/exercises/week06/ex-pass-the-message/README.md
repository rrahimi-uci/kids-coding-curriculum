# Exercise 6.2 – Pass the Message

**Goal:** three sprites take turns, like the note relay. Nobody counts seconds!
**Tool:** Scratch app. **Work with a partner:** Driver and Helper.

## Build steps

1. Click **File**, then **New**. Add the **Ghost** and the **Ballerina**.
2. Cat: build the script. In **broadcast**, pick **New message**, type `ghost`.
3. Ghost: **when I receive ghost** (yellow Events), a say block, then **broadcast**. Make a new message `dance`.
4. Ballerina: **when I receive dance**, then a **repeat 4** (orange Control) with **next costume** and **wait 1 seconds** inside.
5. Click the flag.

## The script in words

Cat:

- when green flag clicked
- say Hi, Ghost! for 2 seconds
- broadcast ghost

Ghost:

- when I receive ghost
- say Boo! for 2 seconds
- broadcast dance

Ballerina:

- when I receive dance
- repeat 4
  - next costume
  - wait 1 seconds

## Expected behavior

The cat talks first. Then the Ghost says Boo! Then the Ballerina dances.
Each one waits for its message.

## Checklist

- [ ] The cat talks first, then the Ghost, then the Ballerina.
- [ ] Each sprite has a when I receive with the right message.
