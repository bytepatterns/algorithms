"""
Ring Buffer Deque (medium) · patterns: circular-buffer, design

Design a double-ended queue whose capacity is fixed when it is created.
push_front and push_back add a value and return True, or return False
without adding anything when the queue is full; pop_front and pop_back
remove and return a value, or return None when the queue is empty. Every
operation must take O(1) time, so no stored value may ever be shifted.

Examples:

    Operations: RingDeque(3), push_back 1, push_back 2, push_front 0, push_back 9
    Results:    True, True, True, False
    Why:        the fourth push finds all three cells taken

    Operations: pop_back, pop_front, pop_front, pop_front   (continuing)
    Results:    2, 0, 1, None
    Why:        front to back the queue held 0, 1, 2

    Operations: RingDeque(1), push_front 5, pop_back
    Results:    True, 5
    Why:        edge case, with one cell the front and the back are the same slot

Approach:
    The values never move: a head index and a size describe where the live
    run sits inside a fixed array, and the modulo folds any index past
    either end back into range. Python's modulo returns a non-negative
    result for a negative left side, so (head - 1) % capacity steps back
    from index 0 to the last cell. The back value always sits at head + size
    - 1, wrapped, so both ends are reachable in constant time. Every
    operation is O(1) time, and space is O(capacity).

The lesson behind it: Circular Queue
    https://bytepatterns.com/learn/stacks-queues/circular-queue
    python stacks-queues/08-circular-queue.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/ring-buffer-deque

Run it:  python problems/stacks-queues/08-ring-buffer-deque.py
"""


class RingDeque:
    def __init__(self, capacity):
        self.buf, self.head, self.size = [None] * capacity, 0, 0
    def push_front(self, x):
        if self.size == len(self.buf): return False
        self.head = (self.head - 1) % len(self.buf)    # step back, wrapping to the end
        self.buf[self.head] = x
        self.size += 1
        return True
    def push_back(self, x):
        if self.size == len(self.buf): return False
        self.buf[(self.head + self.size) % len(self.buf)] = x
        self.size += 1
        return True
    def pop_front(self):
        if not self.size: return None
        x, self.head = self.buf[self.head], (self.head + 1) % len(self.buf)
        self.size -= 1
        return x
    def pop_back(self):
        if not self.size: return None
        self.size -= 1                                 # the back slot is just past the new end
        return self.buf[(self.head + self.size) % len(self.buf)]


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
    d = RingDeque(3)
    check_printed(d.push_back(1), d.push_back(2), d.push_front(0), d.push_back(9), expect="True True True False")
    check_printed(d.pop_back(), d.pop_front(), d.pop_front(), d.pop_front(), expect="2 0 1 None")
    one = RingDeque(1)
    check_printed(one.push_front(5), one.pop_back(), expect="True 5")
