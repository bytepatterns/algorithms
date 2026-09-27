"""
Diameter of a Tree: The longest path bends at exactly one node — find that node.

The longest path between any two nodes turns at one node only. At that node
the path is simply the left depth plus the right depth.

So compute depths once, bottom-up, and at every node ask "would bending here
beat the best so far?" The value returned upwards is still just a depth.

Lesson 10 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/tree-diameter

Run it:  python trees/10-tree-diameter.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def diameter(root):
    best = 0
    def depth(n):                    # returns a depth, records the best path on the way up
        nonlocal best
        if not n: return 0
        l, r = depth(n.left), depth(n.right)
        best = max(best, l + r)      # the path that bends here, at n
        return 1 + max(l, r)         # what n reports to its own parent
    depth(root)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(diameter(Node(1, Node(2, Node(4), Node(5)), Node(3))), 3)  # 4-2-1-3
