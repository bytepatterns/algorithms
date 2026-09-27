"""
Observer Pattern: One event, many reactions, and the source knows none of them.

One object holds a list of callbacks. When something happens, it walks the
list and calls each one, ignoring what they do and what they return.
Reactions are added or removed without touching the source, which is why the
list is the whole design.

Lesson 7 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/observer-pattern

Run it:  python lld/07-observer-pattern.py
"""


class Line:                                       # the subject
    def __init__(self): self.watchers = []
    def subscribe(self, fn): self.watchers.append(fn)
    def pull_cord(self, station):
        for fn in self.watchers: fn(station)      # fire and forget, in order


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    log = []
    board = lambda s: log.append("board: halt " + s)
    pager = lambda s: log.append("pager: go to " + s)

    line = Line()
    line.subscribe(board)
    line.subscribe(pager)
    line.pull_cord("weld-3")
    check(log, ['board: halt weld-3', 'pager: go to weld-3'])
