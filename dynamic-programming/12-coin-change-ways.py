"""
Counting Ways, Not Coins: Loop coins on the outside and each combination is counted once.

Counting ways is a different recurrence from finding the fewest coins. Each
coin is introduced once, and every amount asks how many combinations already
known can absorb it. Because a coin is never revisited after its pass, 1+2
and 2+1 are the same answer. Swap the loops and you count orderings instead.

Lesson 12 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/coin-change-ways

Run it:  python dynamic-programming/12-coin-change-ways.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    coins = [1, 2, 5]
    target = 5

    ways = [0] * (target + 1)
    ways[0] = 1                      # one way to pay nothing: take nothing
    for coin in coins:               # coins outside: every mix is counted once
        for a in range(coin, target + 1):
            ways[a] += ways[a - coin]

    check(ways, [1, 1, 2, 2, 3, 4])
    check(ways[target], 4)
