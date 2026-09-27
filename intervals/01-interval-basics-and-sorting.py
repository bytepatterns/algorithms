"""
Interval Basics & Sorting: Sort by start and the pairwise question becomes a left-to-right scan.

An interval is just a pair: start and end. Two of them overlap when each
begins before the other finishes — one test, no special cases.

Checking every pair costs n squared. Sorting by start costs n log n and then
guarantees something useful: every interval you meet next starts at or after
the one you are holding.

Lesson 1 of Intervals, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/intervals/interval-basics-and-sorting

Run it:  python intervals/01-interval-basics-and-sorting.py
"""


meetings = [(9, 10), (13, 15), (9, 12), (11, 14)]
meetings.sort()                          # by start, ties broken by end
def overlap(a, b):
    return a[0] < b[1] and b[0] < a[1]   # touching ends do not count


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    spans = [(5, 8), (1, 4), (1, 2)]
    spans.sort()
    print(spans[0])


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
    print(meetings)
    print(overlap(meetings[0], meetings[1]), overlap(meetings[0], meetings[2]))

    # The exercise's answer, as the lesson page marks it.
    with expect_output("(1, 2)"):
        exercise()
