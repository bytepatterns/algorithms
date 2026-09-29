"""
Remove Value Nodes (easy) · patterns: dummy-node, pointer-relinking

Given the head of a singly linked list and a target value, remove every node
holding that value and return the head of what remains. Nodes are unlinked
rather than copied into a new list, and the surviving nodes keep their
original order. The result may be empty.

Examples:

    Input:  head = 1 -> 2 -> 6 -> 3 -> 6, target = 6
    Output: 1 -> 2 -> 3

    Input:  head = 7 -> 7 -> 7, target = 7
    Output: empty
    Why:    edge case, every node matches and the list empties out

    Input:  head = empty, target = 1
    Output: empty
    Why:    edge case, there is nothing to remove

Approach:
    A throwaway node placed before the head gives every real node a
    predecessor, so deleting the first node uses exactly the same relink as
    deleting any other. The walker inspects its successor rather than
    itself, and after an unhook it deliberately stays where it is, because
    the node that slid into that slot has not been inspected yet. Moving on
    after an unhook is the classic bug here, since it skips consecutive
    matches. Time is O(n) and space is O(1).

The lesson behind it: Insert and Delete
    https://bytepatterns.com/learn/linked-lists/insert-and-delete
    python linked-lists/03-insert-and-delete.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/remove-value-nodes

Run it:  python problems/linked-lists/04-remove-value-nodes.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def remove_value(head, target):
    dummy = Node(0, head)            # lets head removal use the same relink
    node = dummy
    while node.next:
        if node.next.val == target:
            node.next = node.next.next   # unhook, and do not move on
        else:
            node = node.next
    return dummy.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(remove_value(build([1, 2, 6, 3, 6]), 6)), [1, 2, 3])
    check(dump(remove_value(build([7, 7, 7]), 7)), [])
    check(dump(remove_value(build([]), 1)), [])
