"""
Non-Adjacent Harvest (easy) · patterns: bottom-up-dp, rolling-variables

A harvesting robot drives along a single row of plots, and each plot holds a
known yield. Its arm needs a rest after every pick, so it can never harvest
two plots that sit next to each other. Return the largest total yield the
robot can collect in one pass. Yields are whole numbers from 0 upward, and
the row may be empty.

Examples:

    Input:  yields = [2, 7, 9, 3, 1]
    Output: 12
    Why:    harvest plots 0, 2 and 4 for 2 + 9 + 1

    Input:  yields = [5, 1, 1, 5]
    Output: 10
    Why:    the two end plots are not neighbours, so both can be taken

    Input:  yields = []
    Output: 0
    Why:    edge case, an empty row yields nothing

Approach:
    At every plot the best total so far comes from one of two states: the
    previous plot was harvested, or it was not. Harvesting the current plot
    is only allowed from the skipped state, and skipping it keeps whichever
    state was better, so two variables replace a whole table. The answer is
    the better state after the last plot. Time is O(n) with one pass, and
    space is O(1).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/non-adjacent-harvest

Run it:  python problems/dynamic-programming/09-non-adjacent-harvest.py
"""


def best_harvest(yields):
    took, skipped = 0, 0          # best total if the last plot was harvested / left alone
    for y in yields:
        # harvesting now needs the previous plot skipped; skipping keeps the better state
        took, skipped = skipped + y, max(took, skipped)
    return max(took, skipped)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best_harvest([2, 7, 9, 3, 1]), 12)
    check(best_harvest([5, 1, 1, 5]), 10)
    check(best_harvest([]), 0)
