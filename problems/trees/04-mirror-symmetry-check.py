"""
Mirror Symmetry Check (easy) · patterns: recursion, paired-traversal

Decide whether a binary tree is a mirror image of itself, as if a vertical
line ran down through the root. Both the shape and the values have to match
across that line. An empty tree counts as symmetric.

Examples:

    Input:  tree = 1, left 2 with children 3 and 4, right 2 with children 4 and 3
    Output: True
    Why:    the right subtree is the left subtree read back to front

    Input:  tree = 1, left 2 with right child 3, right 2 with right child 3
    Output: False
    Why:    the two threes hang on the same side, so the shape is not mirrored

    Input:  tree = empty
    Output: True
    Why:    edge case, nothing is trivially symmetric

Approach:
    The natural recursion is over pairs rather than single nodes: two
    subtrees mirror each other when their roots agree and their children
    mirror crosswise, outer against outer and inner against inner. The base
    case has to distinguish both absent, which is a match, from one absent,
    which is a shape mismatch, and an identity comparison covers both at
    once. Every node is visited once. Time is O(n), and space is O(h) for
    the call stack.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/mirror-symmetry-check

Run it:  python problems/trees/04-mirror-symmetry-check.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def is_symmetric(root):
    def mirrors(a, b):
        if a is None or b is None:
            return a is b            # true only when both are absent
        # outer child against outer child, inner child against inner child
        return (a.val == b.val and mirrors(a.left, b.right)
                and mirrors(a.right, b.left))
    return root is None or mirrors(root.left, root.right)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_symmetric(T(1, T(2, T(3), T(4)), T(2, T(4), T(3)))), True)
    check(is_symmetric(T(1, T(2, None, T(3)), T(2, None, T(3)))), False)
    check(is_symmetric(None), True)
