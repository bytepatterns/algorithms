"""
Counting Sort: Skip comparisons entirely when the values are small.

If the values come from a small known range, count how many times each one
appears, then read the counts back out in order. That is O(n + k), faster
than any comparison sort, but only for that shape of data.

Lesson 7 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/counting-sort

Run it:  python sorting/07-counting-sort.py
"""


def counting_sort(nums, max_value):
    counts = [0] * (max_value + 1)
    for x in nums:
        counts[x] += 1              # tally each value
    out = []
    for value, times in enumerate(counts):
        out.extend([value] * times) # read the tallies in order
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(counting_sort([3, 1, 3, 0, 2], 3), [0, 1, 2, 3, 3])
