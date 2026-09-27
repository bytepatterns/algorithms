"""
Context Windows: A hard limit on what the model can see at once.

The context window is the most tokens a model can attend to in one call.
Instructions, history, retrieved passages and the reply all share it, and
anything outside it simply does not exist for the model.

Lesson 10 of AI & ML, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/ai-ml/context-windows

Run it:  python ai-ml/10-context-windows.py
"""


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    history = [("system", 50), ("user", 200), ("assistant", 300), ("user", 100)]
    budget = 500

    used = 0
    for role, size in reversed(history):
        if used + size > budget:
            break
        used += size

    print(used)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import io
import re
import sys


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


class expect_output:
    """Capture everything the block prints and compare it line by line."""

    def __init__(self, *lines):
        self.lines = list(lines)

    def __enter__(self):
        self.buffer, self.stdout = io.StringIO(), sys.stdout
        sys.stdout = self.buffer

    def __exit__(self, *exc):
        sys.stdout = self.stdout
        printed = self.buffer.getvalue()
        print(printed, end="")
        got = [line.rstrip() for line in printed.splitlines()]
        want = self.lines
        if len(want) == 1 and " / " in want[0] and len(got) > 1:
            want = want[0].split(" / ")
        assert exc[0] or _lines_match(got, want), f"expected {want!r}, got {got!r}"


def _lines_match(got, want):
    if not want:
        return not got
    if want[0].strip() in ("...", "\u2026"):  # the lesson elides some lines
        return any(_lines_match(got[i:], want[1:]) for i in range(len(got) + 1))
    return bool(got) and _same(got[0], want[0]) and _lines_match(got[1:], want[1:])


if __name__ == "__main__":
    history = [("system", 20), ("user", 300), ("assistant", 250),
               ("user", 180), ("assistant", 400), ("user", 120)]
    budget = 700

    kept, used = [], 0
    for role, size in reversed(history):     # newest turns first
        if used + size > budget:
            break                            # everything older is dropped
        kept.append((role, size)); used += size

    print(list(reversed(kept)), used)        # note: the system turn fell off

    # The exercise's answer, as the lesson page marks it.
    with expect_output("400"):
        exercise()
