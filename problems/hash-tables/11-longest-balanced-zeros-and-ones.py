"""
Longest Balanced Zeros and Ones (medium) · patterns: prefix-sum, first-seen-index

A log records each request as 1 for success and 0 for failure. Find the
longest contiguous stretch of the log with exactly as many successes as
failures, and return its length, or 0 if there is none. The log holds
between 1 and 100,000 entries, so checking every stretch is too slow.

Examples:

    Input:  bits = [0, 1, 0]
    Output: 2
    Why:    [0, 1] and [1, 0] are both balanced; all three entries are not

    Input:  bits = [0, 0, 1, 0, 0, 0, 1, 1]
    Output: 6
    Why:    the last six entries hold three of each

    Input:  bits = [1, 1, 1]
    Output: 0
    Why:    edge case, no stretch is balanced

Approach:
    Rewriting failures as -1 turns "equal counts" into "sum is zero", and a
    stretch sums to zero exactly when the running balance is the same at
    both of its ends. So the task becomes finding two equal balances as far
    apart as possible. A dictionary remembers the first index at which each
    balance appeared, seeded with balance 0 at index -1 so that balanced
    prefixes count too, and each later sighting of that balance is a
    candidate stretch. Later sightings are never stored, since the earliest
    one always gives the longer stretch. Time and space are both O(n).

The lesson behind it: Subarray Sums With a Map
    https://bytepatterns.com/learn/hash-tables/subarray-sum-map
    python hash-tables/06-subarray-sum-map.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/longest-balanced-zeros-and-ones

Run it:  python problems/hash-tables/11-longest-balanced-zeros-and-ones.py
"""


def longest_balanced(bits):
    first = {0: -1}                 # balance 0 before the first entry
    balance = best = 0
    for i, bit in enumerate(bits):
        balance += 1 if bit else -1
        if balance in first:
            best = max(best, i - first[balance])
        else:
            first[balance] = i      # keep only the earliest index
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_balanced([0, 1, 0]), 2)
    check(longest_balanced([0, 0, 1, 0, 0, 0, 1, 1]), 6)
    check(longest_balanced([1, 1, 1]), 0)
