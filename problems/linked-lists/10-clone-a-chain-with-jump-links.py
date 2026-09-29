"""
Clone a Chain With Jump Links (medium) · patterns: pointer-relinking, in-place

Each node of a singly linked chain has a value, a next link and a jump link,
which points at any node of the same chain, including itself, or at nothing.
Return the head of a deep copy: brand-new nodes with the same values, where
every next and jump points at the corresponding new node. The original chain
must look exactly as it did once you are done. Below, a chain is written as
a list of (value, index the jump points at).

Examples:

    Input:  chain = [(3, None), (8, 0), (5, 3), (1, 1)]
    Output: [(3, None), (8, 0), (5, 3), (1, 1)], built from new nodes only
    Why:    the copy of 5 jumps to the copy of 1, not to the original 1

    Input:  chain = [(4, 0)]
    Output: [(4, 0)]
    Why:    the copy's jump points at the copy itself

    Input:  chain = []
    Output: None
    Why:    edge case, an empty chain copies to an empty chain

Approach:
    Weaving each copy in right after its original turns the original node
    into a free lookup for its copy: the copy of any node x is simply
    x.next. With that, the copy's jump is the next node after the original's
    jump target. A final pass unweaves the two chains, restoring every
    original next link. Time is O(n), and extra space is O(1) apart from the
    new nodes.

The lesson behind it: Copy a List With Random Links
    https://bytepatterns.com/learn/linked-lists/copy-list-with-random-pointer
    python linked-lists/09-copy-list-with-random-pointer.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/clone-a-chain-with-jump-links

Run it:  python problems/linked-lists/10-clone-a-chain-with-jump-links.py
"""


class Node:
    def __init__(self, val): self.val, self.next, self.jump = val, None, None
def build(pairs):                            # (value, index of the jump target or None)
    nodes = [Node(v) for v, _ in pairs]
    for a, b in zip(nodes, nodes[1:]): a.next = b
    for node, (_, j) in zip(nodes, pairs): node.jump = None if j is None else nodes[j]
    return nodes[0] if nodes else None
def describe(head):
    nodes = []
    while head: nodes.append(head); head = head.next
    index = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, index[id(n.jump)] if n.jump else None) for n in nodes]
def clone(head):
    node = head
    while node:                              # 1. weave a copy in after each node
        copy = Node(node.val)
        copy.next, node.next = node.next, copy
        node = copy.next
    node = head
    while node:                              # 2. the copy of x is x.next
        node.next.jump = node.jump.next if node.jump else None
        node = node.next.next
    new_head, node = head.next if head else None, head
    while node:                              # 3. unweave the two chains
        copy = node.next
        node.next = copy.next
        copy.next = copy.next.next if copy.next else None
        node = node.next
    return new_head


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(describe(clone(build([(3, None), (8, 0), (5, 3), (1, 1)]))), [(3, None), (8, 0), (5, 3), (1, 1)])
    check(describe(clone(build([(4, 0)]))), [(4, 0)])
    check(clone(build([])), None)
