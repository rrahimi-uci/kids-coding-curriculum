"""The Mac install script that parents copy from the website must be valid, safe and consistent with the docs."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "resources" / "install-mac.sh"
GUIDE = ROOT / "resources" / "setup-mac.md"


def test_script_is_valid_bash():
    subprocess.run(["bash", "-n", str(SCRIPT)], check=True)


@pytest.mark.skipif(shutil.which("shellcheck") is None, reason="shellcheck not installed")
def test_script_passes_shellcheck():
    subprocess.run(["shellcheck", "-s", "bash", str(SCRIPT)], check=True)


def test_script_is_ascii_and_installs_every_required_program():
    text = SCRIPT.read_bytes()
    assert all(b < 128 for b in text), "the script is pasted into Terminal: keep it ASCII"
    body = text.decode()
    for needed in ("Scratch 3.app", "Thonny.app", "pytest", "xcode-select", "downloads.scratch.mit.edu", "github.com/thonny"):
        assert needed in body, f"install script does not mention {needed}"


def test_script_is_safe_to_paste_and_rerun():
    body = SCRIPT.read_text()
    assert "KIDS_DRY_RUN" in body, "keep the dry-run switch"
    assert "check-signature" in body, "the Thonny installer must be signature-checked"
    assert 'id -u' in body, "refuse to run as root"
    assert "main \"$@\"" in body.splitlines()[-1], "wrap everything in main() so a half-downloaded file never runs"
    for forbidden in ("curl | bash", "curl|bash", "rm -rf /", "eval "):
        assert forbidden not in body


def test_setup_guide_offers_the_script():
    guide = GUIDE.read_text()
    assert "{{INSTALL_SCRIPT}}" in guide and "%SITE%downloads/install-mac.sh" in guide
    assert "install-mac.sh" in guide


def test_setup_guide_matches_current_course_and_thonny_steps():
    guide = GUIDE.read_text()
    assert "Level 1 from week 7" in guide
    assert "Local Python 3" in guide
    assert "Mac administrator password" in guide
    assert "The plain Terminal's `python3` is Apple's own copy" not in guide
    assert "quietly uses the real name of the Mac account" not in guide
