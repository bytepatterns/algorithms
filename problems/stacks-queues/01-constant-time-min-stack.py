"""
Constant Time Min Stack (easy) · patterns: stack, auxiliary-stack

Design a stack that supports pushing a value, popping the top value, reading
the top value, and reporting the smallest value currently stored. Every one
of those operations must run in constant time, so scanning the contents to
find the minimum is not acceptable. You may assume the minimum is only
requested while the stack is non-empty.

Examples:

    Operations: push 5, push 2, push 7
    minimum -> 2, top -> 7

    Operations: pop, pop        (starting from the stack above)
    minimum -> 5, top -> 5
    Why:       popping 2 must restore the earlier minimum

    Operations: push 3, push 3, pop
    minimum -> 3
    Why:       edge case, duplicate minimums must survive one pop

Approach:
    A second stack mirrors the main one, storing at each level the minimum
    of everything at or below that level. Pushing records the smaller of the
    incoming value and the previous minimum, so the mirror top is always the
    answer. Popping discards both tops together, which restores the earlier
    minimum automatically and handles duplicate minimums correctly. Every
    operation is O(1) time, and space is O(n) for the extra stack.

The lesson behind it: Min Stack
    https://bytepatterns.com/learn/stacks-queues/min-stack
    python stacks-queues/06-min-stack.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/constant-time-min-stack

Run it:  python problems/stacks-queues/01-constant-time-min-stack.py
"""


class MinStack:
    def __init__(self): self.items, self.mins = [], []   # mins mirrors the running minimum
    def push(self, x):
        self.items.append(x)
        # each level remembers the minimum of everything at or below it
        self.mins.append(x if not self.mins else min(x, self.mins[-1]))
    def pop(self):
        self.mins.pop()              # both stacks always shrink together
        return self.items.pop()
    def top(self): return self.items[-1]
    def minimum(self): return self.mins[-1]


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
    s = MinStack()
    for v in (5, 2, 7): s.push(v)
    check_printed(s.minimum(), s.top(), expect="2 7")
    s.pop(); s.pop()
    check_printed(s.minimum(), s.top(), expect="5 5")
