"""
Detect a Cycle: If the list loops, the fast pointer laps the slow one.

Run the same one-hop and two-hop pointers. On a straight list, fast falls
off the end. Inside a loop it can never fall off, and since it closes the
gap by one node per step, it must eventually land on slow. Meeting means a
cycle.

Lesson 6 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/detect-cycle

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python linked-lists/06-detect-cycle.py
"""


class Node:
    def __init__(self, v): self.value, self.next = v, None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # one step
        fast = fast.next.next     # two steps
        if slow is fast:          # fast lapped slow
            return True
    return False                  # ran off the end: no loop


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c; c.next = b   # 3 links back to 2
    check(has_cycle(a), True)
