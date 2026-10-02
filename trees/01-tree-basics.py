"""
Tree Basics: One root, many branches, and no way back up.

A tree stores values in nodes that fan out downward. One node is the root;
every other node has exactly one parent, and nodes with no children are
leaves. Links only point down, so a tree has no cycles and no way back up.

Lesson 1 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/tree-basics

Run it:  python trees/01-tree-basics.py
"""


class Node:
    def __init__(self, v, kids=None): self.val, self.kids = v, kids or []

root = Node("home", [Node("docs", [Node("cv.pdf")]), Node("photos")])

def height(node):                      # longest link count below this node
    return 0 if not node.kids else 1 + max(height(k) for k in node.kids)


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
    check_printed(root.val, expect="home  -> the root")
    check([k.val for k in root.kids], ['docs', 'photos'])
    check(root.kids[1].kids == [], True)  # photos is a leaf
    check(height(root), 2)  # edges to the deepest file
