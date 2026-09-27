"""
Traversal and Search: One node at a time is the only way through.

Traversal means parking a pointer on the head and reassigning it to
current.next until it falls off the end. Searching is traversal with a
comparison inside. Both are O(n), and neither can skip ahead.

Lesson 2 of Linked Lists, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/linked-lists/traversal-and-search

Run it:  python linked-lists/02-traversal-and-search.py
"""


class Node:
    def __init__(self, v): self.value, self.next = v, None

def find(head, target):
    node, index = head, 0
    while node is not None:        # walk until the chain ends
        if node.value == target:
            return index
        node = node.next           # hop to the next node
        index += 1
    return -1                      # target is not in the list


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    head = Node(4); head.next = Node(8); head.next.next = Node(15)
    check(find(head, 15), 2)
    check(find(head, 9), -1)
