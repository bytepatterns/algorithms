"""
Drop Nth From End (medium) · patterns: fast-slow-pointers, dummy-node

Given the head of a singly linked list and a number n, remove the node that
sits n positions from the end and return the head of the resulting list.
Counting starts at the last node, so n equal to 1 removes the tail. You may
assume n never exceeds the length of the list, and the goal is a single
traversal.

Examples:

    Input:  head = 1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5
    Why:    the second node from the end is 4

    Input:  head = 1 -> 2, n = 2
    Output: 2
    Why:    edge case, the removed node is the head itself

    Input:  head = 9, n = 1
    Output: empty
    Why:    edge case, removing the only node empties the list

Approach:
    Two pointers separated by a gap of n nodes move in lockstep, so when the
    leader reaches the last node the follower stands exactly one node before
    the target. Starting both at a dummy node placed before the head means
    removing the first node is handled by the same relink as any other
    position. That gives a single traversal instead of one pass to measure
    the length and another to cut. Time is O(L) for list length L, and space
    is O(1).

The lesson behind it: Fast and Slow Pointers
    https://bytepatterns.com/learn/linked-lists/fast-and-slow-pointers
    python linked-lists/05-fast-and-slow-pointers.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/drop-nth-from-end

Run it:  python problems/linked-lists/02-drop-nth-from-end.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def drop_nth_from_end(head, n):
    dummy = Node(0, head)            # lets head removal use the same relink
    lead = lag = dummy
    for _ in range(n):               # open a gap of exactly n nodes
        lead = lead.next
    while lead.next:                 # slide both until the leader hits the tail
        lead, lag = lead.next, lag.next
    lag.next = lag.next.next         # lag sits right before the victim
    return dummy.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(drop_nth_from_end(build([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5])
    check(dump(drop_nth_from_end(build([1, 2]), 2)), [2])
    check(dump(drop_nth_from_end(build([9]), 1)), [])
