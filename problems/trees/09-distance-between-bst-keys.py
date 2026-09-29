"""
Distance Between Two BST Keys (medium) · patterns: bst, lowest-common-ancestor

A binary search tree stores distinct keys, and two of its keys a and b are
given, both guaranteed to be in the tree. Return the number of edges on the
path that connects the node holding a to the node holding b. When a equals b
the answer is 0.

Examples:

    Input:  tree = 8, left 3 with children 1 and 6 (6 has children 4 and 7),
            right 10 with a right child 14; a = 4, b = 14
    Output: 5
    Why:    the path is 4, 6, 3, 8, 10, 14

    Input:  same tree; a = 6, b = 7
    Output: 1
    Why:    7 is a child of 6

    Input:  same tree; a = 10, b = 10
    Output: 0
    Why:    edge case, a node is zero edges from itself

Approach:
    The path between two nodes passes through their lowest common ancestor,
    so its length is the depth of a below that node plus the depth of b
    below it. In a BST the ancestor is the first node on the way down where
    the two keys split to different sides or where one of them is found,
    exactly as in the lesson. From there, two ordinary BST searches count
    the steps to each key. Time is O(h) for a tree of height h, and space is
    O(1).

The lesson behind it: Lowest Common Ancestor
    https://bytepatterns.com/learn/trees/lowest-common-ancestor
    python trees/08-lowest-common-ancestor.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/distance-between-bst-keys

Run it:  python problems/trees/09-distance-between-bst-keys.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def bst_distance(root, a, b):
    node = root
    while (a < node.val and b < node.val) or (a > node.val and b > node.val):
        node = node.left if a < node.val else node.right   # both lie the same way
    def steps(n, key):               # edges from n down to key by BST search
        d = 0
        while n.val != key:
            n = n.left if key < n.val else n.right
            d += 1
        return d
    return steps(node, a) + steps(node, b)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    tree = T(8, T(3, T(1), T(6, T(4), T(7))), T(10, None, T(14)))
    check(bst_distance(tree, 4, 14), 5)
    check(bst_distance(tree, 6, 7), 1)
    check(bst_distance(tree, 10, 10), 0)
