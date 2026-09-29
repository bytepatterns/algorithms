"""
Cheapest Stair Climb (easy) · patterns: bottom-up-dp, rolling-variables

A staircase charges a toll for stepping on each stair, given as a list where
position i holds the toll for stair i. From any stair you may move up one or
two stairs, and you may begin from either stair 0 or stair 1 without paying
to arrive there. Return the cheapest total toll for reaching the floor just
past the last stair.

Examples:

    Input:  cost = [10, 15, 20]
    Output: 15
    Why:    start on stair 1, pay 15, then jump two stairs to the top

    Input:  cost = [1, 100, 1, 1, 100, 1]
    Output: 4
    Why:    stepping only on the cheap stairs costs four in total

    Input:  cost = [5, 3]
    Output: 3
    Why:    edge case, starting on the cheaper stair and jumping straight off

Approach:
    Reaching any position is only possible from one or two stairs below, so
    its cheapest cost is the smaller of those two costs plus the toll of the
    stair being left. Both starting stairs cost nothing to stand on, which
    seeds the recurrence. Because each step looks back at most two
    positions, two rolling variables replace the full table. Time is O(n)
    and space is O(1).

The lesson behind it: Climbing Stairs
    https://bytepatterns.com/learn/dynamic-programming/climbing-stairs
    python dynamic-programming/03-climbing-stairs.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/cheapest-stair-climb

Run it:  python problems/dynamic-programming/01-cheapest-stair-climb.py
"""


def cheapest_climb(cost):
    back2, back1 = 0, 0              # cheapest cost of the two positions behind
    for i in range(2, len(cost) + 1):
        # arrive from one stair below or two, paying that stair own toll
        current = min(back1 + cost[i - 1], back2 + cost[i - 2])
        back2, back1 = back1, current
    return back1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cheapest_climb([10, 15, 20]), 15)
    check(cheapest_climb([1, 100, 1, 1, 100, 1]), 4)
    check(cheapest_climb([5, 3]), 3)
