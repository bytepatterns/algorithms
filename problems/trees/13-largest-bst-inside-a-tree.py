"""
Largest BST Inside a Tree (medium) · patterns: post-order, bst

A binary tree holds whole-number keys, and keys may repeat. A subtree means
a node together with all of its descendants. Return the number of nodes in
the largest subtree that is a valid binary search tree, where every key in a
node's left subtree is strictly smaller than the node and every key in its
right subtree is strictly larger. An empty tree has answer 0.

Examples:

    Input:  tree = 6, left 4 (children 2 and 5, and 2 has a left child 1),
            right 9 (children 7 and 3)
    Output: 4
    Why:    the subtree under 4 holds 1, 2, 4, 5 in order; 3 under 9 spoils the rest

    Input:  tree = 5, left 3, right 8 (children 7 and 9)
    Output: 5
    Why:    the whole tree is already a valid search tree

    Input:  tree = empty
    Output: 0
    Why:    edge case, no nodes at all

Approach:
    A post-order walk answers every subtree using only what its children
    already reported, so no subtree is examined twice. An empty child
    reports itself as valid with a smallest key of plus infinity and a
    largest key of minus infinity, which makes the range test pass for
    missing children. An invalid child makes the parent invalid too, since
    the parent's subtree contains it. Time is O(n), and space is O(h) for
    the recursion on a tree of height h.

The lesson behind it: Validate a BST
    https://bytepatterns.com/learn/trees/validate-bst
    python trees/06-validate-bst.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/largest-bst-inside-a-tree

Run it:  python problems/trees/13-largest-bst-inside-a-tree.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def largest_bst(root):
    best = 0
    def walk(node):                      # -> (valid, size, smallest, largest)
        nonlocal best
        if node is None:
            return True, 0, float("inf"), float("-inf")
        l_ok, l_size, l_lo, l_hi = walk(node.left)
        r_ok, r_size, r_lo, r_hi = walk(node.right)
        if l_ok and r_ok and l_hi < node.val < r_lo:
            size = l_size + r_size + 1
            best = max(best, size)
            return True, size, min(l_lo, node.val), max(r_hi, node.val)
        return False, 0, 0, 0            # the numbers no longer matter
    walk(root)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(largest_bst(T(6, T(4, T(2, T(1)), T(5)), T(9, T(7), T(3)))), 4)
    check(largest_bst(T(5, T(3), T(8, T(7), T(9)))), 5)
    check(largest_bst(None), 0)
