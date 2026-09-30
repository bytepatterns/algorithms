"""
Count Pairs With a Given Gap (easy) · patterns: hash-map, complement-lookup

A pricing team wants to know how many distinct price pairs in a list differ
by exactly k. Given a list of integers nums and an integer k ≥ 0, return the
number of distinct value pairs (a, b) with a ≤ b, both present in the list,
and b - a = k. A pair with k = 0 needs the value to appear at least twice.
The list has up to 10,000 values, so compare against a lookup table rather
than every other value.

Examples:

    Input:  nums = [3, 1, 4, 1, 5], k = 2
    Output: 2
    Why:    (1, 3) and (3, 5); the second 1 does not make a new pair

    Input:  nums = [1, 2, 3, 4, 5], k = 1
    Output: 4

    Input:  nums = [1, 3, 1, 5, 4], k = 0
    Output: 1
    Why:    edge case, only 1 appears twice

Approach:
    Pairs are counted by distinct values, so the list is first reduced to a
    table of value counts. When k is positive, each distinct value a can
    only pair with a + k, and a single lookup in the table answers that, so
    counting the values whose partner exists counts every pair exactly once,
    from its smaller end. When k is 0 the partner is the value itself, so
    the pair exists exactly when that value appears at least twice. Building
    the table and scanning it are both linear, so time and space are O(n).

The lesson behind it: Two Sum
    https://bytepatterns.com/learn/hash-tables/two-sum
    python hash-tables/02-two-sum.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/count-pairs-with-a-given-gap

Run it:  python problems/hash-tables/12-count-pairs-with-a-given-gap.py
"""


from collections import Counter

def gap_pairs(nums, k):
    counts = Counter(nums)
    if k == 0:
        return sum(1 for c in counts.values() if c > 1)   # a value paired with itself
    return sum(1 for a in counts if a + k in counts)      # counted from the smaller end


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(gap_pairs([3, 1, 4, 1, 5], 2), 2)
    check(gap_pairs([1, 2, 3, 4, 5], 1), 4)
    check(gap_pairs([1, 3, 1, 5, 4], 0), 1)
