"""
Single Stock Trade (easy) · patterns: single-pass, running-minimum

You are given a list of daily prices for one stock, where position i holds
the price on day i. You may buy on one day and sell on a strictly later day,
at most once. Return the largest profit that single trade can produce. If no
later day ever pays more than an earlier one, return 0 because the best move
is to skip trading.

Examples:

    Input:  prices = [8, 3, 6, 1, 9, 4]
    Output: 8
    Why:    buy on day 3 at 1, sell on day 4 at 9

    Input:  prices = [7, 5, 4, 2]
    Output: 0
    Why:    prices only fall, so every trade would lose money

    Input:  prices = [5]
    Output: 0
    Why:    edge case, a single day leaves no later day to sell on

Approach:
    Sweep the prices once while carrying the minimum price seen so far.
    Selling on the current day is worth today's price minus that minimum, so
    comparing that value against the best profit so far keeps the answer up
    to date. Updating the minimum after scoring the sale guarantees the buy
    day is always strictly earlier than the sell day. Time is O(n) with a
    single pass, and space is O(1) since only two numbers are stored.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/single-stock-trade

Run it:  python problems/arrays/01-single-stock-trade.py
"""


def max_trade_profit(prices):
    best = 0                        # best profit found so far
    cheapest = float("inf")         # lowest price seen up to today
    for p in prices:
        # a sale today is only worth as much as the cheapest earlier buy
        best = max(best, p - cheapest)
        cheapest = min(cheapest, p)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_trade_profit([8, 3, 6, 1, 9, 4]), 8)
    check(max_trade_profit([7, 5, 4, 2]), 0)
    check(max_trade_profit([5]), 0)
