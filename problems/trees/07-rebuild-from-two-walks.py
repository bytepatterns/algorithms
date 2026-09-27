"""
Rebuild From Two Walks (hard) · patterns: divide-and-conquer, hash-map, recursion

You are handed the values of a binary tree in two orders: the walk that
visits a node before its subtrees, and the walk that visits the left
subtree, then the node, then the right subtree. All values are distinct.
Reconstruct the tree those two walks came from and return its root.

Examples:

    Input:  before = [3, 9, 20, 15, 7], middle = [9, 3, 15, 20, 7]
    Output: 3 with left child 9 and right child 20, whose children are 15 and 7

    Input:  before = [1, 2], middle = [2, 1]
    Output: 1 with a single left child 2
    Why:    the middle walk is what reveals the child hangs on the left

    Input:  before = [], middle = []
    Output: empty
    Why:    edge case, two empty walks describe an empty tree

Approach:
    The first unconsumed value of the before-walk is always the root of the
    subtree being built, and its position in the middle walk splits the
    remaining values into the left and right subtrees. Precomputing
    value-to-position in a map turns that split into a constant-time lookup
    instead of a scan, which is the difference between quadratic and linear.
    The before-walk is consumed through a single cursor, and the left
    subtree must be built before the right one so the cursor arrives at the
    correct value each time. Time is O(n) and space is O(n) for the map and
    the call stack.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/rebuild-from-two-walks

Run it:  python problems/trees/07-rebuild-from-two-walks.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
def show(n): return "." if n is None else "(%s %s %s)" % (n.val, show(n.left), show(n.right))

def rebuild(before, middle):
    place = {v: i for i, v in enumerate(middle)}   # value -> slot in the middle walk
    nxt = iter(before)
    def build(lo, hi):               # the subtree covering middle[lo..hi]
        if lo > hi:
            return None
        node = T(next(nxt))          # the before-walk names each root first
        node.left = build(lo, place[node.val] - 1)   # left first, to stay in step
        node.right = build(place[node.val] + 1, hi)
        return node
    return build(0, len(middle) - 1)


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
    check_printed(show(rebuild([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])), expect="(3 (9 . .) (20 (15 . .) (7 . .)))")
    check_printed(show(rebuild([1, 2], [2, 1])), expect="(1 (2 . .) .)")
    check_printed(show(rebuild([], [])), expect=".")
