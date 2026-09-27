"""
BST Insert and Search: One comparison per level throws away half the tree.

Searching a BST is one comparison per level: smaller means go left, larger
means go right, and the other side is discarded outright. Insertion follows
that identical path and stops at the first empty slot. Both cost O(h), the
height of the tree.

Lesson 5 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/bst-insert-and-search

Run it:  python trees/05-bst-insert-and-search.py
"""


class Node:
    def __init__(self, v): self.val, self.left, self.right = v, None, None
def insert(root, v):
    if root is None: return Node(v)        # empty slot: the value lands here
    if v < root.val: root.left = insert(root.left, v)
    else: root.right = insert(root.right, v)
    return root
def search(root, v):
    while root and root.val != v:          # each step drops one whole side
        root = root.left if v < root.val else root.right
    return root is not None


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
    root = Node(50)
    for v in [30, 70, 20, 40]: insert(root, v)
    check_printed(search(root, 40), search(root, 45), expect="True False")
