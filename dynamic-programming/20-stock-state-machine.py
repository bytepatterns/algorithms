"""
DP as a State Machine: Two running totals, one per state, updated day by day.

Some DP has no table at all — just a handful of states and the moves between
them. Here you are either holding a share or free of one. Each day, every
state takes the better of staying put or arriving from the other state. Both
are updated from yesterday's pair at once, which is why the assignment is
simultaneous.

Lesson 20 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/stock-state-machine

Run it:  python dynamic-programming/20-stock-state-machine.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    fee = 2

    hold, free = -prices[0], 0        # hold: own a share; free: own none
    for p in prices[1:]:
        hold, free = max(hold, free - p), max(free, hold + p - fee)
        # buy today or keep holding   |   sell today or stay in cash

    check(free, 3)  # buy at 1, sell at 6, minus the fee
