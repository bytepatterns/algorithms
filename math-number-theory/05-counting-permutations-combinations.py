"""
Permutations vs Combinations: Divide by k! the moment order stops mattering.

Three podium places, five runners: five choices, then four, then three. That
is 60 ordered line-ups — a permutation, n! / (n - k)!.

If only the group matters, each trio has been counted 3! times, once per
ordering. Divide that away and 60 becomes 10. Pascal's triangle stores the
same counts: every entry is the two above it, because the newest runner is
either in or out.

Lesson 5 of Math & Number Theory, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/math-number-theory/counting-permutations-combinations

Run it:  python math-number-theory/05-counting-permutations-combinations.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from math import comb, factorial, perm

    check(perm(5, 3), 60)  # ordered podiums
    check(factorial(5) // factorial(2), 60)  # the same n! / (n-k)!
    check(comb(5, 3), 10)  # order thrown away
    check(perm(5, 3) // factorial(3), 10)  # divided by k! by hand
    check(comb(5, 3) == comb(5, 2), True)  # pick who is left out instead
