"""
Zigzag Level Walk (medium) · patterns: bfs, level-order

Given the root of a binary tree, collect its values level by level, but
alternate the reading direction. The top level is read left to right, the
next level right to left, and so on down the tree. Return one list per
level, and an empty result for an empty tree.

Examples:

    Input:  tree = 3 with children 9 and 20, where 20 has children 15 and 7
    Output: [[3], [20, 9], [15, 7]]
    Why:    the middle level is reversed, the bottom level returns to normal

    Input:  tree = 1 alone
    Output: [[1]]
    Why:    a single level is read left to right

    Input:  tree = empty
    Output: []
    Why:    edge case, there are no levels to report

Approach:
    A queue drives a standard level-by-level traversal, and the size of the
    queue at the start of a round is exactly the width of the current level.
    Draining that many nodes collects one full level while enqueuing the
    next one. The zigzag is applied only when storing a finished level,
    reversing it on every other round, so the traversal itself never
    changes. Time is O(n) and space is O(w) for the widest level.

The lesson behind it: Level Order Traversal
    https://bytepatterns.com/learn/trees/level-order-traversal
    python trees/09-level-order-traversal.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/zigzag-level-walk

Run it:  python problems/trees/02-zigzag-level-walk.py
"""


from collections import deque
class T:
    def __init__(self, val, l=None, r=None): self.val, self.left, self.right = val, l, r
def zigzag(root):
    if not root: return []
    out, q, forward = [], deque([root]), True
    while q:
        level = []
        for _ in range(len(q)):      # the current queue size is one full level
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level if forward else level[::-1])
        forward = not forward        # flip the reading direction each level
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(zigzag(T(3, T(9), T(20, T(15), T(7)))), [[3], [20, 9], [15, 7]])
    check(zigzag(T(1)), [[1]])
    check(zigzag(None), [])
