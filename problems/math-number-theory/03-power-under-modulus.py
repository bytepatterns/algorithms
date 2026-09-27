"""
Power Under A Modulus (medium) · patterns: fast-exponentiation, modular-arithmetic

Compute base raised to exp, reported modulo mod, where the exponent can
reach a billion. Building the power first and reducing afterwards would
produce a number with hundreds of millions of digits, so the reduction has
to happen along the way.

Examples:

    Input:  base = 2, exp = 10, mod = 1000
    Output: 24
    Why:    1024 % 1000

    Input:  base = 7, exp = 1000000, mod = 13
    Output: 9

    Input:  base = 5, exp = 3, mod = 1
    Output: 0
    Why:    edge case, everything is congruent to 0 modulo 1

Approach:
    Reading the exponent in binary turns it into a sum of powers of two, and
    each of those powers is one squaring away from the last. So the running
    base climbs the ladder, and the answer picks up the rungs whose binary
    digit is set. Because a remainder survives multiplication, reducing
    after every step keeps every intermediate value below the square of the
    modulus without changing the result. Time is O(log exp), and space is
    O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/power-under-modulus

Run it:  python problems/math-number-theory/03-power-under-modulus.py
"""


def mod_power(base, exp, mod):
    if mod == 1:
        return 0                        # every value is congruent to 0
    result, base = 1, base % mod
    while exp:
        if exp & 1:                     # this binary digit is set
            result = result * base % mod
        base = base * base % mod        # climb: b, b², b⁴, b⁸ ...
        exp >>= 1
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(mod_power(2, 10, 1000), 24)
    check(mod_power(7, 1000000, 13), 9)
    check(mod_power(5, 3, 1), 0)
    check(mod_power(3, 0, 7), 1)
