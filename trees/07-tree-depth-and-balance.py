"""
Tree Depth and Balance: Height decides speed, and balance decides height.

Height is the longest chain of links from a node down to a leaf, and it
decides what every tree operation costs. A tree is balanced when the two
sides of each node differ in height by at most one. Balanced means height
near log n; skewed means height n.

Lesson 7 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/tree-depth-and-balance

Run it:  python trees/07-tree-depth-and-balance.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def height(n):
    return 0 if n is None else 1 + max(height(n.left), height(n.right))

def is_balanced(n):
    if n is None: return True
    gap = abs(height(n.left) - height(n.right))    # sides may differ by 1 at most
    return gap <= 1 and is_balanced(n.left) and is_balanced(n.right)


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
    full = Node(2, Node(1), Node(3))
    skew = Node(1, None, Node(2, None, Node(3)))       # a chain wearing a tree costume
    check_printed(height(full), is_balanced(full), expect="2 True")
    check_printed(height(skew), is_balanced(skew), expect="3 False")
