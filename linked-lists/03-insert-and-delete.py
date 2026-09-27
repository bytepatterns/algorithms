"""
Insert and Delete: Rewire two links, and nothing else has to move.

Insertion and deletion are pure pointer surgery. Point the new node at
whatever came next, then point the predecessor at the new node. Deleting is
the mirror image: let the predecessor skip one link forward. No shifting, no
resizing.

Lesson 3 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/insert-and-delete

Run it:  python linked-lists/03-insert-and-delete.py
"""


class Node:
    def __init__(self, v): self.value, self.next = v, None

def insert_after(node, value):
    fresh = Node(value)
    fresh.next = node.next      # new node takes over the old link
    node.next = fresh           # predecessor now points at it

def delete_after(node):
    node.next = node.next.next  # unlink: skip straight over one node


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    head = Node(1); head.next = Node(3)
    insert_after(head, 2)           # 1 -> 2 -> 3
    delete_after(head)              # 1 -> 3, the 2 is unlinked
    check(head.next.value, 3)
