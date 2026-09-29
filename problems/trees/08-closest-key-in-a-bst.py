"""
Closest Key in a BST (easy) · patterns: bst, search-path

A binary search tree stores distinct whole-number keys. Given its root and a
target that may have a fractional part, return the key closest to the
target. If two keys are equally close, return the smaller one. The tree
always has at least one node.

Examples:

    Input:  tree = 8, left 3 with children 1 and 6 (6 has children 4 and 7),
            right 10 with a right child 14; target = 5
    Output: 4
    Why:    4 and 6 are both one away, and 4 is the smaller

    Input:  same tree; target = 12.2
    Output: 14
    Why:    14 is 1.8 away while 10 is 2.2 away

    Input:  tree = a single node 7; target = -100
    Output: 7
    Why:    edge case, the only key is the closest one

Approach:
    A search for the target follows one root-to-leaf path, and the keys just
    below and just above the target both lie on it, because the search has
    to turn at each of them. The closest key is one of those two, so
    checking only the nodes on the path is enough. The tie rule is handled
    by comparing the pair of distance and key, which prefers the smaller key
    when distances match. Time is O(h) for a tree of height h, and space is
    O(1).

The lesson behind it: BST Insert and Search
    https://bytepatterns.com/learn/trees/bst-insert-and-search
    python trees/05-bst-insert-and-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/closest-key-in-a-bst

Run it:  python problems/trees/08-closest-key-in-a-bst.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def closest_key(node, target):
    best = node.val
    while node:
        # closer wins, and on a tie the smaller key wins
        if (abs(node.val - target), node.val) < (abs(best - target), best):
            best = node.val
        node = node.left if target < node.val else node.right
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    tree = T(8, T(3, T(1), T(6, T(4), T(7))), T(10, None, T(14)))
    check(closest_key(tree, 5), 4)
    check(closest_key(tree, 12.2), 14)
    check(closest_key(T(7), -100), 7)
