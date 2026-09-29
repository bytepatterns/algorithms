"""
Lowest Common Ancestor: Walk down from the root until the two targets part ways.

The lowest common ancestor of two nodes is the deepest node that still has
both below it. In a BST you never really search: start at the root and keep
stepping while both targets lie the same way. The node where they split is
the answer.

Lesson 8 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/lowest-common-ancestor

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python trees/08-lowest-common-ancestor.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def lca(node, a, b):
    while node:
        if a < node.val and b < node.val:   node = node.left    # both smaller
        elif a > node.val and b > node.val: node = node.right   # both larger
        else: return node.val               # they split here, so this is the LCA
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    root = Node(6, Node(2, Node(0), Node(4)), Node(8, Node(7), Node(9)))
    check(lca(root, 0, 4), 2)
    check(lca(root, 2, 8), 6)  # the paths split right at the root
    check(lca(root, 7, 9), 8)
