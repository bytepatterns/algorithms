"""
Window Functions: Aggregate across rows without collapsing them.

A window function computes over a set of rows related to the current one,
then attaches the answer to that row. OVER (ORDER BY …) gives you running
totals and rankings; PARTITION BY restarts the calculation per group.
Nothing is folded away, so the detail stays.

Lesson 11 of SQL, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sql/window-functions

Run it:  python sql/11-window-functions.py
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
    import sqlite3
    db = sqlite3.connect(":memory:")
    db.executescript("""CREATE TABLE bake (day TEXT, loaves INT);
      INSERT INTO bake VALUES ('03-04',40),('03-05',55),('03-06',35),('03-07',70);""")
    with expect_output("('03-04', 40, 40, 3)", "('03-05', 55, 95, 2)", "('03-06', 35, 130, 4)", "('03-07', 70, 200, 1)"):
        for row in db.execute("""
          SELECT day, loaves,
                 SUM(loaves) OVER (ORDER BY day) AS so_far,
                 RANK()      OVER (ORDER BY loaves DESC) AS busiest
          FROM bake ORDER BY day"""):
            print(row)
