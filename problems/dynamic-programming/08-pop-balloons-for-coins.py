"""
Pop Balloons For Coins (hard) · patterns: interval-dp, bottom-up-dp

A row of balloons each carries a number. Popping a balloon pays its number
multiplied by the numbers of the balloons currently to its left and right; a
missing neighbour counts as 1. The row closes up after every pop, so the
neighbours change as you go. Pop every balloon and return the largest total
payment possible.

Examples:

    Input:  values = [3, 1, 5, 8]
    Output: 167
    Why:    popping in the order 1, 5, 3, 8 pays 15 + 120 + 24 + 8

    Input:  values = [1, 5]
    Output: 10
    Why:    popping the 1 first pays 5, and the lone 5 then pays another 5

    Input:  values = []
    Output: 0
    Why:    edge case, there is nothing to pop

Approach:
    Choosing the first pop is unusable because it makes the two halves
    interact, while choosing the last pop inside a stretch fixes that
    balloon's neighbours to be the stretch's own walls, which never change.
    That turns the problem into intervals: for each pair of walls, the best
    total is the maximum over inner balloons of the two sub-stretch totals
    plus the payment of that final pop. Padding both ends with a value of
    one removes the missing-neighbour special case. Filling by increasing
    width guarantees sub-stretches are ready when needed. Time is O(n cubed)
    and space is O(n squared).

The lesson behind it: Interval DP
    https://bytepatterns.com/learn/dynamic-programming/matrix-chain-order
    python dynamic-programming/16-matrix-chain-order.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/pop-balloons-for-coins

Run it:  python problems/dynamic-programming/08-pop-balloons-for-coins.py
"""


def max_coins(values):
    pad = [1] + values + [1]         # imaginary balloons of value one at both ends
    n = len(pad)
    best = [[0] * n for _ in range(n)]
    for width in range(2, n):        # the distance between the two walls
        for left in range(n - width):
            right = left + width
            for last in range(left + 1, right):   # the balloon popped last in here
                gain = pad[left] * pad[last] * pad[right]
                best[left][right] = max(best[left][right],
                                        best[left][last] + gain + best[last][right])
    return best[0][n - 1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_coins([3, 1, 5, 8]), 167)
    check(max_coins([1, 5]), 10)
    check(max_coins([]), 0)
