"""
Where Two Chains Merge (easy) · patterns: two-pointers, list-traversal

Two version histories are stored as singly linked lists that may join at a
shared commit and run together from there to the end. Given the heads of
both lists, return the first node they share, or None if they never meet.
Shared means the same node object, not just an equal value. Do not change
either list, and use only O(1) extra space. Each list has up to 30,000
nodes.

Examples:

    Input:  a = 4 -> 1 -> 8 -> 4 -> 5, b = 5 -> 6 -> 1 -> 8 -> 4 -> 5,
            both lists share the nodes 8 -> 4 -> 5
    Output: the node holding 8
    Why:    the 1 before it is a different node in each list, only the value matches

    Input:  a = 2 -> 6 -> 4, b = 1 -> 5, no shared nodes
    Output: None

    Input:  a = 7, b = 7, where both heads are the same node
    Output: the node holding 7
    Why:    edge case, the lists share everything, so the answer is the head itself

Approach:
    Say list a has x nodes before the merge, list b has y, and the shared
    tail has z. A pointer that walks a and then switches to b covers x + z +
    y nodes before it reaches the merge node, and a pointer that walks b and
    then a covers y + z + x, the same distance, so they land on it in the
    same step. When the lists never meet, both pointers finish the combined
    length together and are both None at the same time, which also ends the
    loop. Each pointer takes at most a + b steps, so time is O(a + b), and
    extra space is O(1).

The lesson behind it: Traversal and Search
    https://bytepatterns.com/learn/linked-lists/traversal-and-search
    python linked-lists/02-traversal-and-search.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/where-two-chains-merge

Run it:  python problems/linked-lists/14-where-two-chains-merge.py
"""


class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def merge_point(a, b):
    p, q = a, b
    while p is not q:
        p = p.next if p else b          # switch to the other list at the end
        q = q.next if q else a
    return p                            # the shared node, or None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    shared = Node(8, Node(4, Node(5)))
    first_a = Node(4, Node(1, shared))
    first_b = Node(5, Node(6, Node(1, shared)))
    check(merge_point(first_a, first_b).val, 8)
    check(merge_point(Node(2, Node(6, Node(4))), Node(1, Node(5))), None)
    same = Node(7)
    check(merge_point(same, same).val, 7)
