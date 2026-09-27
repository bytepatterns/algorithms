"""
Rebuild From Traversals: Preorder names the root, inorder says where to cut.

Neither list alone determines a tree, but together they do. Preorder hands
you the root first. Find that root in the inorder list and everything to its
left is the left subtree, everything to its right the right one.

Slice both lists the same way and recurse. The subtree sizes always match.

Lesson 14 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/build-tree-from-traversals

Run it:  python trees/14-build-tree-from-traversals.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def build(pre, ino):
    if not pre: return None
    root = pre[0]                          # preorder hands you the root first
    k = ino.index(root)                    # inorder splits the rest into two sides
    return Node(root,
                build(pre[1:k + 1], ino[:k]),      # k nodes belong on the left
                build(pre[k + 1:], ino[k + 1:]))

def show(n): return [] if not n else show(n.left) + [n.val] + show(n.right)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    tree = build([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    check(show(tree), [9, 3, 15, 20, 7])  # the inorder we were handed
    check(tree.right.left.val, 15)
