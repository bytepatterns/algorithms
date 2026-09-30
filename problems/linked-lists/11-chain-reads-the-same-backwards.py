"""
Chain Reads the Same Backwards (easy) · patterns: fast-slow-pointers, in-place-reversal

Given the head of a singly linked list of digits, return True if the values
read the same from front to back as from back to front. The list has between
1 and 100,000 nodes. Aim for O(n) time and O(1) extra memory, which rules
out copying the values into a Python list, and leave the list in its
original shape when you are done.

Examples:

    Input:  1 -> 2 -> 2 -> 1
    Output: True

    Input:  1 -> 2
    Output: False

    Input:  7
    Output: True
    Why:    edge case, a single node is a palindrome

Approach:
    A palindrome check compares the i-th value from the front with the i-th
    value from the back, and the only obstacle is that the back of a singly
    linked list cannot be walked in reverse. Fast and slow pointers find the
    middle in one pass: when the fast pointer runs out, the slow one stands
    at the first node of the back half (the middle node itself, for an odd
    length). Reversing the list from there makes the back half readable from
    the last node inward, so two pointers can compare it with the front
    half. The comparison stops when the reversed half runs out, which also
    ignores a lone middle node. Reversing that half a second time puts every
    link back. Time is O(n) and extra space is O(1).

The lesson behind it: Fast and Slow Pointers
    https://bytepatterns.com/learn/linked-lists/fast-and-slow-pointers
    python linked-lists/05-fast-and-slow-pointers.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/chain-reads-the-same-backwards

Run it:  python problems/linked-lists/11-chain-reads-the-same-backwards.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list

def reverse(node):
    prev = None
    while node:
        node.next, prev, node = prev, node, node.next
    return prev

def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:                 # slow ends at the back half
        slow, fast = slow.next, fast.next.next
    tail = reverse(slow)
    left, right, same = head, tail, True
    while right:
        if left.val != right.val:
            same = False
            break
        left, right = left.next, right.next
    reverse(tail)                             # restore the original links
    return same


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    check(is_palindrome(build([1, 2, 2, 1])), True)
    check(is_palindrome(build([1, 2])), False)
    check(is_palindrome(build([7])), True)
    chain = build([1, 2, 3, 2, 1])
    check_printed(is_palindrome(chain), dump(chain), expect="True [1, 2, 3, 2, 1]")
