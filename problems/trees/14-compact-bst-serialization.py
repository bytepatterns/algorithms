"""
Compact BST Serialization (medium) · patterns: preorder, monotonic-stack, bst

Write encode(root), which turns a binary search tree with distinct
whole-number keys into a string, and decode(text), which rebuilds the exact
same tree. The string may contain only the keys separated by single spaces,
with no markers for missing children, so it is as short as the keys allow.
Both functions should run in linear time and should not recurse, because the
tree can be as tall as it has nodes.

Examples:

    Input:  tree = 8, left 3 (children 1 and 6), right 10 (right child 14)
    Output: encode -> "8 3 1 6 10 14"
            decode("8 3 1 6 10 14") rebuilds the same shape
    Why:    pre-order lists each node before its children

    Input:  tree = a chain 1 -> 2 -> 3, each key the right child of the previous one
    Output: encode -> "1 2 3"
    Why:    decode knows 2 cannot be a left child of 1, since 2 is larger

    Input:  tree = empty
    Output: encode -> ""
            decode("") -> empty tree
    Why:    edge case, nothing to write

Approach:
    In pre-order a node comes before its whole subtree, so the first key is
    the root, and the search order decides everything else. The decoder
    keeps the path from the root on a stack; a key larger than the stack's
    top has left that node's left subtree, so nodes are popped until the
    next one is larger than the new key, and the new key becomes the right
    child of the last one popped. If nothing was popped, the new key is the
    left child of the top. Each node is pushed and popped at most once. Time
    is O(n) for both functions, and space is O(n).

The lesson behind it: Serialize a Tree
    https://bytepatterns.com/learn/trees/serialize-and-deserialize
    python trees/12-serialize-and-deserialize.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/compact-bst-serialization

Run it:  python problems/trees/14-compact-bst-serialization.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def encode(root):
    keys, stack = [], [root] if root else []
    while stack:                          # iterative pre-order
        node = stack.pop()
        keys.append(str(node.val))
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return " ".join(keys)

def decode(text):
    keys = [int(k) for k in text.split()]
    if not keys: return None
    root = T(keys[0]); path = [root]
    for k in keys[1:]:
        node, parent = T(k), None
        while path and path[-1].val < k:  # k has left these nodes' left subtrees
            parent = path.pop()
        if parent: parent.right = node
        else: path[-1].left = node
        path.append(node)
    return root


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
    tree = T(8, T(3, T(1), T(6)), T(10, None, T(14)))
    check_printed(encode(tree), expect="8 3 1 6 10 14")
    check(encode(decode("1 2 3")) == "1 2 3", True)
    check(decode(""), None)
