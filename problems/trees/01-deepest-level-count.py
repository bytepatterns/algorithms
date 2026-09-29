"""
Deepest Level Count (easy) · patterns: dfs, recursion

Given the root of a binary tree, return the number of levels on the longest
path from the root down to any leaf. A tree with only a root counts as one
level, and an empty tree counts as zero.

Examples:

    Input:  tree = 3 with children 9 and 20, where 20 has children 15 and 7
    Output: 3
    Why:    the path 3, 20, 15 covers three levels

    Input:  tree = 1 with a right child 2, whose right child is 3
    Output: 3
    Why:    a completely lopsided tree still counts every level

    Input:  tree = empty
    Output: 0
    Why:    edge case, there are no levels to count

Approach:
    Depth is defined recursively: an absent node contributes zero levels,
    and a present node contributes one more than the deeper of its two
    subtrees. That single rule handles balanced and lopsided trees
    identically, with no special case beyond the empty child. Every node is
    visited exactly once. Time is O(n), and space is O(h) for the call
    stack, where h is the height of the tree.

The lesson behind it: Tree Depth and Balance
    https://bytepatterns.com/learn/trees/tree-depth-and-balance
    python trees/07-tree-depth-and-balance.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/deepest-level-count

Run it:  python problems/trees/01-deepest-level-count.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def depth(node):
    if node is None: return 0        # an absent branch adds no level
    # a node sits exactly one level above its deeper subtree
    return 1 + max(depth(node.left), depth(node.right))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(depth(T(3, T(9), T(20, T(15), T(7)))), 3)
    check(depth(T(1, None, T(2, None, T(3)))), 3)
    check(depth(None), 0)
