"""
Height-Balanced Tree Check (easy) · patterns: post-order, early-exit

A search index keeps its keys in a binary tree and rebuilds it whenever it
gets lopsided. A tree is height-balanced when, at every node, the heights of
the left and right subtrees differ by at most 1. Given the root of a binary
tree, return True if it is height-balanced. The tree has up to 5,000 nodes,
so computing the height again from every node is wasteful.

Examples:

    Input:  tree = 3, left 9, right 20 (children 15 and 7)
    Output: True

    Input:  tree = 1, left 2 (left child 3 with children 4 and 4, right child 3), right 2
    Output: False
    Why:    at the root the left side is 3 levels deep and the right side only 1

    Input:  tree = empty
    Output: True
    Why:    edge case, an empty tree has nothing out of balance

Approach:
    A single post-order walk returns each subtree's height to its parent, so
    every node can check its own balance from numbers its children already
    worked out. When a node finds its two heights differ by more than one,
    it returns -1 instead of a height, and every ancestor passes that -1
    straight up without doing more work. The tree is balanced exactly when
    the root does not return -1. Every node is visited once, so time is
    O(n), and space is O(h) for the recursion.

The lesson behind it: Tree Depth and Balance
    https://bytepatterns.com/learn/trees/tree-depth-and-balance
    python trees/07-tree-depth-and-balance.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/height-balanced-tree-check

Run it:  python problems/trees/17-height-balanced-tree-check.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_balanced(root):
    def height(node):                  # height, or -1 if unbalanced below
        if node is None:
            return 0
        lh = height(node.left)
        if lh == -1:
            return -1
        rh = height(node.right)
        if rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)
    return height(root) != -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_balanced(T(3, T(9), T(20, T(15), T(7)))), True)
    check(is_balanced(T(1, T(2, T(3, T(4), T(4)), T(3)), T(2))), False)
    check(is_balanced(None), True)
