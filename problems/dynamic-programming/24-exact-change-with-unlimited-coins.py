"""
Exact Change With Unlimited Coins (easy) · patterns: unbounded-knapsack, bottom-up-dp

A vending machine holds an unlimited supply of coins in each denomination
listed in coins. Return True if it can pay back exactly amount, otherwise
False.

Examples:

    Input:  coins = [4, 7], amount = 15
    Output: True
    Why:    4 + 4 + 7 = 15

    Input:  coins = [4, 6], amount = 9
    Output: False
    Why:    every mix of 4s and 6s is even

    Input:  coins = [5], amount = 0
    Output: True
    Why:    edge case, paying zero needs no coins

Approach:
    This is the unbounded knapsack with a yes-or-no answer, the feasibility
    half of coin change. ok[a] says whether amount a can be paid, and a coin
    makes a payable when a - coin already was. The loop over amounts runs
    upward, so by the time it reaches a, the entry for a - coin may already
    include this same coin, which is exactly what an unlimited supply
    allows. Running it downward would turn this into the use-each-coin-once
    problem instead. Time is O(len(coins) · amount) and space is O(amount).

The lesson behind it: Coin Change
    https://bytepatterns.com/learn/dynamic-programming/coin-change
    python dynamic-programming/05-coin-change.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/exact-change-with-unlimited-coins

Run it:  python problems/dynamic-programming/24-exact-change-with-unlimited-coins.py
"""


def can_pay(coins, amount):
    ok = [False] * (amount + 1)
    ok[0] = True                              # zero needs no coins
    for coin in coins:
        for a in range(coin, amount + 1):     # upward: a coin may be reused
            if ok[a - coin]:
                ok[a] = True
    return ok[amount]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_pay([4, 7], 15), True)
    check(can_pay([4, 6], 9), False)
    check(can_pay([5], 0), True)
