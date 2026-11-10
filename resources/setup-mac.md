# Set up your Mac

Allow about an hour, once, before the first session. You need the internet only for the downloads. After that, everything works offline. Nothing here needs an account, a login or an email address.

A grown-up should do the installing. Children can then do everything else themselves.

## The quick way: one command

This installs everything below in one go: Scratch 3, Thonny, pytest and git. It is safe to run again, because anything already installed is skipped.

1. Open **Terminal**: press **Cmd+Space**, type `Terminal` and press **Return**.
2. Click the **Copy** button on the line below, paste it into Terminal (**Cmd+V**) and press **Return**:

```
curl -fsSL %SITE%downloads/install-mac.sh -o ~/Downloads/install-mac.sh && bash ~/Downloads/install-mac.sh
```

3. Wait. It downloads about 200 MB and tells you each step. When it asks for your **Mac password**, type it (nothing appears on screen while you type) and press **Return**. That is needed once, to put Thonny in the Applications folder.
4. If a window asks to install the "command line developer tools", click **Install**, wait until it finishes, then run the same line again.

What it does not do: it needs no account, it sends nothing anywhere, and the only downloads are from `scratch.mit.edu` (Scratch) and `github.com` (Thonny, which is signed and checked before it is installed). It does not change any setting on your Mac.

<details class="more"><summary>Read the whole script before you run it</summary>

You can also [download the script](%SITE%downloads/install-mac.sh) and run it with `bash ~/Downloads/install-mac.sh`. This is everything it does:

{{INSTALL_SCRIPT}}

</details>

Prefer to do it by hand, or something went wrong? The steps are below.

## Scratch (Level 1, weeks 1 to 6)

Scratch is the block-coding app. Use the free offline app, not the website, so nobody needs an account.

1. Open Safari and go to `scratch.mit.edu/download`.
2. Under "Install the Scratch app", choose **macOS**. Use the Mac App Store link, or download the `.dmg` file.
3. If you used the `.dmg`: drag **Scratch 3** into the **Applications** folder.
4. Open Scratch once. If macOS says it cannot check the app, Control-click the app, choose **Open**, then **Open** again. You only need to do this once.
5. Test it offline: turn Wi-Fi off, open Scratch, drag a "move 10 steps" block into the code area and click it. The cat moves. No sign-in is needed.

**Saving:** choose **File > Save to your computer**. Keep projects in a folder called `My Scratch` inside Documents. To open one, choose **File > Load from your computer**.

## Thonny and Python (Level 1 from week 7, and Levels 2 and 3)

Thonny is a friendly program for writing Python. It comes with its own copy of Python, so you do not need to install anything else.

1. Go to `thonny.org` and download the macOS installer (a `.pkg` file).
2. Open the file and click through the installer.
3. Open Thonny. On the first start, choose your language and **Standard** settings.
4. Test it: type `print("hello")` in the top part, press the green **Run** button (or **F5**), and save the file as `test.py` when asked. You should see `hello` in the **Shell** at the bottom.

Make the text easy to read: choose **View > Increase font size** until everyone at the screen can read it comfortably.

## Get the course files

Each week page on this website has a **Starter files (ZIP)** button. Download it, open it (double-click) and move the folder into your **Documents** folder. Inside are the exercise instructions and the starter code.

- Keep your own work in a folder such as `Documents/my-python`.
- Give programs names that say what they do, like `flag-drawing.py`.
- Never name a file `turtle.py` or `random.py`: Python would mix it up with its own tools.
- In Thonny, open a file with **File > Open**, and press **Cmd+S** to save.

## pytest (Level 2, needed from week 8)

pytest is a free helper that runs automatic tests. Install it once:

1. In Thonny choose **Tools > Manage packages...**
2. Type `pytest` in the search box and click **Search on PyPI**.
3. Click **pytest** in the results, then **Install**. Wait a minute or two, then close the window.

This needs the internet once. If it does not work, check that **Tools > Options > Interpreter** says "The same interpreter which runs Thonny (default)", then try again.

## Terminal and git (Level 3)

Git is a "save-game" system for code. It comes with Apple's free command line tools.

1. Open **Terminal**: press **Cmd+Space**, type `Terminal` and press **Return**.
2. Type this line and press **Return**:

   ```
   xcode-select --install
   ```

   A window asks to install the "command line developer tools". Click **Install**, then **Agree**. It downloads for 5 to 20 minutes. If it says the tools are already installed, great.
3. Check it worked: type `git --version`. It prints something like `git version 2.39.5 (Apple Git-154)`.

### Use a nickname for git, never your real name

Git writes a name and an email into every save point. Use a **nickname** and a clearly fake email (`example.com` never receives mail). Replace `Pixel Fox` with your own nickname and type, one line at a time:

```
git config --global user.name "Pixel Fox"
git config --global user.email "pixelfox@example.com"
git config --global init.defaultBranch main
git config --global core.editor nano
```

`git config --global --list` shows what you set. The last line makes git use the friendly `nano` editor if you forget `-m "message"`.

**Do not skip this step.** On a Mac, git does not stop you if no name is set: it quietly uses the real name of the Mac account instead. Check it: type `git config user.name`. It must print the nickname. If it prints nothing, type the two lines above again.

### Run tests from Thonny's own Terminal

In Thonny choose **Tools > Open system shell...**. This opens a Terminal that uses Thonny's Python, which has pytest. Run tests from there. Test it with `python3 -m pytest --version`. (The plain Terminal's `python3` is Apple's own copy, which does not have pytest.)

## Safety checklist

- No accounts, no sign-ups, no real names, addresses, schools or photos in any project.
- Projects stay on your computer. Nothing is uploaded.
- If a window asks for your name, a password or to use the camera or microphone, click **Don't Allow** or close it, and ask a grown-up.
- Take a break every 20 minutes: look at something 20 feet away for 20 seconds.

Something not working? See [Troubleshooting](../troubleshooting/).
