"""
Validate a BST: Checking the parent is not enough; carry a range down.

Checking that each node beats its own parent is not enough, because a node
can satisfy its parent and still break an ancestor's rule. Carry a valid
range down instead: stepping left tightens the upper bound, stepping right
raises the lower one.

Lesson 6 of Trees & BST, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/trees/validate-bst

Run it:  python trees/06-validate-bst.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def is_bst(n, low=float('-inf'), high=float('inf')):
    if n is None: return True                    # an empty tree is valid
    if not (low < n.val < high): return False    # inherited range, not the parent
    return (is_bst(n.left, low, n.val) and       # going left tightens the cap
            is_bst(n.right, n.val, high))        # going right raises the floor


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    good = Node(5, Node(3), Node(8))
    bad = Node(5, Node(3, None, Node(6)), Node(8))   # 6 beats 3 but sits left of 5
    check(is_bst(good), True)
    check(is_bst(bad), False)
