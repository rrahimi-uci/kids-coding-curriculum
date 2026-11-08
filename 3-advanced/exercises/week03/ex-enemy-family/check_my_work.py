"""CHECK MY WORK - open this file in Thonny and press the green Run button (F5).

It checks the code in starter.py (the file YOU edit) and tells you
which parts already work. You do not need to change this file.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
for folder in [HERE, *HERE.parents]:
    if (folder / "testing" / "kidtest").is_dir():
        sys.path.insert(0, str(folder / "testing"))
        break

from kidtest.checker import check_folder  # noqa: E402

check_folder(HERE)
