"""
Root To Leaf Target Sum (easy) · patterns: dfs, recursion

Given a binary tree and a target number, decide whether some path from the
root down to a leaf has values adding up exactly to the target. A leaf is a
node with no children, so a path must always end at the bottom of the tree.
Values may be negative.

Examples:

    Input:  tree = 5, left 4 with left child 11 having children 7 and 2,
            right 8 with children 13 and 4; target = 22
    Output: True
    Why:    the path 5, 4, 11, 2 adds up to 22

    Input:  tree = 1 with a single left child 2; target = 1
    Output: False
    Why:    the root is not a leaf, so the path cannot stop there

    Input:  tree = empty; target = 0
    Output: False
    Why:    edge case, an empty tree has no root-to-leaf path at all

Approach:
    Carrying the remaining amount downward turns the question at each node
    into the same question on a smaller tree, so one recursion covers the
    whole search. The absent-branch case must answer no rather than checking
    the remainder, otherwise a node with a single child would be treated as
    a valid endpoint. A leaf answers by comparing the remainder with its own
    value, and the two children are combined with a short-circuiting or.
    Time is O(n) in the worst case, and space is O(h) for the call stack.

The lesson behind it: Path Sum Variants
    https://bytepatterns.com/learn/trees/path-sum-variants
    python trees/11-path-sum-variants.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/root-to-leaf-target-sum

Run it:  python problems/trees/05-root-to-leaf-target-sum.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def has_path_sum(node, target):
    if node is None:
        return False                 # an absent branch is not a stopping point
    rest = target - node.val
    if node.left is None and node.right is None:
        return rest == 0             # only a leaf may close the path
    return has_path_sum(node.left, rest) or has_path_sum(node.right, rest)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(has_path_sum(T(5, T(4, T(11, T(7), T(2))), T(8, T(13), T(4))), 22), True)
    check(has_path_sum(T(1, T(2)), 1), False)
    check(has_path_sum(None, 0), False)
