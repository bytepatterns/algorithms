"""
Flatten a Tree Into a Chain (medium) · patterns: preorder, explicit-stack

Given the root of a binary tree, rewire it in place into a chain that
follows preorder: the root first, then its left subtree, then its right
subtree. In the chain every node's left link is None and its right link
points to the next node in preorder. Only links may change; no new nodes may
be created.

Examples:

    Input:  tree = 7, left 3 (children 1 and 5), right 9 (left child 8)
    Output: chain 7 -> 3 -> 1 -> 5 -> 9 -> 8
    Why:    that is the preorder of the tree

    Input:  tree = 4, left 2, whose left is 1
    Output: chain 4 -> 2 -> 1
    Why:    the left spine becomes a right spine

    Input:  tree = empty
    Output: empty chain
    Why:    edge case, there is nothing to rewire

Approach:
    An explicit stack produces preorder: pop a node, push its right child,
    then its left child, so the left side comes off first. By the time a
    node is linked into the chain, its children are already saved on the
    stack, so rewriting the previous node's links can never lose part of the
    tree. The last node in preorder is always a leaf, so its links are
    already None. Time is O(n) and space is O(h) for the stack, for a tree
    of height h.

The lesson behind it: Tree Traversals
    https://bytepatterns.com/learn/trees/tree-traversals
    python trees/03-tree-traversals.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/flatten-a-tree-into-a-chain

Run it:  python problems/trees/11-flatten-a-tree-into-a-chain.py
"""


class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def flatten(root):
    stack, prev = ([root] if root else []), None
    while stack:
        node = stack.pop()
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)      # the left side comes off first
        if prev:
            prev.left, prev.right = None, node       # its children are already saved
        prev = node
    return root

def chain(node):
    out = []
    while node:
        out.append(node.val)
        node = node.right
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(chain(flatten(T(7, T(3, T(1), T(5)), T(9, T(8))))), [7, 3, 1, 5, 9, 8])
    check(chain(flatten(T(4, T(2, T(1))))), [4, 2, 1])
    check(chain(flatten(None)), [])
