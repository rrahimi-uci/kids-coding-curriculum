"""What the voice says for a line of narration (pure text rules, no audio libraries)."""

from __future__ import annotations

import re

# Pronunciation fixes for words the voice model says wrongly.
LEXICON = {"Thonny": "Tonny", "elif": "el-if", "randint": "rand int", "def ": "deff "}

# Captions show code the way it is written (self.height, stickers.txt, __init__, --global); the voice
# says it the way a teacher reads it aloud (self dot height, stickers dot T X T, dunder init, dash dash global).
FILE_TYPES = {"py": "pie", "txt": "T X T", "csv": "C S V", "json": "jason", "md": "M D", "html": "H T M L"}
SPOKEN_CODE = (
    (re.compile(r"__(\w+?)__"), r"dunder \1"),
    (re.compile(r"(?<!\w)--(?=\w)"), "dash dash "),
    (re.compile(r"(?<=\w)\.(" + "|".join(FILE_TYPES) + r")\b"), lambda m: " dot " + FILE_TYPES[m[1]]),
    (re.compile(r"(?<=[A-Za-z_)])\.(?=[A-Za-z_])"), " dot "),
    (re.compile(r"(?<=[A-Za-z0-9])_(?=[A-Za-z0-9])"), " underscore "),
    # whole code words only (a plain replace would turn "monkey" into "mon key")
    (re.compile(r"\bonkey\b"), "on key"),
    (re.compile(r"\bontimer\b"), "on timer"),
)


def spoken_form(text: str) -> str:
    """The words the voice says for a caption line."""
    for pattern, said in SPOKEN_CODE:
        text = pattern.sub(said, text)
    for word, said in LEXICON.items():
        text = text.replace(word, said)
    return text.replace("‘", "").replace("’s", "'s").replace("’", "'")
