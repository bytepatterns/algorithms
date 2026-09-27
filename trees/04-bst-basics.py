"""
BST Basics: Smaller values left, larger values right, all the way down.

A binary search tree adds one rule to a binary tree: every value in a node's
left subtree is smaller than it, and every value on the right is larger. The
rule covers entire subtrees, not just direct children. Read the tree inorder
and the values arrive sorted.

Lesson 4 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/bst-basics

Run it:  python trees/04-bst-basics.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

# BST rule: everything left of a node is smaller, everything right is larger
root = Node(50, Node(30, Node(20), Node(40)), Node(70, Node(60), Node(80)))

def inorder(n):
    return [] if not n else inorder(n.left) + [n.val] + inorder(n.right)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(inorder(root), [20, 30, 40, 50, 60, 70, 80])  # sorted
    check(root.left.right.val, 40)  # right of 30, yet still left of 50
