"""
Widest Node To Node Path (medium) · patterns: dfs, post-order

In a binary tree, measure the longest path between any two nodes, counting
the links along it rather than the nodes. The path does not have to pass
through the root, and it may bend at exactly one node on the way. Return 0
for an empty tree or a tree with a single node.

Examples:

    Input:  tree = 1 with left child 2 having children 4 and 5, and right child 3
    Output: 3
    Why:    the path 4, 2, 1, 3 uses three links and bends at the root

    Input:  tree = 1 with a single left child 2
    Output: 1
    Why:    a single link is the only path there is

    Input:  tree = empty
    Output: 0
    Why:    edge case, there is no path to measure

Approach:
    Every path bends at a single node and descends as far as possible on
    both sides, so the best path through a given node is the sum of its two
    subtree depths. One bottom-up traversal computes depths and, at each
    node, scores that sum against a running record. The value reported to
    the parent is different from the value scored, because a parent can only
    continue down one side. Each node is visited once. Time is O(n), and
    space is O(h) for the call stack.

The lesson behind it: Diameter of a Tree
    https://bytepatterns.com/learn/trees/tree-diameter
    python trees/10-tree-diameter.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/widest-node-to-node-path

Run it:  python problems/trees/06-widest-node-to-node-path.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def widest_path(root):
    best = 0
    def depth(node):
        nonlocal best
        if node is None:
            return 0
        left, right = depth(node.left), depth(node.right)
        best = max(best, left + right)   # the path that bends right here
        return 1 + max(left, right)      # a parent can only use one side
    depth(root)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(widest_path(T(1, T(2, T(4), T(5)), T(3))), 3)
    check(widest_path(T(1, T(2))), 1)
    check(widest_path(None), 0)
