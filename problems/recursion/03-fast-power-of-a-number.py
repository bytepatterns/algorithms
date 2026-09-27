"""
Fast Power (medium) · patterns: recursion, divide-and-conquer

Raise a number to an integer exponent without multiplying it by itself that
many times. The exponent may be zero or negative, and a negative exponent
means one divided by the positive-exponent result. Return the value.

Examples:

    Input:  base = 2, exp = 10
    Output: 1024
    Why:    ten multiplications are not needed; four calls suffice

    Input:  base = 2, exp = -3
    Output: 0.125
    Why:    a negative exponent inverts the positive result

    Input:  base = 3, exp = 0
    Output: 1
    Why:    edge case, any base to the zero is one

Approach:
    Squaring halves the exponent, so each call cuts the work in two rather
    than shaving one off. The key detail is storing the recursive result in
    a variable and squaring it: calling twice would rebuild the same subtree
    and collapse the saving back to linear. An odd exponent leaves one base
    factor behind after the halving, which the last multiplication puts
    back. Negative exponents are handled once at the top by inverting the
    positive answer. Time is O(log exp) and the stack depth is the same.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/fast-power-of-a-number

Run it:  python problems/recursion/03-fast-power-of-a-number.py
"""


def power(base, exp):
    if exp == 0:
        return 1                              # anything to the zero
    if exp < 0:
        return 1 / power(base, -exp)          # a negative exponent flips it
    half = power(base, exp // 2)              # one call, reused twice
    return half * half * (base if exp % 2 else 1)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(power(2, 10), 1024)
    check(power(3, 0), 1)
    check(power(2, -3), 0.125)
