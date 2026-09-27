"""
Find the Cycle Start: Knowing a loop exists is half the job — now find its door.

Once slow and fast collide you know there is a loop, but not where it
begins. Here is the trick: move one walker back to the head and let both
step one node at a time. They meet exactly at the entry.

Why? The distance from the head to the entry equals the distance from the
meeting point back round to the entry. Both walkers cover the same gap.

Lesson 7 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/find-the-cycle-start

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python linked-lists/07-find-the-cycle-start.py
"""


class Node:
    def __init__(self, v): self.val, self.next = v, None

def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:                  # met somewhere inside the loop
            slow = head                   # restart one walker at the head
            while slow is not fast:       # both take single steps from here
                slow, fast = slow.next, fast.next
            return slow.val               # they meet again at the entry
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    n = [Node(i) for i in range(6)]
    for a, b in zip(n, n[1:]): a.next = b     # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    n[5].next = n[2]                          # ...and 5 links back to 2
    check(cycle_start(n[0]), 2)
