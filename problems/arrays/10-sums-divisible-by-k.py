"""
Subarray Sums Divisible by K (medium) · patterns: prefix-sums, hash-map, modular-arithmetic

A ledger holds daily balance changes, some of them negative. Given the list
nums and a positive whole number k, count the contiguous, non-empty
stretches of days whose total change is a multiple of k. A total of 0
counts, since 0 is a multiple of every k.

Examples:

    Input:  nums = [2, -2, 3, 1, 5], k = 3
    Output: 6
    Why:    [2, -2], [3], [2, -2, 3], [1, 5], [3, 1, 5] and the whole list

    Input:  nums = [1, 1], k = 5
    Output: 0
    Why:    the possible totals are 1, 1 and 2

    Input:  nums = [7], k = 7
    Output: 1
    Why:    edge case, a single day whose change is exactly k

Approach:
    With prefix totals, the stretch from day i to day j sums to the total
    after j minus the total before i. That difference is divisible by k
    exactly when both totals share a remainder mod k, so the answer is the
    number of pairs of prefix totals with equal remainders. A dictionary of
    remainder counts, seeded with the empty prefix, counts those pairs as
    the scan goes. Python's modulo returns a remainder between 0 and k minus
    1 even for negative totals, so negative changes need no special case.
    Time is O(n) and space is O(min(n, k)).

The lesson behind it: Prefix Sums
    https://bytepatterns.com/learn/arrays/prefix-sums
    python arrays/04-prefix-sums.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/sums-divisible-by-k

Run it:  python problems/arrays/10-sums-divisible-by-k.py
"""


def count_divisible(nums, k):
    seen = {0: 1}                    # the empty prefix, before any day
    total = count = 0
    for x in nums:
        total += x
        r = total % k                # never negative in Python when k > 0
        count += seen.get(r, 0)      # pair with every earlier equal remainder
        seen[r] = seen.get(r, 0) + 1
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_divisible([2, -2, 3, 1, 5], 3), 6)
    check(count_divisible([1, 1], 5), 0)
    check(count_divisible([7], 7), 1)
