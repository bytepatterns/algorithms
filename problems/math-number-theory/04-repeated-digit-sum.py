"""
Repeated Digit Sum (easy) · patterns: modular-arithmetic, math

Take a non-negative whole number and add up its decimal digits. If the
result has more than one digit, add up its digits again, and keep going
until a single digit remains. Return that digit, ideally without looping at
all.

Examples:

    Input:  n = 38
    Output: 2
    Why:    3 + 8 = 11, then 1 + 1 = 2

    Input:  n = 99999
    Output: 9
    Why:    the digits add to 45, and 4 + 5 = 9

    Input:  n = 0
    Output: 0
    Why:    edge case, zero is already one digit and the only number that ends at 0

Approach:
    Every power of ten is one more than a multiple of nine, so a number and
    the sum of its digits leave the same remainder modulo nine, and that
    remainder survives every round of the process. The final single digit is
    therefore the one digit from 1 to 9 with the same remainder as n, which
    is 1 plus (n minus 1) modulo 9, with zero as the only number that ends
    at 0. No loop is needed. Time and space are O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/repeated-digit-sum

Run it:  python problems/math-number-theory/04-repeated-digit-sum.py
"""


def digit_root(n):
    if n == 0:
        return 0                     # the only number whose digits sum to 0
    return 1 + (n - 1) % 9           # digit sums preserve the remainder mod 9


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(digit_root(38), 2)
    check(digit_root(99999), 9)
    check(digit_root(0), 0)
    check(digit_root(9), 9)
