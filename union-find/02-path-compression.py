"""
Path Compression: You already walked to the root — leave everyone pointing straight at it.

Unions can build a long chain, and then every find re-walks it. But the walk
already learned the answer.

So make a second pass over the same path and point each node straight at the
root. The path you paid for once is flat for everyone who uses it
afterwards.

Lesson 2 of Union-Find, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/union-find/path-compression

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python union-find/02-path-compression.py
"""


parent = [1, 2, 3, 4, 4]        # a 0 -> 1 -> 2 -> 3 -> 4 chain
def find(x):
    root = x
    while parent[root] != root:  # first pass: locate the root
        root = parent[root]
    while parent[x] != root:     # second pass: re-point the whole path
        parent[x], x = root, parent[x]
    return root


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    parent = [1, 2, 2]
    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    find(0)
    print(parent)


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
    print(find(0), parent)

    # The exercise's answer, as the lesson page marks it.
    with expect_output("[2, 2, 2]"):
        exercise()
