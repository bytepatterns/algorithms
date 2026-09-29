"""
Closest Two-Team Split (medium) · patterns: 0-1-knapsack, subset-sum

Players have skill ratings that are whole numbers, zero or more. Put every
player on exactly one of two teams, where a team may end up empty, so that
the two team totals are as close as possible. Return the smallest possible
difference between the totals.

Examples:

    Input:  ratings = [5, 8, 13, 2]
    Output: 2
    Why:    13 + 2 = 15 against 5 + 8 = 13; no split reaches 14 each

    Input:  ratings = [4, 9, 5]
    Output: 0
    Why:    9 against 4 + 5, a perfect split

    Input:  ratings = [7]
    Output: 7
    Why:    edge case, one player means one team gets everything

Approach:
    A split is decided by one team's total s, and the difference is total
    minus 2s, so the best split uses the reachable s closest to half the
    total without passing it. Which sums are reachable is the equal-split
    question with a different finish: each player either joins the first
    team or not, so the reachable set after a player is the old set plus the
    old set shifted by that rating. The set is kept as the bits of one
    Python integer, where bit s means sum s is reachable, so each player
    costs one shift and one bitwise or. Time is O(n times the total) bit
    operations, and space is O(total) bits.

The lesson behind it: Equal Split
    https://bytepatterns.com/learn/dynamic-programming/partition-equal-subset
    python dynamic-programming/13-partition-equal-subset.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/closest-two-team-split

Run it:  python problems/dynamic-programming/22-closest-two-team-split.py
"""


def closest_split(ratings):
    total = sum(ratings)
    reach = 1                                 # bit s set: some group sums to s
    for r in ratings:
        reach |= reach << r                   # this player joins the group, or not
    for s in range(total // 2, -1, -1):       # the best team total is at most half
        if reach >> s & 1:
            return total - 2 * s


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(closest_split([5, 8, 13, 2]), 2)
    check(closest_split([4, 9, 5]), 0)
    check(closest_split([7]), 7)
