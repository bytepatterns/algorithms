"""
Subarray Sums With a Map: The complement trick, moved onto running totals.

Two Sum asks a map for the complement of a value. Do the same with running
totals. A subarray ending here sums to k exactly when some earlier prefix
total equals running - k. So carry the running total, ask the map how many
times that complement has already been seen, add it to the answer, and
record the current total for the positions still to come. One pass, and
negative numbers do not bother it.

Lesson 6 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/subarray-sum-map

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python hash-tables/06-subarray-sum-map.py
"""


def count_subarrays(nums, k):
    seen = {0: 1}          # the empty prefix counts once
    total = running = 0
    for x in nums:
        running += x
        total += seen.get(running - k, 0)      # prefixes that close a k-sum
        seen[running] = seen.get(running, 0) + 1
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_subarrays([1, 2, 3, -2, 2], 3), 4)
