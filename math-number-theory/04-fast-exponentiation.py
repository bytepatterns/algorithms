"""
Fast Exponentiation: Square your way up instead of multiplying n times.

Write the exponent in binary. 13 is 1101, so 313 is 38 3*4 * 31.

Each rung of the ladder is the square of the one below it, so reaching 38
costs three multiplications rather than seven. Keep the rungs whose digit is
1 and the whole power lands in about log n steps.

Lesson 4 of Math & Number Theory, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/math-number-theory/fast-exponentiation

Run it:  python math-number-theory/04-fast-exponentiation.py
"""


def power(base, exp, mod):
    result = 1
    while exp:                          # one pass per binary digit
        if exp & 1:                     # this digit is on -> keep the rung
            result = result * base % mod
        base = base * base % mod        # climb: b, b², b⁴, b⁸ …
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
    check(power(3, 13, 10 ** 9 + 7), 1594323)
    check(power(3, 13, 1000), 323)
    check(power(2, 1000, 1000), 376)  # last three digits of 2**1000
