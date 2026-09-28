"""
Fewest Coins for an Amount (medium) · patterns: bottom-up-dp, unbounded-knapsack

A machine pays out change using coin values from a given list, and it has an
unlimited supply of every value. Return the smallest number of coins that
add up to exactly amount, or -1 if no combination of coins reaches it. Coin
values are positive and distinct, and an amount of 0 needs no coins at all.

Examples:

    Input:  coins = [1, 4, 6], amount = 8
    Output: 2
    Why:    4 + 4; grabbing the 6 first leads to 6 + 1 + 1, three coins

    Input:  coins = [5, 10], amount = 3
    Output: -1
    Why:    every coin is bigger than the amount

    Input:  coins = [2], amount = 0
    Output: 0
    Why:    edge case, nothing to pay

Approach:
    Removing the last coin from an optimal payout leaves an optimal payout
    for a smaller amount, so the best count for amount a is one plus the
    best count for a minus some coin. Filling a table from 0 upward
    guarantees those smaller answers are ready when needed. Amounts that no
    coin mix can reach keep the sentinel amount + 1, which is more coins
    than any real answer could use, and that becomes -1 at the end. Time is
    O(amount times number of coins), and space is O(amount).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/fewest-coins-for-amount

Run it:  python problems/dynamic-programming/10-fewest-coins-for-amount.py
"""


def fewest_coins(coins, amount):
    NONE = amount + 1                        # more coins than any real answer needs
    best = [0] + [NONE] * amount             # best[a] = fewest coins that make a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]:
                best[a] = best[a - c] + 1    # pay c last, the rest optimally
    return best[amount] if best[amount] < NONE else -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_coins([1, 4, 6], 8), 2)
    check(fewest_coins([5, 10], 3), -1)
    check(fewest_coins([2], 0), 0)
