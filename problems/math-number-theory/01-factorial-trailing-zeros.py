"""
Trailing Zeros Of A Factorial (easy) · patterns: factor-counting, math

Given a non-negative whole number n, report how many zeros sit at the end of
n factorial. The factorial itself is astronomically large for even modest n,
so computing it and then counting characters is not an option.

Examples:

    Input:  n = 5
    Output: 1
    Why:    120 ends in a single zero

    Input:  n = 30
    Output: 7

    Input:  n = 0
    Output: 0
    Why:    edge case, 0! is 1 and has no trailing zero

Approach:
    Every trailing zero comes from a factor of ten, and ten is a two times a
    five. Between one and n there are always more even numbers than
    multiples of five, so the fives run out first and the count of fives is
    the answer. Multiples of five contribute one each, multiples of
    twenty-five contribute a second, and so on up the powers, which is
    exactly what the loop adds up. Time is O(log n) because the power grows
    fivefold each round, and space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/factorial-trailing-zeros

Run it:  python problems/math-number-theory/01-factorial-trailing-zeros.py
"""


def trailing_zeros(n):
    zeros, power = 0, 5
    while power <= n:
        zeros += n // power   # every multiple of this power gives one more five
        power *= 5            # 5, 25, 125 ... each adds a spare five
    return zeros


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(trailing_zeros(5), 1)
    check(trailing_zeros(30), 7)
    check(trailing_zeros(0), 0)
    check(trailing_zeros(100), 24)
