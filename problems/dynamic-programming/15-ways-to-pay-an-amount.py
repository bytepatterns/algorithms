"""
Ways to Pay an Amount (medium) · patterns: unbounded-knapsack, bottom-up-dp

A vending machine accepts coins of a few distinct positive values, and it
has an unlimited supply of each. Given the coin values and an amount, return
how many different collections of coins add up to exactly that amount. The
order in which coins are inserted does not matter, so 2 + 3 and 3 + 2 are
the same collection, and an amount of 0 has exactly one collection: no
coins.

Examples:

    Input:  coins = [2, 3, 5], amount = 10
    Output: 4
    Why:    2+2+2+2+2, 2+2+3+3, 5+5 and 2+3+5

    Input:  coins = [4], amount = 6
    Output: 0
    Why:    no number of fours makes six

    Input:  coins = [3, 7], amount = 0
    Output: 1
    Why:    edge case, the empty collection pays nothing

Approach:
    Processing the coins in an outer loop means that when coin c is being
    added, the table already counts every collection that uses only earlier
    coins. Walking the amounts upward lets the same coin be used again,
    since ways[a - c] may already include copies of c. Because each
    collection is built by adding its coins in coin order, it is counted
    exactly once, and swapping the two loops would count orderings instead.
    Time is O(k × amount) for k coin values, and space is O(amount).

The lesson behind it: Counting Ways, Not Coins
    https://bytepatterns.com/learn/dynamic-programming/coin-change-ways
    python dynamic-programming/12-coin-change-ways.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/ways-to-pay-an-amount

Run it:  python problems/dynamic-programming/15-ways-to-pay-an-amount.py
"""


def count_ways(coins, amount):
    ways = [1] + [0] * amount        # one way to pay 0: no coins
    for c in coins:                  # each coin value gets exactly one pass
        for a in range(c, amount + 1):
            ways[a] += ways[a - c]   # collections that use at least one more c
    return ways[amount]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_ways([2, 3, 5], 10), 4)
    check(count_ways([4], 6), 0)
    check(count_ways([3, 7], 0), 1)
