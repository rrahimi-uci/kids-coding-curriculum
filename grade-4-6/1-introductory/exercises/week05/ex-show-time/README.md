# Exercise 5.3 – Show Time (bug hunt)

**Goal:** make two sprites work together with **broadcast** and **when I receive**,
and fix a message that nobody receives.
**Tool:** Scratch app (offline). **Work in pairs.**

## Build steps

1. Start a new project. Keep the cat: it is the **Presenter**.
2. Click **Choose a Sprite** and add a **Dancer**: any sprite with several costumes
   (for example Ballerina).
3. Make two messages: drag a **broadcast** block (in **Events**), click its dropdown,
   choose **New message** and type `start show`. Make another called `finale`.
4. Build the scripts below on the right sprites.
5. Click the green flag and enjoy the show.
6. Bug hunt: Ada's dancer starts with **when I receive (show start)** instead of
   **start show**. Make a new message `show start` and use it in the dancer's hat block.
   What happens? Why? Fix it by choosing `start show` again.
7. Save as `show-time`.

## The scripts in words

**Presenter** (cat), two scripts:

1. when green flag clicked
   - go to x: -150 y: -50
   - say "Welcome to the show!" for 2 seconds
   - broadcast start show
2. when I receive finale
   - say "Thank you for watching!" for 2 seconds

**Dancer**, two scripts:

1. when green flag clicked
   - hide
2. when I receive start show
   - go to x: 80 y: -30
   - show
   - repeat 8:
     - next costume
     - wait 0.3 seconds
   - broadcast finale

## Expected behavior

The dancer hides at the start. The presenter says "Welcome to the show!",
then the dancer appears and dances (8 costume changes), then the presenter
says "Thank you for watching!". With Ada's bug, the presenter speaks and then
nothing happens, because no sprite is listening for `start show`.

## Checklist

- [ ] I made the messages `start show` and `finale`.
- [ ] The dancer only appears after the presenter has spoken.
- [ ] The presenter says thank you after the dance.
- [ ] I can explain Ada's bug: the message names did not match.
- [ ] I saved my project.
