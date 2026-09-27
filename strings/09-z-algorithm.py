"""
Z-Algorithm Intuition: Reuse what an earlier match already proved.

z[i] is how many characters from position i match the start of the string.
Comparing every position from scratch is quadratic, so keep the rightmost
match found so far — the z-box. A position inside that box was already
compared once, at its mirror near the front, so its answer starts from the
mirror's value and only the part beyond the box is compared again. The box
only ever slides right.

Lesson 9 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/z-algorithm

Run it:  python strings/09-z-algorithm.py
"""


def z_array(s):
    z = [0] * len(s)
    lo = hi = 0                             # the live z-box
    for i in range(1, len(s)):
        if i < hi:
            z[i] = min(hi - i, z[i - lo])   # reuse the box's mirror
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1                       # extend past the box
        if i + z[i] > hi:
            lo, hi = i, i + z[i]            # a longer box: keep it
    return z


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(z_array("aabxaab"), [0, 1, 0, 0, 3, 1, 0])
