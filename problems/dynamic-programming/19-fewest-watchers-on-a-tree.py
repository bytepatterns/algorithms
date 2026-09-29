"""
Fewest Watchers on a Tree (hard) · patterns: tree-dp, state-machine

A watcher placed on a node of a binary tree keeps an eye on that node, its
parent and its children. Return the fewest watchers needed so that every
node in the tree is watched. An empty tree needs none.

Examples:

    Input:  tree = 1, left 2, whose children are 3 and 4
    Output: 1
    Why:    a watcher on 2 covers 1, 3 and 4 as well as itself

    Input:  tree = a chain of five nodes, each the left child of the one before
    Output: 2
    Why:    watchers on the second and fourth nodes cover all five

    Input:  tree = a single node
    Output: 1
    Why:    edge case, the root has to watch itself

Approach:
    Each node returns three costs for its subtree, always with everything
    below the node covered: the node holds a watcher, the node is watched by
    a child, or the node waits for its parent. A missing child counts as
    already watched at no cost and can never hold a watcher. A watcher on
    the node lets each child take its cheapest state, including waiting; the
    watched state takes each child's better of holding or watched and pays
    the smallest extra to make one child hold a watcher. The root has no
    parent, so its waiting state is not allowed. Time is O(n) and space is
    O(h) for the recursion, for a tree of height h.

The lesson behind it: DP on Trees
    https://bytepatterns.com/learn/dynamic-programming/dp-on-trees
    python dynamic-programming/17-dp-on-trees.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/fewest-watchers-on-a-tree

Run it:  python problems/dynamic-programming/19-fewest-watchers-on-a-tree.py
"""


INF = float("inf")

class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def fewest_watchers(root):
    def costs(node):
        # (holds a watcher, watched by a child, waits for its parent)
        if not node:
            return INF, 0, INF                   # nothing to watch, cannot hold one
        kids = (costs(node.left), costs(node.right))
        hold = 1 + sum(min(k) for k in kids)      # this watcher also covers the children
        base = sum(min(h, w) for h, w, _ in kids)
        watched = base + min(h - min(h, w) for h, w, _ in kids)   # one child must hold
        waits = sum(w for _, w, _ in kids)
        return hold, watched, waits
    return min(costs(root)[:2]) if root else 0


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_watchers(T(1, T(2, T(3), T(4)))), 1)
    check(fewest_watchers(T(1, T(2, T(3, T(4, T(5)))))), 2)
    check(fewest_watchers(T(9)), 1)
