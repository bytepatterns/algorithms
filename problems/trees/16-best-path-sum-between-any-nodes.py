"""
Best Path Sum Between Any Nodes (hard) · patterns: post-order, tree-dp, global-best

An org chart is a binary tree where each node holds a profit or loss as an
integer, possibly negative. A path is any sequence of nodes joined by
parent-child edges that never visits a node twice; it does not have to pass
through the root, and it has at least one node. Return the largest sum of
node values along any path. The tree has up to 30,000 nodes with values
between -1,000 and 1,000.

Examples:

    Input:  tree = -10, left 9, right 20 (children 15 and 7)
    Output: 42
    Why:    the path 15 -> 20 -> 7 skips the loss at the root

    Input:  tree = 1, left 2, right 3
    Output: 6

    Input:  tree = -3
    Output: -3
    Why:    edge case, a path needs at least one node even when every value is negative

Approach:
    Every path has one highest node where it bends, and from there it runs
    down into the left subtree, the right subtree, both, or neither. A
    post-order walk computes, for every node, the best downward sum starting
    at it, and any child whose best downward sum is negative is dropped,
    since leaving it out is better. The best path bending at the node is its
    value plus both kept sides, which updates a global answer, but only one
    side can be passed up, because a parent's path cannot use both of a
    child's branches. The answer starts at minus infinity so an all-negative
    tree still returns its largest single value. Time is O(n), and space is
    O(h) for the recursion.

The lesson behind it: Diameter of a Tree
    https://bytepatterns.com/learn/trees/tree-diameter
    python trees/10-tree-diameter.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/best-path-sum-between-any-nodes

Run it:  python problems/trees/16-best-path-sum-between-any-nodes.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def best_path_sum(root):
    best = float("-inf")
    def gain(node):                               # best downward sum starting here
        nonlocal best
        if node is None:
            return 0
        left = max(gain(node.left), 0)            # drop a losing branch
        right = max(gain(node.right), 0)
        best = max(best, node.val + left + right) # the path that bends at this node
        return node.val + max(left, right)        # a parent can use only one side
    gain(root)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best_path_sum(T(-10, T(9), T(20, T(15), T(7)))), 42)
    check(best_path_sum(T(1, T(2), T(3))), 6)
    check(best_path_sum(T(-3)), -3)
