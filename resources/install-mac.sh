#!/bin/bash
# Kids Coding: install everything the course needs on a Mac.
#
#   * Scratch 3 (the free offline app)          - Level 1, weeks 1 to 6
#   * Thonny (comes with its own Python)        - Level 1 from week 7, Levels 2 and 3
#   * pytest, inside Thonny's Python            - Level 2 from week 8
#   * git (Apple's command line tools)          - Level 3
#
# It is safe to run again: anything already installed is skipped.
# It asks for your Mac password once (to put Thonny in Applications) and never sends any
# information anywhere: the only network traffic is the downloads from scratch.mit.edu and github.com.
# Set KIDS_DRY_RUN=1 to see what it would do without installing anything.

main() {
  set -u

  say()  { printf '\n==> %s\n' "$1"; }
  ok()   { printf '    ok: %s\n' "$1"; }
  fail() { printf '\n!! %s\n' "$1" >&2; exit 1; }
  run()  { if [ "${KIDS_DRY_RUN:-0}" = "1" ]; then printf '    (dry run) %s\n' "$*"; else "$@"; fi; }

  [ "$(uname -s)" = "Darwin" ] || fail "This script is for a Mac."
  [ "$(id -u)" -ne 0 ] || fail "Run this as your normal user, not with sudo. It asks for the password when needed."
  case "$(uname -m)" in
    arm64)  THONNY_ARCH="arm64" ;;
    x86_64) THONNY_ARCH="x64" ;;
    *)      fail "Unknown Mac processor: $(uname -m)" ;;
  esac

  APPS="${KIDS_APPS_DIR:-/Applications}"   # (only changed for testing)
  WORK="$(mktemp -d "${TMPDIR:-/tmp}/kidscoding.XXXXXX")" || fail "Could not make a temporary folder."
  MOUNT=""
  cleanup() {
    [ -n "$MOUNT" ] && hdiutil detach -quiet "$MOUNT" 2>/dev/null
    rm -rf "$WORK"
  }
  trap cleanup EXIT

  # ---- 1. git (Apple command line tools) -------------------------------------------------------
  say "1 of 4: git"
  if xcode-select -p >/dev/null 2>&1 && git --version >/dev/null 2>&1; then
    ok "$(git --version)"
  else
    run xcode-select --install
    printf '\n    A window opened and asks to install the "command line developer tools".\n'
    printf '    Click Install, then Agree, and wait for it to finish (5 to 20 minutes).\n'
    printf '    Then run this script again to finish the other steps.\n'
    [ "${KIDS_DRY_RUN:-0}" = "1" ] || exit 0
  fi

  # ---- 2. Scratch 3 ------------------------------------------------------------------------------
  say "2 of 4: Scratch 3"
  if [ -d "$APPS/Scratch 3.app" ]; then
    ok "Scratch 3 is already installed"
  else
    echo "    Downloading Scratch (about 150 MB)..."
    run curl -fL --progress-bar -o "$WORK/Scratch.dmg" "https://downloads.scratch.mit.edu/desktop/Scratch.dmg" \
      || fail "Could not download Scratch. Check the internet connection and try again."
    if [ "${KIDS_DRY_RUN:-0}" != "1" ]; then
      MOUNT="$WORK/scratch-disk"
      mkdir -p "$MOUNT"
      hdiutil attach -nobrowse -quiet -readonly -mountpoint "$MOUNT" "$WORK/Scratch.dmg" \
        || fail "Could not open the Scratch download."
      APP="$(find "$MOUNT" -maxdepth 1 -name '*.app' | head -n 1)"
      [ -n "$APP" ] || fail "The Scratch download did not contain an app."
      cp -R "$APP" "$APPS/" 2>/dev/null || sudo cp -R "$APP" "$APPS/" \
        || fail "Could not copy Scratch into Applications."
      hdiutil detach -quiet "$MOUNT" && MOUNT=""
    fi
    ok "Scratch 3 installed"
  fi

  # ---- 3. Thonny ---------------------------------------------------------------------------------
  say "3 of 4: Thonny (the Python editor)"
  if [ -d "$APPS/Thonny.app" ]; then
    ok "Thonny is already installed"
  else
    TAG="$(curl -fsSLI -o /dev/null -w '%{url_effective}' https://github.com/thonny/thonny/releases/latest | sed 's#.*/tag/##')"
    case "$TAG" in v[0-9]*) ;; *) fail "Could not find the latest Thonny version. Try again later." ;; esac
    PKG_URL="https://github.com/thonny/thonny/releases/download/${TAG}/thonny-${TAG#v}-${THONNY_ARCH}.pkg"
    echo "    Downloading Thonny ${TAG#v}..."
    run curl -fL --progress-bar -o "$WORK/thonny.pkg" "$PKG_URL" \
      || fail "Could not download Thonny. Check the internet connection and try again."
    if [ "${KIDS_DRY_RUN:-0}" != "1" ]; then
      pkgutil --check-signature "$WORK/thonny.pkg" 2>/dev/null | grep -q "Status: signed" \
        || fail "The Thonny installer is not signed by a developer, so it was not installed."
      echo "    Your Mac password is needed once, to put Thonny in the Applications folder."
      sudo /usr/sbin/installer -pkg "$WORK/thonny.pkg" -target / >/dev/null \
        || fail "The Thonny installer did not finish."
    fi
    ok "Thonny installed"
  fi

  # ---- 4. pytest, inside Thonny's own Python ----------------------------------------------------
  say "4 of 4: pytest (automatic tests, Level 2)"
  PY="$(find "$APPS/Thonny.app/Contents/Frameworks/Python.framework/Versions" -path '*/bin/python3' 2>/dev/null | head -n 1)"
  if [ -z "$PY" ]; then
    if [ "${KIDS_DRY_RUN:-0}" = "1" ]; then
      echo "    (dry run) would install pytest after Thonny"
    else
      fail "Could not find Thonny's Python. Open Thonny once, then run this script again."
    fi
  elif "$PY" -m pytest --version >/dev/null 2>&1; then
    ok "$("$PY" -m pytest --version 2>&1 | head -n 1)"
  else
    run "$PY" -m pip install --user --quiet --disable-pip-version-check pytest \
      || fail "Could not install pytest. Check the internet connection and try again."
    ok "pytest installed"
  fi

  say "All done"
  cat <<'EOF'
    Installed: Scratch 3, Thonny, pytest, git.

    Try them:
      * Open Scratch 3 and Thonny from the Applications folder (or Spotlight: Cmd+Space).
      * The first time macOS may ask if you want to open an app downloaded from the internet: click Open.
      * In Thonny type  print("hello")  and press the green Run button.

    Level 3 only: tell git a nickname (never a real name) before the first save point:
      git config --global user.name "Pixel Fox"
      git config --global user.email "pixelfox@example.com"
EOF
}

main "$@"
