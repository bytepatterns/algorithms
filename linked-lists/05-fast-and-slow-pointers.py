"""
Fast and Slow Pointers: One hop versus two finds the middle in one pass.

Send two pointers from the head, one moving a node at a time and the other
two. The fast pointer runs out of list after n/2 steps of the slow one, so
wherever slow stands is the middle. One pass, O(1) space, no length counter.

Lesson 5 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/fast-and-slow-pointers

Run it:  python linked-lists/05-fast-and-slow-pointers.py
"""


class Node:
    def __init__(self, v): self.value, self.next = v, None

def middle(head):
    slow = fast = head
    while fast and fast.next:   # need two nodes left to jump
        slow = slow.next        # one hop
        fast = fast.next.next   # two hops
    return slow                 # fast hit the end, slow is halfway


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20); head.next.next = Node(30)
    head.next.next.next = Node(40); head.next.next.next.next = Node(50)
    check(middle(head).value, 30)
