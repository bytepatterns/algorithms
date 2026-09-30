"""
Reverse Nodes in Groups of K (hard) · patterns: in-place-reversal, dummy-head

A packet buffer is stored as a singly linked list, and the transmitter needs
the packets reversed in blocks of k. Given the head of the list and an
integer k ≥ 1, reverse the nodes of each consecutive block of k and return
the new head. If fewer than k nodes remain at the end, leave them in their
original order. Rewire the next pointers rather than copying values, and use
only O(1) extra space. The list has up to 5,000 nodes.

Examples:

    Input:  list = 1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 2 -> 1 -> 4 -> 3 -> 5
    Why:    5 is a block of one, shorter than k, so it stays put

    Input:  list = 1 -> 2 -> 3 -> 4 -> 5, k = 3
    Output: 3 -> 2 -> 1 -> 4 -> 5

    Input:  list = 1 -> 2, k = 1
    Output: 1 -> 2
    Why:    edge case, blocks of one never change

Approach:
    A dummy node in front of the head means the first block is stitched in
    exactly like every later one. For each block, a walk of k steps first
    confirms the block is complete, because an incomplete tail must stay in
    order. The block is then reversed with the usual three-pointer loop,
    starting with its first node pointing at whatever follows the block, so
    the reversed block is already linked to the rest of the list. The node
    before the block is pointed at the new front, and the old front, now
    last in its block, becomes the node before the next block. Every node is
    visited a constant number of times, so time is O(n), and extra space is
    O(1).

The lesson behind it: Reverse a Linked List
    https://bytepatterns.com/learn/linked-lists/reverse-linked-list
    python linked-lists/04-reverse-linked-list.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/reverse-nodes-in-groups-of-k

Run it:  python problems/linked-lists/13-reverse-nodes-in-groups-of-k.py
"""


class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def reverse_in_groups(head, k):
    dummy = Node(0, head)
    before = dummy                          # node just before the current block
    while True:
        probe = before
        for _ in range(k):                  # is there a full block ahead?
            probe = probe.next
            if probe is None:
                return dummy.next
        after = probe.next                  # first node past the block
        prev, cur = after, before.next      # reversed block will point at `after`
        for _ in range(k):
            cur.next, prev, cur = prev, cur, cur.next
        first = before.next                 # old front, now the block's last node
        before.next = prev                  # prev is the new front
        before = first

def build(vals):
    head = None
    for v in reversed(vals):
        head = Node(v, head)
    return head

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(to_list(reverse_in_groups(build([1, 2, 3, 4, 5]), 2)), [2, 1, 4, 3, 5])
    check(to_list(reverse_in_groups(build([1, 2, 3, 4, 5]), 3)), [3, 2, 1, 4, 5])
    check(to_list(reverse_in_groups(build([1, 2]), 1)), [1, 2])
