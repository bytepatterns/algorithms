"""
Circular Queue: A fixed array that never shifts, because the ends wrap around.

A queue on a plain list is tempting until you see the cost: removing the
front shifts everything else down. A ring buffer never moves data. It moves
two numbers.

head marks the front, size says how many cells are live, and % capacity
folds any index past the end back to the beginning.

Lesson 8 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/circular-queue

Run it:  python stacks-queues/08-circular-queue.py
"""


class Ring:
    def __init__(self, cap):
        self.buf, self.head, self.size = [None] * cap, 0, 0
    def push(self, x):
        if self.size == len(self.buf): raise IndexError("full")
        self.buf[(self.head + self.size) % len(self.buf)] = x   # wrap with %
        self.size += 1
    def pop(self):
        x = self.buf[self.head]
        self.head = (self.head + 1) % len(self.buf)             # head walks the ring
        self.size -= 1
        return x


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
    r = Ring(3)
    for x in "abc": r.push(x)
    check_printed(r.pop(), r.pop(), expect="a b")
    r.push("d"); r.push("e")    # the two freed cells are reused, nothing shifts
    check_printed(r.buf, r.head, expect="['d', 'e', 'c'] 2")
