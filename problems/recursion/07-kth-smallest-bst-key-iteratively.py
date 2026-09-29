"""
Kth Smallest BST Key, Iteratively (medium) · patterns: explicit-stack, inorder

A binary search tree holds distinct integer keys. Given its root and a
number k, return the k-th smallest key, counting from 1, or None if the tree
has fewer than k keys. Do it without recursion, since the tree may be a
chain far deeper than the call stack allows, and stop as soon as the answer
is known.

Examples:

    Input:  tree = 8, left 3 with children 1 and 6 (6 has children 4 and 7),
            right 10 with a right child 14; k = 4
    Output: 6
    Why:    in order the keys read 1, 3, 4, 6, 7, 8, 10, 14

    Input:  same tree; k = 8
    Output: 14
    Why:    the largest key is the last one in order

    Input:  same tree; k = 9
    Output: None
    Why:    edge case, the tree holds only eight keys

Approach:
    This is the inorder walk with the call stack made explicit: stepping
    left pushes each node that still owes a visit, and popping one means
    everything smaller has already been reported. Counting down k as nodes
    are popped finds the answer at the k-th pop, and returning there skips
    the rest of the tree. The stack never holds more than one path from the
    root, and the depth of the tree no longer matters to the interpreter.
    Time is O(h + k) and space is O(h), for a tree of height h.

The lesson behind it: Your Own Call Stack
    https://bytepatterns.com/learn/recursion/your-own-call-stack
    python recursion/08-your-own-call-stack.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/kth-smallest-bst-key-iteratively

Run it:  python problems/recursion/07-kth-smallest-bst-key-iteratively.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def kth_smallest_key(root, k):
    stack, node = [], root
    while stack or node:
        while node:                   # step left, noting the way back
            stack.append(node)
            node = node.left
        node = stack.pop()            # everything smaller is already counted
        k -= 1
        if k == 0:
            return node.val           # stop early: the rest is never visited
        node = node.right
    return None                       # fewer than k keys


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    tree = T(8, T(3, T(1), T(6, T(4), T(7))), T(10, None, T(14)))
    check(kth_smallest_key(tree, 4), 6)
    check(kth_smallest_key(tree, 8), 14)
    check(kth_smallest_key(tree, 9), None)
