"""
Sizing a Thread Pool: More threads stop helping the moment the work stops waiting.

A pool size is a bet about where the bottleneck is. CPU-bound work saturates
at roughly the core count; extra threads only add context switches. IO-bound
work spends its time blocked, so many more threads fit. Either way the
longest single task is a floor nothing can go below.

Lesson 13 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/sizing-a-thread-pool

Run it:  python concurrency/13-sizing-a-thread-pool.py
"""


def makespan(tasks, workers):
    free = [0.0] * workers                 # when each worker is next idle
    for cost in sorted(tasks, reverse=True):
        first = min(range(workers), key=lambda w: free[w])
        free[first] += cost
    return max(free)


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
    jobs = [4, 4, 4, 4, 1, 1, 1, 1]            # 20 units of work, longest is 4
    with expect_output("1 20.0 / 2 10.0 / 4 5.0 / 8 4.0 / 16 4.0 -- the longest task is the floor"):
        for n in (1, 2, 4, 8, 16):
            print(n, makespan(jobs, n))
