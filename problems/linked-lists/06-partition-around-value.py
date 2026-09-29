"""
Partition Around Value (medium) · patterns: dummy-node, list-splitting

Given the head of a singly linked list and a pivot value, rearrange the
nodes so every node holding a value below the pivot comes before every node
holding a value at or above it. Inside each of the two groups the nodes keep
the order they had originally. The pivot itself need not appear in the list.

Examples:

    Input:  head = 1 -> 4 -> 3 -> 2 -> 5 -> 2, pivot = 3
    Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5
    Why:    both groups keep their original internal order

    Input:  head = 2 -> 1, pivot = 2
    Output: 1 -> 2
    Why:    a node equal to the pivot belongs to the upper group

    Input:  head = empty, pivot = 0
    Output: empty
    Why:    edge case, there is nothing to partition

Approach:
    Two chains are grown side by side during one walk of the original list,
    each appending at its tail so the original relative order survives
    inside both groups. Throwaway starter nodes remove the empty-chain
    special cases, and the join at the end is two pointer writes. The high
    chain must be terminated explicitly, because its last node still carries
    whatever link it had in the original list and would otherwise loop back.
    Time is O(n) and space is O(1), since only links change.

The lesson behind it: Traversal and Search
    https://bytepatterns.com/learn/linked-lists/traversal-and-search
    python linked-lists/02-traversal-and-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/partition-around-value

Run it:  python problems/linked-lists/06-partition-around-value.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def partition_around(head, pivot):
    low = low_tail = Node(0)         # values below the pivot, in original order
    high = high_tail = Node(0)       # values at or above the pivot
    while head:
        if head.val < pivot: low_tail.next, low_tail = head, head
        else: high_tail.next, high_tail = head, head
        head = head.next
    high_tail.next = None            # the old tail still points into the past
    low_tail.next = high.next        # stitch the two chains together
    return low.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(partition_around(build([1, 4, 3, 2, 5, 2]), 3)), [1, 2, 2, 4, 3, 5])
    check(dump(partition_around(build([2, 1]), 2)), [1, 2])
    check(dump(partition_around(build([]), 0)), [])
