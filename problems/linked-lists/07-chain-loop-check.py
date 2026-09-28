"""
Loop in a Chain (easy) · patterns: fast-slow-pointers, cycle-detection

You receive the head of a singly linked chain of nodes. Somewhere a node may
point back to an earlier node, which makes the walk go round forever instead
of reaching the end. Return True if the chain contains such a loop and False
if following the links eventually reaches None. In the examples the chain is
described by its values plus pos, the index the last node links back to, or
-1 for no loop.

Examples:

    Input:  values = [3, 2, 0, -4], pos = 1
    Output: True
    Why:    the last node links back to the node holding 2

    Input:  values = [1, 2], pos = -1
    Output: False
    Why:    the walk ends after the second node

    Input:  values = [7], pos = 0
    Output: True
    Why:    edge case, a single node that points to itself

Approach:
    Two pointers start at the head, one moving one link per step and the
    other moving two. Without a loop the fast pointer reaches the end and
    the answer is False. With a loop both pointers eventually circle inside
    it, and since the gap between them shrinks by one link every step, the
    fast pointer must land exactly on the slow one. Time is O(n) and space
    is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/chain-loop-check

Run it:  python problems/linked-lists/07-chain-loop-check.py
"""


class Node:
    def __init__(self, val): self.val, self.next = val, None
def build(values, pos):               # the tail links back to index pos, or nowhere if -1
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]): a.next = b
    if nodes and pos >= 0: nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None
def has_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next   # the gap closes by one link per step
        if slow is fast:
            return True
    return False                      # the fast pointer found the end


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(has_loop(build([3, 2, 0, -4], 1)), True)
    check(has_loop(build([1, 2], -1)), False)
    check(has_loop(build([7], 0)), True)
