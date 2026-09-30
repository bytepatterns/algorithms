"""
Add Two Numbers Without Plus (medium) · patterns: bitwise-add, carry-propagation, twos-complement

A tiny chip exposes only bitwise instructions: AND, OR, XOR and shifts.
Write the addition routine it needs: given two 32-bit signed integers a and
b, return a + b without using + or - on them. Both inputs and the sum lie
between -1,000 and 1,000, and the result must match ordinary 32-bit two's
complement addition, including for negative numbers.

Examples:

    Input:  a = 1, b = 2
    Output: 3

    Input:  a = -5, b = 3
    Output: -2

    Input:  a = -7, b = -8
    Output: -15
    Why:    edge case, both inputs are negative

Approach:
    Binary addition splits into two independent parts: XOR gives each
    column's digit ignoring carries, and AND shifted left by one gives the
    carries in the column they flow into. The true sum is those two numbers
    added together, so the loop repeats with them until no carry is left,
    and each round pushes every remaining carry at least one column to the
    left, so a 32-bit add finishes in at most 32 rounds. Python integers are
    unbounded, so every intermediate is masked to 32 bits, which reproduces
    the wraparound of a real register. At the end a value with bit 31 set is
    a negative number in two's complement, and ~(a ^ MASK) converts it back
    to Python's negative integer. Time and space are both O(1) for a fixed
    32-bit width.

The lesson behind it: Binary and Bitwise Ops
    https://bytepatterns.com/learn/bit-manipulation/binary-and-bitwise-ops
    python bit-manipulation/01-binary-and-bitwise-ops.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/bit-manipulation/add-two-numbers-without-plus

Run it:  python problems/bit-manipulation/11-add-two-numbers-without-plus.py
"""


MASK, MAX_INT = 0xFFFFFFFF, 0x7FFFFFFF

def add(a, b):
    while b & MASK:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK   # digits, then carries
    a &= MASK
    return a if a <= MAX_INT else ~(a ^ MASK)          # bit 31 set means negative


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(add(1, 2), 3)
    check(add(-5, 3), -2)
    check(add(-7, -8), -15)
    check(add(0, -4), -4)
