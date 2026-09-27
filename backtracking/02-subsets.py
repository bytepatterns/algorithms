"""
Subsets: Two branches per item: leave it out, or take it.

A subset is one yes-or-no answer per item, so the decision tree is binary:
skip nums[i], or take it and move on.

The index only ever moves forward, which is what stops {1, 2} and {2, 1}
both appearing. Every leaf is a complete set of decisions, so there are
exactly two to the power n of them — and the pop after the take branch is
again what keeps the shared path honest.

Lesson 2 of Backtracking, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/backtracking/subsets

Run it:  python backtracking/02-subsets.py
"""


def subsets(nums, i, path, out):
    if i == len(nums):               # every item has been decided
        out.append(path[:])
        return
    subsets(nums, i + 1, path, out)  # branch 1: leave nums[i] out
    path.append(nums[i])             # branch 2: take it
    subsets(nums, i + 1, path, out)
    path.pop()                       # un-choose before returning


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    out = []
    subsets([1, 2, 3], 0, [], out)
    print(len(out))


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
    out = []
    subsets([1, 2, 3], 0, [], out)
    print(len(out))
    print(out[:4])

    # The exercise's answer, as the lesson page marks it.
    with expect_output("8"):
        exercise()
