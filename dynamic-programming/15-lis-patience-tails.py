"""
LIS in O(n log n): Keep the smallest possible ending for a chain of each length.

The O(n²) version asks every element which earlier one it can extend. The
faster version keeps one array: the smallest value that can end an
increasing chain of each length. Each number either extends the array or
replaces the first entry that is not smaller, found by binary search. Length
comes out right; the array itself is not the subsequence.

Lesson 15 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/lis-patience-tails

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python dynamic-programming/15-lis-patience-tails.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from bisect import bisect_left

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    tails = []
    for n in nums:
        i = bisect_left(tails, n)    # first tail that is not smaller than n
        if i == len(tails):
            tails.append(n)          # n extends the longest chain so far
        else:
            tails[i] = n             # same length, smaller ending

    check(tails, [2, 3, 7, 18])  # a length, not the actual subsequence
    check(len(tails), 4)
