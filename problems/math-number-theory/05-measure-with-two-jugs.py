"""
Measure With Two Jugs (medium) · patterns: gcd, math

You have two unmarked jugs that hold at most a and b litres, both starting
empty, and an unlimited tap. A move fills a jug to the brim, empties a jug
completely, or pours one jug into the other until the first is empty or the
second is full. Decide whether the two jugs can end up holding exactly t
litres between them.

Examples:

    Input:  a = 3, b = 5, t = 4
    Output: True
    Why:    one route ends with 4 litres in the big jug and the small jug empty

    Input:  a = 2, b = 6, t = 5
    Output: False
    Why:    every move keeps the total even

    Input:  a = 4, b = 6, t = 0
    Output: True
    Why:    edge case, the jugs already hold zero litres before any move

Approach:
    Filling or emptying changes the total by a whole jug, and pouring leaves
    it unchanged, so every reachable total is an integer combination of a
    and b and hence a multiple of their greatest common divisor. Conversely,
    repeatedly filling one jug and pouring it into the other reaches every
    such multiple up to a plus b, which is the classic Bezout argument. So
    the whole question collapses to a capacity check and a divisibility
    check. Euclid's algorithm makes this O(log min(a, b)) time and O(1)
    space.

The lesson behind it: GCD and Euclid
    https://bytepatterns.com/learn/math-number-theory/gcd-and-euclid
    python math-number-theory/02-gcd-and-euclid.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/measure-with-two-jugs

Run it:  python problems/math-number-theory/05-measure-with-two-jugs.py
"""


from math import gcd

def can_measure(a, b, t):
    if t == 0:
        return True                 # the jugs start out empty
    if t > a + b:
        return False                # more than both jugs hold together
    return t % gcd(a, b) == 0       # reachable totals are multiples of the gcd


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_measure(3, 5, 4), True)
    check(can_measure(2, 6, 5), False)
    check(can_measure(4, 6, 0), True)
    check(can_measure(1, 2, 3), True)
