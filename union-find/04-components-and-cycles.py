"""
Components & Cycles: Start the counter at n and drop it on every union that actually merges.

Give every element its own group and set a counter to n. Then walk the
edges.

A union that merges two different roots drops the counter by one. A union
that finds one shared root changes nothing — and that edge is exactly a
cycle, because both ends were already reachable from each other. One pass
answers both questions.

Lesson 4 of Union-Find, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/union-find/components-and-cycles

Run it:  python union-find/04-components-and-cycles.py
"""


parent = list(range(6))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    parent = list(range(4))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    count = 4
    for a, b in [(0, 1), (2, 3), (1, 3)]:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            count -= 1
    print(count)


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
    edges = [(0, 1), (1, 2), (0, 2), (3, 4)]
    components, cycles = 6, 0
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb: cycles += 1        # both ends already linked
        else: parent[ra], components = rb, components - 1
    print(components, cycles)

    # The exercise's answer, as the lesson page marks it.
    with expect_output("1"):
        exercise()
