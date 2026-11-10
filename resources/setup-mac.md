# Set up your Mac

Allow about an hour, once, before the first session. You need the internet only for the downloads. After that, everything works offline. Nothing here needs an account, a login or an email address.

A grown-up should do the installing. Children can then do everything else themselves.

**Before you start:** this guide uses the current Thonny Mac installer, which requires macOS 10.15 (Catalina) or newer. Open the Apple menu and choose **About This Mac**. It should show **Chip** (Apple silicon) or **Processor** (Intel), so you can choose the matching Thonny download below. If the Mac is older than macOS 10.15, ask a grown-up before installing anything.

## The quick way: one command

This installs everything below in one go: Scratch 3, Thonny, pytest and git. It is safe to run again, because anything already installed is skipped. If macOS first needs its Command Line Tools, the script pauses after opening that installer; run the same command again when it finishes.

1. Open **Terminal**: press **Cmd+Space**, type `Terminal` and press **Return**.
2. Click the **Copy** button on the line below, paste it into Terminal (**Cmd+V**) and press **Return**:

```
mkdir -p ~/Downloads && curl -fsSL %SITE%downloads/install-mac.sh -o ~/Downloads/install-mac.sh && bash ~/Downloads/install-mac.sh
```

3. Wait. It downloads the installers and tells you each step. It may ask for the **Mac administrator password** while Thonny (and, on some Macs, Scratch) is put in the Applications folder. A grown-up should enter it; nothing appears on screen while it is typed.
4. If a window asks to install the "command line developer tools", click **Install**, wait until it finishes, then run the same line again. The script needs this once so it can install git.

What it does not do: it needs no account and it does not upload your projects or personal information. It downloads this script from GitHub Pages, Scratch from `downloads.scratch.mit.edu`, Thonny from a GitHub release, and pytest plus its dependencies from PyPI. If git is missing, macOS may also download Apple's Command Line Tools. The script checks that the Thonny installer is signed before installing it and does not change your Mac's settings.

<details class="more"><summary>Read the whole script before you run it</summary>

You can also [download the script](%SITE%downloads/install-mac.sh) and run it with `bash ~/Downloads/install-mac.sh`. This is everything it does:

{{INSTALL_SCRIPT}}

</details>

Prefer to do it by hand, or something went wrong? The steps are below.

## Scratch (Level 1, weeks 1 to 6)

Scratch is the block-coding app. Use the free offline app, not the website, so nobody needs an account.

1. Open Safari and go to [scratch.mit.edu/download](https://scratch.mit.edu/download/).
2. Under "Install the Scratch app", choose **macOS**. Use the Mac App Store link, or download the `.dmg` file.
3. If you used the `.dmg`: drag **Scratch 3** into the **Applications** folder.
4. Open Scratch once. If macOS says it cannot check the app, Control-click the app, choose **Open**, then **Open** again. You only need to do this once.
5. Test it offline: turn Wi-Fi off, open Scratch, drag a "move 10 steps" block into the code area and click it. The cat moves. No sign-in is needed.

**Saving:** choose **File > Save to your computer**. Keep projects in a folder called `My Scratch` inside Documents. To open one, choose **File > Load from your computer**.

## Thonny and Python (Level 1 from week 7, and Levels 2 and 3)

Thonny is a friendly program for writing Python. It comes with its own copy of Python, so you do not need to install anything else.

1. Go to [thonny.org](https://thonny.org/) and download the macOS installer (a `.pkg` file). Choose **Intel (x64)** for an Intel Mac or **Apple silicon (arm64)** for an M1/M2/M3/M4-or-later Mac.
2. Open the file and click through the installer. It puts Thonny in **Applications**.
3. Open Thonny. On the first start, choose your language, **Standard** settings, and **Let's go!** if it appears.
4. Test it: type `print("hello")` in the top part, press the green **Run** button (or **F5**), and save the file as `test.py` when asked. You should see `hello` in the **Shell** at the bottom.

Make the text easy to read: choose **View > Increase font size** until everyone at the screen can read it comfortably.

## Get the course files

Each week page on this website that has Python exercises has a **Starter files (ZIP)** button. Download it, open it (double-click) and move the folder into your **Documents** folder. Inside are the exercise instructions and, for Python exercises, the starter code. Scratch activities use the instructions and blocks in the Scratch app instead.

- Keep your own work in a folder such as `~/Documents/my-python`.
- Give programs names that say what they do, like `flag-drawing.py`.
- Never name a file `turtle.py` or `random.py`: Python would mix it up with its own tools.
- In Thonny, open a file with **File > Open**, and press **Cmd+S** to save.

## pytest (Level 1 from week 7; Level 2 from week 8)

pytest is a free helper that runs automatic tests. Level 1's Python self-check files use it from week 7; Level 2 teaches pytest directly from week 8. Install it once before the first Python self-check:

1. In Thonny choose **Tools > Manage packages...**
2. Type `pytest` in the search box and click **Search on PyPI**.
3. Click **pytest** in the results, then **Install**. Wait a minute or two, then close the window. If a test still says that pytest is missing, restart Thonny or choose **Run > Stop/Reset** once.

This needs the internet once. If it does not work, use Thonny's interpreter selector at the lower right and choose **Local Python 3** (the bundled interpreter), then try again. In older Thonny versions the same choice is under **Tools > Options > Interpreter** or **Tools > Options > Back-end**.

## Terminal and git (Level 3)

Git is a "save-game" system for code. It comes with Apple's free command line tools.

1. Open **Terminal**: press **Cmd+Space**, type `Terminal` and press **Return**.
2. Type this line and press **Return**:

   ```
   xcode-select --install
   ```

   A window asks to install the "command line developer tools". Click **Install**, then **Agree**. It downloads for 5 to 20 minutes. If it says the tools are already installed, great.
3. Check it worked: type `git --version`. It prints a version number.

### Use a nickname for git, never your real name

Git writes a name and an email into every save point. Use a **nickname** and a clearly fake email (`example.com` never receives mail). Replace `Pixel Fox` with your own nickname and type, one line at a time:

```
git config --global user.name "Pixel Fox"
git config --global user.email "pixelfox@example.com"
git config --global init.defaultBranch main
git config --global core.editor nano
```

`git config --global --list` shows what you set. The last line makes git use the friendly `nano` editor if you forget `-m "message"`.

**Do not skip this step.** Git needs a name and email for each commit. If neither is configured, a commit normally stops with an identity error; it does not safely create an anonymous save point. Check it: type `git config user.name`. It must print the nickname. If it prints nothing, set the `user.name` and `user.email` lines above again.

### Run tests from Thonny's system shell

In Thonny choose **Tools > Open system shell...**. This opens a Terminal with Thonny's selected Python commands on its `PATH`, so it uses the same environment where pytest was installed. Run tests from there. Normally, test it with `python -m pytest --version`; if that command is not available, use `python3 -m pytest --version`. A plain Terminal may choose a different Python and may not have pytest.

## Safety checklist

- No accounts, no sign-ups, no real names, addresses, schools or photos in any project.
- Projects stay on your computer. Nothing is uploaded.
- During installation, a grown-up may enter the expected Mac administrator password. For any unexpected password or personal-information request, or any request to use the camera or microphone, click **Don't Allow** or close it and ask a grown-up.
- Take a break every 20 minutes: look at something 20 feet away for 20 seconds.

Something not working? See [Troubleshooting](../troubleshooting/).
