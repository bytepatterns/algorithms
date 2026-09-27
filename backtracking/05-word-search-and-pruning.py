"""
Word Search & Pruning: Walk the grid, block the cell, and quit on the first wrong letter.

Spelling a word in a letter grid is backtracking on a board instead of a
list. From the current cell, the four neighbours are the branches.

Two lines do the pruning. The first rejects a cell whose letter is wrong or
that is off the board, killing that whole subtree immediately. The second
writes a blocking marker into the cell before recursing and restores it
afterwards, so one path cannot reuse a letter while a different path still
can.

Lesson 5 of Backtracking, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/backtracking/word-search-and-pruning

Run it:  python backtracking/05-word-search-and-pruning.py
"""


grid = [["s", "n", "a"], ["b", "a", "k"], ["t", "p", "o"]]
def find(r, c, word, k):
    if k == len(word): return True
    if not (0 <= r < 3 and 0 <= c < 3) or grid[r][c] != word[k]:
        return False                       # off the board or wrong letter
    grid[r][c] = "#"                       # blocked for this path only
    ok = any(find(r + dr, c + dc, word, k + 1)
             for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
    grid[r][c] = word[k]                   # un-choose
    return ok


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    print(find(0, 0, "snap", 0), find(0, 0, "snip", 0))


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
    print(find(0, 0, "snap", 0), find(0, 0, "snip", 0))

    # The exercise's answer, as the lesson page marks it.
    with expect_output("True False"):
        exercise()
