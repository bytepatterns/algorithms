"""
Right Edge View (medium) · patterns: bfs, level-order

Imagine standing to the right of a binary tree and looking straight at it.
Return the values you can see, ordered from the top of the tree downward.
Exactly one value is visible per level: the rightmost node on that level,
whichever subtree it happens to belong to.

Examples:

    Input:  tree = 1, left child 2 with right child 5, right child 3 with right child 4
    Output: [1, 3, 4]
    Why:    node 5 is hidden behind node 4 on the same level

    Input:  tree = 1 with a single left child 2
    Output: [1, 2]
    Why:    edge case, a left-only node is still the rightmost on its level

    Input:  tree = empty
    Output: []
    Why:    edge case, there is nothing to see

Approach:
    A level-order traversal exposes each level as a contiguous batch of
    queue entries, and the visible node is simply the last entry of each
    batch. Queuing left children before right ones guarantees the final node
    drained from a level is its rightmost one, even when it descends from a
    left subtree. Nodes below a hidden one still get queued, so lower levels
    remain complete. Time is O(n) and space is O(w) for the widest level.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/right-edge-view

Run it:  python problems/trees/03-right-edge-view.py
"""


from collections import deque
class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right
def right_view(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        n = len(q)                   # exactly the nodes on this level
        for i in range(n):
            node = q.popleft()
            if i == n - 1: out.append(node.val)   # last one taken is visible
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(right_view(T(1, T(2, None, T(5)), T(3, None, T(4)))), [1, 3, 4])
    check(right_view(T(1, T(2))), [1, 2])
    check(right_view(None), [])
