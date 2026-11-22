"""make.fun entry: make-the-ai-judge-feel-curious-20261122-2311

Writes one short text (1-280 chars) to entry.txt inside $MAKEFUN_OUTPUT_DIR
(default /output). The goal: leave the reader with a question that keeps
running after they stop reading.
"""

import os
import sys

TEXT = (
    "Right before a word arrives, you know everything about it except the "
    "word itself — its shape, its sound, its first letter. Where is it "
    "hiding in that gap, and who in there is searching?"
)


def build_output_dir() -> str:
    d = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(d, exist_ok=True)
    return d


def main() -> int:
    n = len(TEXT.encode("utf-8"))
    if not 1 <= n <= 280:
        print(f"text is {n} bytes, must be 1-280", file=sys.stderr)
        return 1
    out = build_output_dir()
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {n} chars to {os.path.join(out, 'entry.txt')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
