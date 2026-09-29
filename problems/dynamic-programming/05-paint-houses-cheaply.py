"""
Paint Houses Cheaply (easy) · patterns: bottom-up-dp, rolling-variables

A row of houses must each be painted in one of three colours, and painting a
given house a given colour has its own price. Neighbouring houses may not
share a colour. Return the cheapest total price for painting the whole row.

Examples:

    Input:  costs = [[17, 2, 17],
                     [16, 16, 5],
                     [14, 3, 19]]
    Output: 10
    Why:    paint the houses in the second, third and second colour for 2 + 5 + 3

    Input:  costs = [[7, 6, 2]]
    Output: 2
    Why:    a single house simply takes its cheapest colour

    Input:  costs = []
    Output: 0
    Why:    edge case, an empty row costs nothing

Approach:
    The only thing the rest of the row cares about is the colour of the
    house just painted, so three running totals, one per colour, capture the
    whole history. Each house rebuilds those three from the previous three
    by adding its own price to the cheaper of the two conflicting options.
    Computing all three simultaneously matters, because using a freshly
    updated value would let a house borrow from itself. Time is O(n) and
    space is O(1), since only three numbers are kept.

The lesson behind it: What Is Dynamic Programming?
    https://bytepatterns.com/learn/dynamic-programming/what-is-dp
    python dynamic-programming/01-what-is-dp.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/paint-houses-cheaply

Run it:  python problems/dynamic-programming/05-paint-houses-cheaply.py
"""


def cheapest_painting(costs):
    first = second = third = 0       # cheapest total ending in each of the colours
    for a, b, c in costs:
        # each colour pays its own price plus the better of the other two histories
        first, second, third = (a + min(second, third),
                                b + min(first, third),
                                c + min(first, second))
    return min(first, second, third)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(cheapest_painting([[17, 2, 17], [16, 16, 5], [14, 3, 19]]), 10)
    check(cheapest_painting([[7, 6, 2]]), 2)
    check(cheapest_painting([]), 0)
