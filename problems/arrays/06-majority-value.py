"""
Majority Value (easy) · patterns: counting, single-pass

One value in a list occupies more than half of all positions. Return that
value. You may assume such a value always exists, so you never have to
report failure, and the list is never empty.

Examples:

    Input:  nums = [3, 3, 4]
    Output: 3
    Why:    3 fills two of the three slots, which is more than half

    Input:  nums = [2, 2, 1, 1, 2]
    Output: 2
    Why:    the majority value is not required to sit together

    Input:  nums = [9]
    Output: 9
    Why:    edge case, the only value trivially owns more than half the list

Approach:
    Pairing each majority occurrence against one non-majority occurrence
    cancels both, and since the majority owns more than half the slots it
    cannot be fully cancelled. A single candidate plus a lead counter
    simulates that pairing without storing anything else: the lead hitting
    zero means the previous candidate has been fully matched, so the next
    element starts a fresh round. Time is O(n) with one pass, and space is
    O(1).

The lesson behind it: Majority Element
    https://bytepatterns.com/learn/arrays/majority-element
    python arrays/14-majority-element.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/majority-value

Run it:  python problems/arrays/06-majority-value.py
"""


def majority_value(nums):
    candidate = None
    lead = 0                         # how far the candidate is ahead
    for x in nums:
        if lead == 0:                # the previous candidate was fully cancelled
            candidate = x
        lead += 1 if x == candidate else -1
    return candidate


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(majority_value([3, 3, 4]), 3)
    check(majority_value([2, 2, 1, 1, 2]), 2)
    check(majority_value([9]), 9)
