"""
Add Two Digit Chains (medium) · patterns: dummy-node, carry-propagation

Two non-negative whole numbers are stored as linked lists of single digits,
with the least significant digit at the head. Add the two numbers and return
the sum in the same format. The two lists may have different lengths, and
neither carries a leading zero, meaning the last node is never a zero unless
the number is zero itself.

Examples:

    Input:  a = 2 -> 4 -> 3, b = 5 -> 6 -> 4
    Output: 7 -> 0 -> 8
    Why:    342 plus 465 is 807, still written back to front

    Input:  a = 9 -> 9, b = 1
    Output: 0 -> 0 -> 1
    Why:    edge case, the carry runs off the end and adds a digit

    Input:  a = 0, b = 0
    Output: 0
    Why:    the sum of two zeros is a single zero digit

Approach:
    Digits arrive least significant first, so a single forward pass adds
    column by column exactly like long addition on paper. The loop condition
    includes a pending carry, which is what grows the result by one digit
    when the final column overflows. A throwaway starter node means
    appending never has to special-case the empty result, and using divmod
    keeps the digit and the next carry together. Time is O(max of the two
    lengths), and space is O(1) beyond the returned list.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/linked-lists/add-two-digit-chains

Run it:  python problems/linked-lists/05-add-two-digit-chains.py
"""


class Node:
    def __init__(self, val, nxt=None): self.val, self.next = val, nxt
def build(v): return Node(v[0], build(v[1:])) if v else None   # list -> chain
def dump(h): return [h.val] + dump(h.next) if h else []        # chain -> list
def add_digit_chains(a, b):
    dummy = tail = Node(0)           # starter node removes the empty-result case
    carry = 0
    while a or b or carry:           # a pending carry still owes a digit
        total = carry
        if a: total, a = total + a.val, a.next
        if b: total, b = total + b.val, b.next
        carry, digit = divmod(total, 10)
        tail.next = Node(digit)
        tail = tail.next
    return dummy.next


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(dump(add_digit_chains(build([2, 4, 3]), build([5, 6, 4]))), [7, 0, 8])
    check(dump(add_digit_chains(build([9, 9]), build([1]))), [0, 0, 1])
    check(dump(add_digit_chains(build([0]), build([0]))), [0])
