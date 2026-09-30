"""
Longest Chain of Pairs (medium) · patterns: greedy, sort-by-end, interval-scheduling

You are given a list of pairs [a, b] with a < b. A pair [c, d] can follow a
pair [a, b] in a chain when b < c. Pairs may be used in any order, each at
most once. Return the length of the longest chain you can build.

Examples:

    Input:  pairs = [[1, 2], [2, 3], [3, 4]]
    Output: 2
    Why:    [1, 2] then [3, 4]; [2, 3] cannot follow [1, 2] because 2 is not less than 2

    Input:  pairs = [[5, 24], [15, 25], [27, 40], [50, 60]]
    Output: 3
    Why:    [5, 24], [27, 40], [50, 60]

    Input:  pairs = [[1, 2], [7, 8], [4, 5]]
    Output: 3
    Why:    edge case, the input order does not matter, so all three chain

Approach:
    This is interval scheduling with a strict gap. Among all pairs, the one
    that ends earliest is a safe first link: any longest chain can swap its
    first pair for that one, because ending earlier never blocks a pair that
    could follow. After taking it, the same argument applies to the pairs
    that start after its end, so a single pass in order of end value builds
    a longest chain. The comparison is strict, start > last_end, because a
    pair must start after the previous one ends, not on the same number.
    Sorting dominates, so time is O(n log n) and space is O(n) for the
    sorted copy.

The lesson behind it: Interval Scheduling
    https://bytepatterns.com/learn/greedy/interval-scheduling
    python greedy/02-interval-scheduling.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/longest-chain-of-pairs

Run it:  python problems/greedy/12-longest-chain-of-pairs.py
"""


def longest_chain(pairs):
    count, last_end = 0, float("-inf")
    for start, end in sorted(pairs, key=lambda p: p[1]):   # earliest end first
        if start > last_end:            # strictly after the chain's current end
            count += 1
            last_end = end
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_chain([[1, 2], [2, 3], [3, 4]]), 2)
    check(longest_chain([[5, 24], [15, 25], [27, 40], [50, 60]]), 3)
    check(longest_chain([[1, 2], [7, 8], [4, 5]]), 3)
