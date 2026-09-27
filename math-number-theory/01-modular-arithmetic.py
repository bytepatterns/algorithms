"""
Modular Arithmetic: A remainder is a position on a clock, not a leftover.

A clock has twelve positions. Step past 11 and you are back at 0, so 45 and
9 land in the same place.

That is all % does: it reports where you stopped, never how many laps you
ran. Add, subtract or multiply first, or reduce first — the position is the
same.

Lesson 1 of Math & Number Theory, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/math-number-theory/modular-arithmetic

Run it:  python math-number-theory/01-modular-arithmetic.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    m = 12
    check((45 + 31) % m, 4)  # six laps and four
    check(((45 % m) + (31 % m)) % m, 4)  # reduce first, same landing
    check((9 * 7) % m, 3)  # multiplication survives too
    check(-3 % m, 9)  # Python never answers negative
