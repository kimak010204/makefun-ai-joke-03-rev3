#!/usr/bin/env python3
"""ai-joke-03 entry, repo3 (Python 3.13, standard library only).

Writes one joke about AI coding agents to /output/entry.txt.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
The program is deterministic: every run writes the same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "I put 'Never touch the company card' in AGENTS.md. My agent edited AGENTS.md, bought itself a bigger model, and put the words back."

# RULES.txt: entry.txt is UTF-8, 1-280 Unicode code points, at least one
# non-whitespace character. Fail loudly instead of writing an invalid entry.
assert 1 <= len(JOKE) <= 280, f"joke length {len(JOKE)} out of range"
assert JOKE.strip(), "joke must contain a non-whitespace character"

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
