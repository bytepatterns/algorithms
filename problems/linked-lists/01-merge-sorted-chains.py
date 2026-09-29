"""
Merge Sorted Chains (easy) · patterns: two-pointers, dummy-node

Two singly linked lists are each already sorted in non-decreasing order.
Splice them into one sorted list by relinking the existing nodes rather than
creating new ones. Return the head of the merged list, which is empty when
both inputs are empty.

Examples:

    Input:  a = 1 -> 4 -> 6, b = 2 -> 3
    Output: 1 -> 2 -> 3 -> 4 -> 6

    Input:  a = empty, b = 7
    Output: 7
    Why:    edge case, one side runs out before the loop starts

    Input:  a = empty, b = empty
    Output: empty
    Why:    edge case, there is nothing to merge

Approach:
    The two chains are consumed front to front, always taking the smaller
    head and appending it to the tail of the result. A dummy starter node
    means the first append needs no special handling, and the real head is
    simply the node after it. When one chain runs dry, the other is already
    sorted, so the remainder is attached in one move instead of node by
    node. Time is O(n + m) and space is O(1), since only pointers change.

The lesson behind it: Merge Two Sorted Lists
    https://bytepatterns.com/learn/linked-lists/merge-two-sorted-lists
    python linked-lists/08-merge-two-sorted-lists.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/merge-sorted-chains

Run it:  python problems/linked-lists/01-merge-sorted-chains.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def merge_sorted(a, b):
    dummy = tail = Node(0)           # starter node removes the empty-result case
    while a and b:
        if a.val <= b.val: tail.next, a = a, a.next
        else: tail.next, b = b, b.next
        tail = tail.next             # the attached node is the new tail
    tail.next = a or b               # the leftover chain is already sorted
    return dummy.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(merge_sorted(build([1, 4, 6]), build([2, 3]))), [1, 2, 3, 4, 6])
    check(dump(merge_sorted(build([]), build([7]))), [7])
    check(dump(merge_sorted(build([]), build([]))), [])
