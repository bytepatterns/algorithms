"""
Doubly Linked Lists: Add a backwards pointer and removal stops needing a search.

A prev field costs one pointer per node and changes what is cheap. Given a
node, both of its neighbours are in hand, so unlinking is two assignments
and no walking.

Two sentinel nodes — a permanent head and tail that hold no data — mean
every node always has neighbours, so the edge cases vanish.

Lesson 10 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/doubly-linked-lists

Run it:  python linked-lists/10-doubly-linked-lists.py
"""


class Node:
    def __init__(self, v): self.val, self.prev, self.next = v, None, None

def unlink(n):                               # O(1): both neighbours are already in hand
    n.prev.next, n.next.prev = n.next, n.prev
    n.prev = n.next = None

def insert_after(at, n):
    n.prev, n.next = at, at.next
    at.next.prev, at.next = n, n


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    head, tail = Node("head"), Node("tail")      # sentinels: no None checks anywhere
    head.next, tail.prev = tail, head
    for v in "abc": insert_after(head, Node(v))  # each one lands at the front
    unlink(head.next.next)                       # drop the middle node
    n, out = head.next, []
    while n is not tail: out.append(n.val); n = n.next
    check(out, ['c', 'a'])
