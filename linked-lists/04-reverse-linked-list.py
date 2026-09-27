"""
Reverse a Linked List: Flip every arrow backwards using three pointers.

Walk the list once, turning each link to face the node behind it. Three
pointers do the work: prev trails, node is current, and a temporary holds
the rest of the chain before you overwrite it. The old tail becomes the new
head.

Lesson 4 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/reverse-linked-list

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python linked-lists/04-reverse-linked-list.py
"""


class Node:
    def __init__(self, v): self.value, self.next = v, None

def reverse(head):
    prev, node = None, head
    while node:
        nxt = node.next        # remember the rest of the list
        node.next = prev       # flip this link backwards
        prev, node = node, nxt # slide both pointers forward
    return prev                # the old tail is the new head


# The predict-output exercise from the lesson page. Guess first, then run.
def exercise():
    class Node:
        def __init__(self, v): self.value, self.next = v, None

    a = Node(1); a.next = Node(2)
    prev = None
    while a:
        nxt = a.next
        a.next = prev
        prev, a = a, nxt
    print(prev.value, prev.next.value)


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
    head = Node(1); head.next = Node(2); head.next.next = Node(3)
    node = reverse(head)
    while node:                    # prints 3 2 1
        print(node.value, end=" "); node = node.next

    # The exercise's answer, as the lesson page marks it.
    with expect_output("2 1"):
        exercise()
