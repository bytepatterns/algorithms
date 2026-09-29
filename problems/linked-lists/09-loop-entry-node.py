"""
Where the Loop Begins (medium) · patterns: fast-slow-pointers, cycle-detection

You receive the head of a singly linked chain that may end in a loop, where
the last node links back to an earlier one. Return the first node of the
loop, the one you reach first when walking from the head, or None if the
chain has no loop. Use O(1) extra memory and do not change any links. In the
examples the chain is given by its values plus pos, the index the last node
links back to, or -1 for no loop, and the output shows the value of the
returned node.

Examples:

    Input:  values = [3, 2, 0, -4], pos = 1
    Output: 2
    Why:    the walk enters the loop at the node holding 2

    Input:  values = [1, 2], pos = 0
    Output: 1
    Why:    the whole chain is the loop, so it starts at the head

    Input:  values = [1], pos = -1
    Output: None
    Why:    edge case, no loop to enter

Approach:
    First the slow and fast pointers run until they meet inside the loop, or
    the fast one finds the end. Say the entry is a steps from the head and
    the meeting point is b steps past the entry: the fast pointer has walked
    twice as far as the slow one, which forces a to equal a whole number of
    laps minus b. So a pointer restarted at the head and a pointer left at
    the meeting point, both moving one step at a time, arrive at the entry
    together. Time is O(n) and space is O(1).

The lesson behind it: Find the Cycle Start
    https://bytepatterns.com/learn/linked-lists/find-the-cycle-start
    python linked-lists/07-find-the-cycle-start.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/loop-entry-node

Run it:  python problems/linked-lists/09-loop-entry-node.py
"""


class Node:
    def __init__(self, val): self.val, self.next = val, None
def build(values, pos):               # the tail links back to index pos, or nowhere if -1
    nodes = [Node(v) for v in values]
    for a, b in zip(nodes, nodes[1:]): a.next = b
    if nodes and pos >= 0: nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None
def loop_entry(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:                      # inside the loop; now find its door
            probe = head
            while probe is not slow:          # equal distances to the entry
                probe, slow = probe.next, slow.next
            return probe
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(loop_entry(build([3, 2, 0, -4], 1)).val, 2)
    check(loop_entry(build([1, 2], 0)).val, 1)
    check(loop_entry(build([1], -1)), None)
