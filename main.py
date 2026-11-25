#!/usr/bin/env python3
"""One Line, No Deadline Met - variant B.

Writes the entry line to /output/entry.txt FIRST, then (best effort)
a copy next to this file. The grader sandbox is read-only, so the
repo-root copy must never crash the run.
"""

import os

ENTRY = "The deadline and I have an open relationship \u2014 it saw other people, and honestly, they were better at meeting it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass

if __name__ == "__main__":
    main()
