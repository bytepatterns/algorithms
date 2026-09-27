"""
Level Order Traversal: A queue turns a tree into one tidy row per depth.

Push the root, then repeatedly take the front node and push its children.
That is breadth-first order — everything at depth 1, then everything at
depth 2.

To get one list per level, read the queue's length before the loop. Whatever
is in there right now is exactly this level.

Lesson 9 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/level-order-traversal

Run it:  python trees/09-level-order-traversal.py
"""


from collections import deque

class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def levels(root):
    out, q = [], deque([root])
    while q:
        row = []
        for _ in range(len(q)):          # exactly the nodes standing on this level
            n = q.popleft()
            row.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(row)                  # one list per level, depth for free
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(levels(Node(3, Node(9), Node(20, Node(15), Node(7)))), [[3], [9, 20], [15, 7]])
