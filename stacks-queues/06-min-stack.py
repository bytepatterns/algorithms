"""
Min Stack: Carry the answer up with the data instead of recomputing it.

A stack can hand back its top in O(1), but its minimum would need a scan. So
record the minimum at push time, on a second stack that rises and falls with
the first.

Pop both together and the old minimum reappears by itself — no
recomputation, ever.

Lesson 6 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/min-stack

Run it:  python stacks-queues/06-min-stack.py
"""


class MinStack:
    def __init__(self): self.main, self.mins = [], []
    def push(self, x):
        self.main.append(x)
        # the minimum of everything below, stored beside the value
        self.mins.append(x if not self.mins else min(x, self.mins[-1]))
    def pop(self):
        self.mins.pop()
        return self.main.pop()
    def min(self): return self.mins[-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


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
    for x in [5, 2, 7, 1]: s.push(x)
    check_printed(s.min(), s.mins, expect="1 [5, 2, 2, 1]")
    s.pop()                  # the 1 leaves
    check(s.min(), 2)  # the old minimum is simply back on top
