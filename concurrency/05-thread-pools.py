"""
Thread Pools: Hire the workers once, reuse them all day.

A thread pool keeps a fixed crew of workers alive and feeds them tasks from
a queue. Threads are created once, not per task, and the pool size is a
deliberate cap on how much work runs at once.

Lesson 5 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/thread-pools

Run it:  python concurrency/05-thread-pools.py
"""


from concurrent.futures import ThreadPoolExecutor

def fetch_size(page):
    return page, len(page) * 100      # stands in for a slow network call


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    from concurrent.futures import ThreadPoolExecutor

    def double(n):
        return n * 2

    with ThreadPoolExecutor(max_workers=3) as pool:
        out = list(pool.map(double, [1, 2, 3, 4]))

    print(out)


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
    pages = ["index", "about", "pricing", "faq"]

    with ThreadPoolExecutor(max_workers=2) as pool:
        # two workers, four tasks; map hands results back in input order
        for page, size in pool.map(fetch_size, pages):
            print(page, size)

    # The exercise's answer, as the lesson page marks it.
    with expect_output("[2, 4, 6, 8]"):
        exercise()
