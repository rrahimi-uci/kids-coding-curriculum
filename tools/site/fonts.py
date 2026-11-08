#!/usr/bin/env python3
"""Subset the course fonts to WOFF2 for the website (self-hosted: no third-party font requests).

Run once (or when the fonts change); the results are committed under site/src/fonts/.
Fonts: Atkinson Hyperlegible Next and Mono (Braille Institute, SIL OFL 1.1) and Lexend Deca
(Lexend Project, SIL OFL 1.1). Source files come from the TeX Live / user texmf tree.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXMF = Path.home() / "Library" / "texmf" / "fonts"
OUT = ROOT / "site" / "src" / "fonts"
ATK = TEXMF / "opentype" / "public" / "atkinson"
FONTS = {
    "atkinson-regular": ATK / "AtkinsonHyperlegibleNext-Regular.otf",
    "atkinson-italic": ATK / "AtkinsonHyperlegibleNext-RegularItalic.otf",
    "atkinson-bold": ATK / "AtkinsonHyperlegibleNext-Bold.otf",
    "atkinson-extrabold": ATK / "AtkinsonHyperlegibleNext-ExtraBold.otf",
    "atkinson-mono-regular": ATK / "AtkinsonHyperlegibleMono-Regular.otf",
    "atkinson-mono-bold": ATK / "AtkinsonHyperlegibleMono-Bold.otf",
    "lexend-regular": TEXMF / "truetype" / "public" / "lexend" / "LexendDeca-Regular.ttf",
}
UNICODES = "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+2010-2027,U+2030,U+20AC,U+2122,U+2190-2193,U+2212,U+2264-2265"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, src in FONTS.items():
        if not src.exists():
            print("missing font:", src)
            return 1
        subprocess.run([sys.executable, "-m", "fontTools.subset", str(src), f"--unicodes={UNICODES}",
                        "--flavor=woff2", f"--output-file={OUT / (name + '.woff2')}",
                        "--layout-features=kern,liga,calt,ccmp,locl,mark,mkmk", "--no-hinting"], check=True)
        print(f"{name}.woff2  {(OUT / (name + '.woff2')).stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
