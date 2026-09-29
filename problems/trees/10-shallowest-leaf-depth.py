"""
Shallowest Leaf Depth (easy) · patterns: bfs, level-order

Given the root of a binary tree, return the number of nodes on the shortest
path from the root down to a leaf, where a leaf is a node with no children.
An empty tree has depth 0. A node with only one child is not a leaf, so a
path through it has to continue into that child.

Examples:

    Input:  tree = 6, left 2 (whose left is 1, whose left is 0), right 9
    Output: 2
    Why:    9 is a leaf one step below the root

    Input:  tree = 1, right 2, whose right is 3
    Output: 3
    Why:    1 and 2 each have a child, so only 3 is a leaf

    Input:  tree = empty
    Output: 0
    Why:    edge case, there are no nodes

Approach:
    Breadth-first search removes nodes in order of depth, so the first leaf
    it removes is a shallowest leaf and the search can stop there. That
    early stop pays off when a leaf sits near the root of a large tree,
    where a depth-first walk would still visit every node. The easy mistake
    is taking the smaller of the two subtree depths at a one-child node: the
    missing side reports 0 and the node is wrongly treated as a leaf. Time
    is O(n) in the worst case, and space is O(w) for the widest level held
    in the queue.

The lesson behind it: Tree Basics
    https://bytepatterns.com/learn/trees/tree-basics
    python trees/01-tree-basics.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/trees/shallowest-leaf-depth

Run it:  python problems/trees/10-shallowest-leaf-depth.py
"""


from collections import deque

class T:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def min_depth(root):
    if not root:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth                  # BFS meets the shallowest leaf first
        for child in (node.left, node.right):
            if child:
                queue.append((child, depth + 1))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(min_depth(T(6, T(2, T(1, T(0))), T(9))), 2)
    check(min_depth(T(1, None, T(2, None, T(3)))), 3)
    check(min_depth(None), 0)
