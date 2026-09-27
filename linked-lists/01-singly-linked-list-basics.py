"""
Singly Linked List Basics: Each item carries the address of the next one.

A linked list stores each value in its own node, and every node keeps the
address of the next one. Nothing sits side by side in memory. You hold only
the head, and the chain ends at a node pointing to None.

Lesson 1 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/singly-linked-list-basics

Run it:  python linked-lists/01-singly-linked-list-basics.py
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None          # link to the next node


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(7)               # 3 -> 7 -> None

    check(head.value, 3)
    check(head.next.value, 7)
    check(head.next.next, None)  # marks the end
