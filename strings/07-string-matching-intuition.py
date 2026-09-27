"""
String Matching Intuition: A mismatch already tells you where to restart.

Naive matching throws away everything it just learned: after four matching
characters it slides the pattern one step and re-reads them all.

Precompute, for every prefix of the pattern, the longest proper prefix that
is also a suffix. On a mismatch, fall back to that length — the text pointer
never moves backwards.

Lesson 7 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/string-matching-intuition

Run it:  python strings/07-string-matching-intuition.py
"""


def failure(pat):
    table = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k and pat[i] != pat[k]:   # fall back to a shorter prefix
            k = table[k - 1]
        if pat[i] == pat[k]:
            k += 1
        table[i] = k                    # prefix that is also a suffix
    return table


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(failure("ababc"), [0, 0, 1, 2, 0])
    check(failure("aaaa"), [0, 1, 2, 3])
