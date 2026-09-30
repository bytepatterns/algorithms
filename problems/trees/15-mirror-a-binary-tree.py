"""
Mirror a Binary Tree (easy) · patterns: recursion, tree-traversal

A layout engine stores a page as a binary tree, and right-to-left languages
need the whole layout flipped. Given the root of a binary tree, swap the
left and right children of every node so the tree becomes its mirror image,
and return the root. The tree has up to 100 nodes. The examples show the
result read level by level, left to right.

Examples:

    Input:  tree = 4, left 2 (children 1 and 3), right 7 (children 6 and 9)
    Output: [4, 7, 2, 9, 6, 3, 1]
    Why:    7 now sits on the left, and every level reads backwards

    Input:  tree = 2, left 1, right 3
    Output: [2, 3, 1]

    Input:  tree = empty
    Output: []
    Why:    edge case, there is nothing to flip

Approach:
    A tree's mirror is its root with the mirrored right subtree on the left
    and the mirrored left subtree on the right, so the definition is already
    a recursion. Each call swaps its node's two children and recurses into
    both; an empty subtree returns straight away. Every node is swapped
    exactly once, so time is O(n), and space is O(h) for the recursion on a
    tree of height h.

The lesson behind it: Binary Trees
    https://bytepatterns.com/learn/trees/binary-trees
    python trees/02-binary-trees.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/mirror-a-binary-tree

Run it:  python problems/trees/15-mirror-a-binary-tree.py
"""


from collections import deque

class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def mirror(node):
    if node is None:
        return None
    node.left, node.right = mirror(node.right), mirror(node.left)   # swap flipped halves
    return node

def levels(root):
    out, q = [], deque([root] if root else [])
    while q:
        node = q.popleft()
        out.append(node.val)
        q.extend(c for c in (node.left, node.right) if c)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(levels(mirror(T(4, T(2, T(1), T(3)), T(7, T(6), T(9))))), [4, 7, 2, 9, 6, 3, 1])
    check(levels(mirror(T(2, T(1), T(3)))), [2, 3, 1])
    check(levels(mirror(None)), [])
