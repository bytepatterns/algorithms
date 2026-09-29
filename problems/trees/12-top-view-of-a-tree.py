"""
Top View of a Tree (medium) · patterns: bfs, column-index

Place a binary tree on a grid: the root in column 0, each left child one
column left of its parent and each right child one column right. Looking
down from above, only the highest node in each column is visible. Return the
visible values from the leftmost column to the rightmost; when two nodes tie
for highest in a column, the one further left in their level is the one you
see.

Examples:

    Input:  tree = 1, left 2, right 3; 2 has a right child 4,
            4 has a right child 5, 5 has a right child 6
    Output: [2, 1, 3, 6]
    Why:    4 and 5 hide below 1 and 3; only 6 reaches column 2

    Input:  tree = 8, left 4, whose left is 2
    Output: [2, 4, 8]
    Why:    each node of the left spine opens a new column

    Input:  tree = empty
    Output: []
    Why:    edge case, nothing to see

Approach:
    Breadth-first search meets nodes in order of depth, and within one depth
    from left to right, which matches the tie rule, so the first node
    recorded in a column is the visible one. A dictionary keeps the first
    value per column and ignores every later one. Every column between the
    leftmost and the rightmost holds some node, because a path from the root
    moves one column per step, so reading the range from its minimum to its
    maximum needs no sort. Time is O(n) and space is O(n).

The lesson behind it: Vertical Order Traversal
    https://bytepatterns.com/learn/trees/vertical-order-traversal
    python trees/13-vertical-order-traversal.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/top-view-of-a-tree

Run it:  python problems/trees/12-top-view-of-a-tree.py
"""


from collections import deque

class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def top_view(root):
    first, queue = {}, deque([(root, 0)] if root else [])
    while queue:
        node, col = queue.popleft()
        first.setdefault(col, node.val)          # the first visit to a column is the highest
        if node.left: queue.append((node.left, col - 1))
        if node.right: queue.append((node.right, col + 1))
    return [first[c] for c in range(min(first), max(first) + 1)] if first else []


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(top_view(T(1, T(2, None, T(4, None, T(5, None, T(6)))), T(3))), [2, 1, 3, 6])
    check(top_view(T(8, T(4, T(2)))), [2, 4, 8])
    check(top_view(None), [])
