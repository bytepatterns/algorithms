"""
Your Own Call Stack: Not a tail call? Then carry the stack yourself.

When work remains after the recursive call, a loop alone cannot replace it —
something has to remember where to come back to. So keep that stack
yourself.

For an inorder walk: dive left, pushing every node you pass. When the left
runs out, pop, report, and turn right. The pushed nodes are the pending
frames.

Lesson 8 of Recursion, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/recursion/your-own-call-stack

Run it:  python recursion/08-your-own-call-stack.py
"""


class Node:
    def __init__(self, v, l=None, r=None): self.val, self.left, self.right = v, l, r

def inorder(root):
    out, stack, n = [], [], root
    while stack or n:
        while n:                      # walk left as far as it goes, noting the way back
            stack.append(n); n = n.left
        n = stack.pop()               # nothing further left, so this node is next
        out.append(n.val)
        n = n.right                   # now do the same on its right side
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(inorder(Node(4, Node(2, Node(1), Node(3)), Node(5))), [1, 2, 3, 4, 5])
