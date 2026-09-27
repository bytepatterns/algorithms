"""
Tree Traversals: Same nodes, same recursion, three different reading orders.

Visiting every node means choosing when to handle the node itself. Preorder
handles it before its children, inorder between the left and right subtrees,
and postorder after both. One tree, one recursion, a single line moved.

Lesson 3 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/tree-traversals

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python trees/03-tree-traversals.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

root = Node("B", Node("A"), Node("C"))

def preorder(n):  return [] if not n else [n.val] + preorder(n.left) + preorder(n.right)
def inorder(n):   return [] if not n else inorder(n.left) + [n.val] + inorder(n.right)
def postorder(n): return [] if not n else postorder(n.left) + postorder(n.right) + [n.val]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(preorder(root), ['B', 'A', 'C'])  # node first
    check(inorder(root), ['A', 'B', 'C'])  # node in the middle
    check(postorder(root), ['A', 'C', 'B'])  # node last
