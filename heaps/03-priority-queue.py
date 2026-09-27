"""
Priority Queue: Serve by urgency, not by who shouted first.

A priority queue hands out the most urgent item, whatever time it arrived. A
heap is the natural engine: push and pop in O(log n), peek in O(1).

Python's heapq compares whatever you push, so push tuples. Convention is
(priority, tiebreak, item) — tuples compare left to right, and the counter
both keeps equal priorities in arrival order and stops Python from ever
comparing the payloads.

Lesson 3 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/priority-queue

Run it:  python heaps/03-priority-queue.py
"""


import heapq, itertools

berth, tick = [], itertools.count()    # tick breaks ties, keeps FIFO

def request(priority, ship):
    heapq.heappush(berth, (priority, next(tick), ship))

def next_ship():
    return heapq.heappop(berth)[2]     # lowest number = most urgent


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    for p, s in [(2, "Kestrel"), (1, "Aurora"), (2, "Bellona")]:
        request(p, s)
    check_printed(next_ship(), expect="Aurora")
    check_printed(next_ship(), expect="Kestrel - tied, but queued first")
