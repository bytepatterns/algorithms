"""
Smallest Start for a Positive Walk (easy) · patterns: running-sum, prefix-minimum

You pick a positive whole number as a starting value, then add the numbers
of a list to it one at a time, from left to right. Return the smallest
starting value for which the running total never drops below 1 at any step.

Examples:

    Input:  nums = [-3, 2, -3, 4, 2]
    Output: 5
    Why:    5 goes to 2, 4, 1, 5, 7, while 4 would reach 0 after the third step

    Input:  nums = [1, 2]
    Output: 1
    Why:    the total only grows, so the smallest positive start works

    Input:  nums = [1, -2, -3]
    Output: 5
    Why:    edge case, the lowest point comes at the very end

Approach:
    This is the fuel tank from the gas station lesson: the running sum is
    the tank, and a start value is fuel you bring along. Adding a start
    value s lifts every running total by exactly s, so the walk stays at 1
    or above precisely when s plus the lowest running total is at least 1.
    One pass finds that lowest total. Starting the minimum at 0 covers lists
    whose running sum never goes negative, where the answer is the smallest
    positive start, 1. Time is O(n) and space is O(1).

The lesson behind it: Gas Station
    https://bytepatterns.com/learn/greedy/gas-station
    python greedy/04-gas-station.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/smallest-start-for-a-positive-walk

Run it:  python problems/greedy/11-smallest-start-for-a-positive-walk.py
"""


def smallest_start(nums):
    total = lowest = 0
    for x in nums:
        total += x
        lowest = min(lowest, total)     # the deepest dip of the running sum
    return 1 - lowest                   # lowest <= 0, so this is at least 1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(smallest_start([-3, 2, -3, 4, 2]), 5)
    check(smallest_start([1, 2]), 1)
    check(smallest_start([1, -2, -3]), 5)
