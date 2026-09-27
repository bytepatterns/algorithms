"""
Minimum Daily Capacity (medium) · patterns: binary-search-on-answer, greedy-check

A conveyor carries packages in the order they are listed, and every package
must ship within a given number of days. A day's load is a run of packages
taken from the front, and no day may exceed the belt's capacity. Find the
smallest capacity that still finishes on time.

Examples:

    Input:  weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
    Output: 15
    Why:    1-5, 6-7, 8, 9, 10 fills exactly five days

    Input:  weights = [3, 2, 2, 4, 1, 4], days = 3
    Output: 6

    Input:  weights = [5], days = 1
    Output: 5
    Why:    edge case, the capacity can never be below the heaviest package

Approach:
    The capacity itself is the search space, and it is bounded below by the
    heaviest package and above by shipping everything in one day.
    Feasibility is monotone in that range, which is what makes binary search
    legal: a working capacity means every larger one works too. For a fixed
    capacity the best packing is the greedy one, since the order is fixed
    and starting a new day early can never help. The check costs O(n) and
    the range halves each round, so time is O(n log(total weight)) and space
    is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/searching/minimum-daily-capacity

Run it:  python problems/searching/05-minimum-daily-capacity.py
"""


def least_capacity(weights, days):
    def days_needed(cap):
        used, load = 1, 0
        for w in weights:
            if load + w > cap:      # this one starts a fresh day
                used, load = used + 1, 0
            load += w
        return used
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(mid) <= days:
            hi = mid                # mid works, so nothing above it is needed
        else:
            lo = mid + 1
    return lo


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(least_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
    check(least_capacity([3, 2, 2, 4, 1, 4], 3), 6)
    check(least_capacity([5], 1), 5)
