"""
Vertical Order Traversal: Give every node an x-coordinate and read the tree in columns.

Hang the tree on a grid. The root sits at column 0, a left child at one
column less, a right child at one more. Nodes sharing a column line up
vertically even when they sit in different branches.

Walk breadth-first, bucket each value by its column, then read the buckets
left to right.

Lesson 13 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/vertical-order-traversal

Run it:  python trees/13-vertical-order-traversal.py
"""


from collections import defaultdict, deque

class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def vertical(root):
    cols, q = defaultdict(list), deque([(root, 0)])   # the root owns column 0
    while q:
        n, c = q.popleft()                            # BFS fills each column top-down
        cols[c].append(n.val)
        if n.left: q.append((n.left, c - 1))          # left is one column out
        if n.right: q.append((n.right, c + 1))
    return [cols[c] for c in sorted(cols)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(vertical(Node(3, Node(9), Node(20, Node(15), Node(7)))), [[9], [3, 15], [20], [7]])
