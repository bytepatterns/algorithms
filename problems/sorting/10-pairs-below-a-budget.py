"""
Pairs Below a Budget (easy) · patterns: sorting, two-pointers

A shop lists item prices, and a price can even be negative after a refund.
Count the pairs of two different items whose prices add up to strictly less
than a budget. Two items at different positions form a separate pair even if
their prices are equal.

Examples:

    Input:  prices = [4, -2, 0, 3, 1], budget = 3
    Output: 5
    Why:    (4, -2), (-2, 0), (-2, 3), (-2, 1) and (0, 1) all add up to less than 3

    Input:  prices = [2, 2, 2], budget = 5
    Output: 3
    Why:    each of the three ways to pick two of the 2s adds up to 4

    Input:  prices = [5], budget = 100
    Output: 0
    Why:    edge case, one item cannot form a pair

Approach:
    Sorting lets one comparison settle many pairs at once. When the smallest
    remaining price plus the largest remaining price is under the budget,
    every price between them also fits with the smallest one, so all of
    those pairs are counted and the smallest is retired. When the sum is too
    big, the largest price cannot fit with anything left and is retired
    instead. Each step retires one price, so the scan after sorting is
    linear. Time is O(n log n) for the sort, and space is O(n) for the
    sorted copy.

The lesson behind it: O(n²) and Nested Loops
    https://bytepatterns.com/learn/big-o/on2-and-nested-loops
    python big-o/03-on2-and-nested-loops.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/pairs-below-a-budget

Run it:  python problems/sorting/10-pairs-below-a-budget.py
"""


def pairs_below(prices, budget):
    p = sorted(prices)
    left, right, count = 0, len(p) - 1, 0
    while left < right:
        if p[left] + p[right] < budget:
            count += right - left       # p[left] fits with every price up to right
            left += 1
        else:
            right -= 1                  # p[right] fits with nothing left
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(pairs_below([4, -2, 0, 3, 1], 3), 5)
    check(pairs_below([2, 2, 2], 5), 3)
    check(pairs_below([5], 100), 0)
