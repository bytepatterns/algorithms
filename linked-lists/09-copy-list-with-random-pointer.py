"""
Copy a List With Random Links: Clone the nodes first, wire the pointers second.

Each node carries a second pointer that can aim anywhere — forwards,
backwards, at itself. Copying in one pass is impossible: the target may not
exist yet.

So split it. Pass one creates a bare copy of every node and records old to
new. Pass two reads that map and translates both links. O(n) time, O(n)
space.

Lesson 9 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/copy-list-with-random-pointer

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python linked-lists/09-copy-list-with-random-pointer.py
"""


class Node:
    def __init__(self, v): self.val, self.next, self.rand = v, None, None

def copy(head):
    clone = {None: None}                   # old node -> its fresh copy
    n = head
    while n: clone[n] = Node(n.val); n = n.next        # pass 1: bare copies
    n = head
    while n:                                           # pass 2: translate both fields
        clone[n].next, clone[n].rand = clone[n.next], clone[n.rand]
        n = n.next
    return clone[head]


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
    a, b = Node("a"), Node("b")
    a.next, a.rand, b.rand = b, b, b
    c = copy(a)
    check_printed(c.val, c.next.val, c.rand is b, c.rand is c.next, expect="a b False True")
