"""
Longest Window Within Budget (medium) · patterns: sliding-window, two-pointers

Each day of a trip has a cost, and neither the costs nor the budget are ever
negative. Given the list of daily costs and the budget, return the length of
the longest run of consecutive days whose costs add up to at most the
budget. If every single day is over budget on its own, return 0.

Examples:

    Input:  costs = [4, 1, 1, 3, 2, 6], budget = 6
    Output: 3
    Why:    days 1-3 cost 1 + 1 + 3 = 5, and no run of four days fits

    Input:  costs = [0, 0, 2, 0], budget = 0
    Output: 2
    Why:    the two free days at the start are the longest run that costs nothing

    Input:  costs = [9, 8], budget = 5
    Output: 0
    Why:    edge case, every single day is already over budget

Approach:
    Re-adding every run is O(n³) and extending a running sum from each start
    is O(n²). Because costs are never negative, the best start for each end
    only moves forward, so a sliding window visits every day at most twice:
    once when the right edge adds it and once when the left edge drops it.
    After shrinking, the window is the longest valid run ending at the
    current day, and the best of those is the answer. Time is O(n), and
    space is O(1).

The lesson behind it: Comparing Complexities
    https://bytepatterns.com/learn/big-o/comparing-complexities
    python big-o/05-comparing-complexities.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/longest-window-within-budget

Run it:  python problems/arrays/16-longest-window-within-budget.py
"""


def longest_within(costs, budget):
    left = total = best = 0
    for right, cost in enumerate(costs):
        total += cost
        while total > budget:           # shrink until the window fits again
            total -= costs[left]
            left += 1
        best = max(best, right - left + 1)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_within([4, 1, 1, 3, 2, 6], 6), 3)
    check(longest_within([0, 0, 2, 0], 0), 2)
    check(longest_within([9, 8], 5), 0)
