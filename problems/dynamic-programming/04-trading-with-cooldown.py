"""
Trading With Cooldown (hard) · patterns: state-machine-dp, rolling-variables

You are given daily prices for one stock and may trade as often as you like,
but you can hold at most one share at a time. After any sale you must sit
out the following day entirely, so the earliest possible next purchase is
two days later. Return the maximum total profit achievable, which is 0 when
no trade is worth making.

Examples:

    Input:  prices = [1, 2, 3, 0, 2]
    Output: 3
    Why:    buy at 1, sell at 2, rest a day, buy at 0, sell at 2

    Input:  prices = [5, 4, 3]
    Output: 0
    Why:    every trade would lose money, so no trade is made

    Input:  prices = []
    Output: 0
    Why:    edge case, there are no days to trade on

Approach:
    Each day is described by three balances: the best result while holding a
    share, the best result on a day a sale happens, and the best result
    while free to buy. The cooldown is captured by letting the free balance
    absorb yesterday just-sold balance, so buying can only follow a rest
    day. All three are computed from yesterday values simultaneously, which
    keeps a single pass with three variables instead of a table. Time is
    O(n) and space is O(1).

The lesson behind it: DP as a State Machine
    https://bytepatterns.com/learn/dynamic-programming/stock-state-machine
    python dynamic-programming/20-stock-state-machine.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/trading-with-cooldown

Run it:  python problems/dynamic-programming/04-trading-with-cooldown.py
"""


def max_profit_with_cooldown(prices):
    if not prices: return 0
    hold = -prices[0]                # best balance while holding a share
    sold = 0                         # best balance on a day a sale happens
    free = 0                         # best balance while free to buy
    for p in prices[1:]:
        # buying is only allowed out of free, which lags a day behind a sale
        hold, sold, free = max(hold, free - p), hold + p, max(free, sold)
    return max(sold, free)           # never finish holding a share


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_profit_with_cooldown([1, 2, 3, 0, 2]), 3)
    check(max_profit_with_cooldown([5, 4, 3]), 0)
    check(max_profit_with_cooldown([]), 0)
