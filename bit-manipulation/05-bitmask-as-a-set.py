"""
Bitmask as a Set: An integer is a subset; counting to 2^n lists them all.

Give each item a lane. Then one integer describes a whole subset: lane i is
1 when item i is in.

Counting from 0 to 2^n - 1 therefore enumerates every subset, in order, with
no recursion. Union is |, intersection is &, membership is mask >> i & 1.

Lesson 5 of Bit Manipulation, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/bit-manipulation/bitmask-as-a-set

Run it:  python bit-manipulation/05-bitmask-as-a-set.py
"""


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
    items = ["a", "b", "c"]

    with expect_output("0 000 []", "1 001 ['a']", "2 010 ['b']", "3 011 ['a', 'b']", "...", "7 111 ['a', 'b', 'c']"):
        for mask in range(1 << len(items)):   # 0 .. 7
            picked = [items[i] for i in range(len(items)) if mask >> i & 1]
            print(mask, format(mask, "03b"), picked)
