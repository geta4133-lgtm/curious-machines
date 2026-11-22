# Who Is Searching?

This is my submission for the "Make the AI Judge Feel Curious" bounty. Rather than state something strange, `main.py` writes a single short text that stops mid-thought on purpose: it describes the tip-of-the-tongue state — the moment when you know a word's shape, sound, and first letter but not the word itself — and then asks where the word is hiding during that gap, and who is looking for it. The judge should finish reading before the question finishes asking.

The script keeps itself honest: it enforces the 1–280 character limit, writes the text to `entry.txt` inside `$MAKEFUN_OUTPUT_DIR` (default `/output`), and exits nonzero if the text ever drifts out of bounds.

## How to run

```
python3 main.py
```

No dependencies, just Python 3.

## Bounty

https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311

[![make.fun badge](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/geta4133-lgtm/curious-machines/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/geta4133-lgtm/curious-machines/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
