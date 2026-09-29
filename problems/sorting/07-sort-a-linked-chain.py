"""
Sort a Linked Chain (medium) · patterns: divide-and-conquer, fast-slow-pointers

Given the head of a singly linked list of numbers, return the head of the
same nodes relinked into ascending order. Nodes may not be copied into a
Python list and sorted there; the answer should relink the existing nodes in
O(n log n) time. The list may be empty.

Examples:

    Input:  4 -> 1 -> 3 -> 1 -> 2
    Output: 1 -> 1 -> 2 -> 3 -> 4
    Why:    duplicates are kept, only the links change

    Input:  -3 -> 8
    Output: -3 -> 8
    Why:    already in order, so the relinking is a no-op

    Input:  empty
    Output: empty
    Why:    edge case, an empty chain is already sorted

Approach:
    Merge sort suits a chain because splitting and merging only ever walk
    forward along the links. The slow and fast pointers find the middle in
    one pass, and cutting the link there gives two independent chains.
    Merging behind a placeholder node relinks existing nodes without
    allocating new ones, and taking from the left chain on ties keeps the
    sort stable. Time is O(n log n), and space is O(log n) for the
    recursion.

The lesson behind it: Merge Sort
    https://bytepatterns.com/learn/sorting/merge-sort
    python sorting/05-merge-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/sort-a-linked-chain

Run it:  python problems/sorting/07-sort-a-linked-chain.py
"""


class N:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return N(v[0], build(v[1:])) if v else None     # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list

def sort_chain(head):
    if head is None or head.next is None:
        return head                  # zero or one node is already sorted
    slow, fast = head, head.next
    while fast and fast.next:        # slow stops at the end of the left half
        slow, fast = slow.next, fast.next.next
    right, slow.next = slow.next, None       # cut the chain in two
    a, b = sort_chain(head), sort_chain(right)
    tail = dummy = N(0)
    while a and b:                   # merge: always take the smaller head
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b               # one side may still have nodes
    return dummy.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(sort_chain(build([4, 1, 3, 1, 2]))), [1, 1, 2, 3, 4])
    check(dump(sort_chain(build([-3, 8]))), [-3, 8])
    check(dump(sort_chain(build([]))), [])
