"""
Fair Candy Shares (hard) · patterns: greedy, two-pass

Children stand in a row and each has a score. Every child must get at least
one sweet, and a child whose score is higher than a direct neighbour's must
get more sweets than that neighbour. Equal scores place no demand either
way. Return the smallest total number of sweets that meets both rules.

Examples:

    Input:  scores = [1, 0, 2]
    Output: 5
    Why:    hand out 2, 1, 2

    Input:  scores = [1, 2, 2]
    Output: 4
    Why:    hand out 1, 2, 1; the last child only has to beat nobody

    Input:  scores = [7]
    Output: 1
    Why:    edge case, a lone child still needs one sweet

Approach:
    The left-to-right pass gives each child exactly the length of the rising
    run that ends at them, which is the least that satisfies every
    left-neighbour rule. The right-to-left pass computes the same for the
    right side, and taking the maximum of the two meets both rules at once;
    neither pass hands out a sweet that some rule does not force, so the
    total is minimal. The maximum is what stops the second pass from undoing
    the first. Time is O(n) over two sweeps and space is O(n) for the
    counts.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/fair-candy-shares

Run it:  python problems/greedy/06-fair-candy-shares.py
"""


def fewest_sweets(scores):
    n = len(scores)
    give = [1] * n                             # everyone gets at least one
    for i in range(1, n):                      # rules against the left neighbour
        if scores[i] > scores[i - 1]:
            give[i] = give[i - 1] + 1
    for i in range(n - 2, -1, -1):             # rules against the right neighbour
        if scores[i] > scores[i + 1]:
            give[i] = max(give[i], give[i + 1] + 1)   # keep the left rule intact
    return sum(give)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_sweets([1, 0, 2]), 5)
    check(fewest_sweets([1, 2, 2]), 4)
    check(fewest_sweets([7]), 1)
    check(fewest_sweets([1, 3, 4, 5, 2]), 11)
