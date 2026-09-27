"""
Binary Search Variants: Don't just find it. Find the first one that qualifies.

Interview problems rarely want any match; they want the first or the last
one. So instead of returning on a hit, record it and keep shrinking toward
that side. What you get back is a boundary, not an arbitrary index.

Lesson 3 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/binary-search-variants

Run it:  python searching/03-binary-search-variants.py
"""


def first_at_least(nums, target):
    lo, hi, answer = 0, len(nums) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            answer = mid      # a candidate...
            hi = mid - 1      # ...but look further left
        else:
            lo = mid + 1
    return answer


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(first_at_least([1, 3, 3, 3, 7], 3), 1)
