"""
Path Sum Variants: Same tree, three questions — and three different things to carry.

"Does a root-to-leaf path add up to the target?" is answered by carrying the
remainder down: subtract each node, and a leaf only has to hit zero.

"How many paths anywhere add up to it?" needs more: at each node, keep the
running sum of every path an ancestor started, plus one starting here.

Lesson 11 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/path-sum-variants

Run it:  python trees/11-path-sum-variants.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def has_path(n, target):                  # root to leaf: carry the remainder down
    if not n: return False
    rest = target - n.val
    if not n.left and not n.right: return rest == 0
    return has_path(n.left, rest) or has_path(n.right, rest)

def count_paths(n, target, open_sums=()):        # any node down to any node
    if not n: return 0
    sums = [s + n.val for s in open_sums] + [n.val]   # grow every open path, open one more
    return (sums.count(target)
            + count_paths(n.left, target, sums)
            + count_paths(n.right, target, sums))


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
    root = Node(5, Node(4, Node(11)), Node(8, Node(3)))
    check_printed(has_path(root, 20), count_paths(root, 11), expect="True 2")
