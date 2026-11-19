#!/usr/bin/env python3
"""make.fun news-image-20261119 entry.

Copies the bundled front-page image (entry.png, drawn for this entry) to
/output/entry.png. Standard library only; no network; deterministic —
two runs write byte-identical output because the source file never changes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()
