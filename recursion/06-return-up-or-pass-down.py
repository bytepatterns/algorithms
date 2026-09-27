"""
Return Up or Pass Down: Every recursion moves information one of two ways. Pick one.

Recursive functions differ in which direction information travels. Return
up: children compute, the parent combines, the answer grows on the way back.

Pass down: the parent hands context to each child as an argument, and a base
case reports a finished result. Choosing the wrong direction is why a
recursion turns into a tangle of globals.

Lesson 6 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/return-up-or-pass-down

Run it:  python recursion/06-return-up-or-pass-down.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def deepest(n):                  # RETURN UP: the children answer, the parent combines
    if not n: return 0
    return 1 + max(deepest(n.left), deepest(n.right))

def paths(n, so_far=()):         # PASS DOWN: the parent hands context to the children
    if not n: return []
    trail = (*so_far, n.val)
    if not n.left and not n.right: return [trail]
    return paths(n.left, trail) + paths(n.right, trail)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    root = Node(1, Node(2, Node(4)), Node(3))
    check(deepest(root), 3)
    check(paths(root), [(1, 2, 4), (1, 3)])
