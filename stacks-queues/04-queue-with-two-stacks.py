"""
Queue From Two Stacks: Reverse a reversal and LIFO turns into FIFO.

Keep an inbox stack for arrivals and an outbox stack for departures. When
the outbox runs dry, pour the whole inbox into it — the order flips, so the
oldest item now sits on top. Every item moves at most twice, which makes
dequeue O(1) amortized.

Lesson 4 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/queue-with-two-stacks

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python stacks-queues/04-queue-with-two-stacks.py
"""


class Queue:
    def __init__(self):
        self.inbox, self.outbox = [], []
    def enqueue(self, x):
        self.inbox.append(x)              # always cheap
    def dequeue(self):
        if not self.outbox:               # refill only when empty
            while self.inbox:             # pour: the order flips
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()          # oldest sits on top


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
    q = Queue()
    for x in [1, 2, 3]:
        q.enqueue(x)
    check_printed(q.dequeue(), q.dequeue(), expect="1 2")
