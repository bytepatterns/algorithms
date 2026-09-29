"""
Weave List Halves (medium) · patterns: fast-slow-pointers, list-reversal

Given the head of a singly linked list holding at least one node, rearrange
it so the nodes alternate between the front and the back: first node, last
node, second node, second-to-last node, and so on. The nodes themselves must
be relinked, not copied into a new list. Return the head of the rearranged
list.

Examples:

    Input:  head = 1 -> 2 -> 3 -> 4
    Output: 1 -> 4 -> 2 -> 3

    Input:  head = 1 -> 2 -> 3
    Output: 1 -> 3 -> 2
    Why:    an odd length leaves the middle node at the end

    Input:  head = 7
    Output: 7
    Why:    edge case, a single node is already in the required order

Approach:
    Three classic moves compose into the answer: find the midpoint with a
    slow and fast pointer, reverse the second half in place, then zip the
    two chains together one node at a time. Splitting at the midpoint
    guarantees the front chain is never shorter than the reversed back
    chain, so the zip ends cleanly on odd and even lengths alike. Everything
    happens by relinking, so no second list is built. Time is O(L) across
    the three passes, and space is O(1).

The lesson behind it: Reverse a Linked List
    https://bytepatterns.com/learn/linked-lists/reverse-linked-list
    python linked-lists/04-reverse-linked-list.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/weave-list-halves

Run it:  python problems/linked-lists/03-weave-list-halves.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def weave(head):
    slow = fast = head               # slow stops at the end of the first half
    while fast.next and fast.next.next: slow, fast = slow.next, fast.next.next
    back, slow.next = slow.next, None            # cut the list in two
    prev = None
    while back: back.next, prev, back = prev, back, back.next   # reverse the tail
    front = head
    while prev:                      # zip one node from each chain
        nf, nb = front.next, prev.next
        front.next, prev.next = prev, nf
        front, prev = nf, nb
    return head


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(weave(build([1, 2, 3, 4]))), [1, 4, 2, 3])
    check(dump(weave(build([1, 2, 3]))), [1, 3, 2])
    check(dump(weave(build([7]))), [7])
