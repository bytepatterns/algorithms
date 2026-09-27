"""
GCD and Euclid: Replace the pair with the leftover and it shrinks fast.

The greatest common divisor is the longest ruler that measures both numbers
exactly.

Lay the shorter length along the longer one. Whatever sticks out must also
be measurable by that ruler, so gcd(a, b) becomes gcd(b, a % b). The pair
collapses within a handful of divisions, and a remainder of zero names the
answer.

Lesson 2 of Math & Number Theory, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/math-number-theory/gcd-and-euclid

Run it:  python math-number-theory/02-gcd-and-euclid.py
"""


def gcd(a, b):
    while b:                 # stop when nothing is left over
        a, b = b, a % b      # the leftover becomes the next divisor
    return a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(gcd(48, 18), 6)
    check(gcd(18, 48), 6)  # the first pass just swaps them
    check(gcd(13, 7), 1)  # coprime, no shared ruler
    check(48 * 18 // gcd(48, 18), 144)  # lcm comes free
