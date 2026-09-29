"""
Meeting Rooms: Count how many run at once; the high-water mark is the room count.

You never need to know which meeting sits in which room — only how many are
live at once.

Sort the starts and the ends into two separate lists and sweep. A start
claims a room; an end reached before that start frees one. The highest the
counter ever reaches is the answer.

Lesson 4 of Intervals, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/intervals/meeting-rooms

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python intervals/04-meeting-rooms.py
"""


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    starts = [1, 2, 3]
    ends = [4, 5, 6]
    rooms = peak = j = 0
    for s in starts:
        while ends[j] <= s:
            rooms -= 1; j += 1
        rooms += 1
        peak = max(peak, rooms)
    print(peak)


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
    meetings = [(0, 30), (5, 10), (15, 20)]
    starts = sorted(s for s, _ in meetings)
    ends = sorted(e for _, e in meetings)
    rooms = peak = j = 0
    for s in starts:
        while ends[j] <= s:      # a room freed up before this meeting starts
            rooms -= 1; j += 1
        rooms += 1               # this meeting claims a room
        peak = max(peak, rooms)
    print(peak)

    # The exercise's answer, as the lesson page marks it.
    with expect_output("3"):
        exercise()
