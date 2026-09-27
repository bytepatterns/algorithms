"""
Majority Element: Cancel the votes in pairs and the majority survives.

If one value fills more than half the array, then pairing each of its copies
against a copy of anything else still leaves copies over. Boyer-Moore does
that cancelling in one pass: hold a candidate and a count, add one when the
value matches, subtract one when it does not, and adopt a new candidate
whenever the count hits zero. Only a true majority can survive every
cancellation.

Lesson 14 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/majority-element

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python arrays/14-majority-element.py
"""


def majority(nums):
    candidate, count = None, 0
    for x in nums:
        if count == 0:          # nobody is holding the floor
            candidate = x
        count += 1 if x == candidate else -1
    return candidate


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(majority([2, 2, 1, 3, 2, 2, 2]), 2)
