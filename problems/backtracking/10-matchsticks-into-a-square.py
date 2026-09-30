"""
Matchsticks Into a Square (hard) · patterns: backtracking, pruning, k-way-partition

You have a set of matchsticks with integer lengths. Decide whether you can
use every stick exactly once, without breaking any, to form the outline of a
square. There are between 1 and 15 sticks and each length is between 1 and
10^8. Trying all 4^15 ways to assign sticks to sides is about a billion
cases, so the search must prune aggressively.

Examples:

    Input:  sticks = [1, 1, 2, 2, 2]
    Output: True
    Why:    the sides are 2, 2, 2 and 1 + 1

    Input:  sticks = [3, 3, 3, 3, 4]
    Output: False
    Why:    the total, 16, would need sides of 4, and the four 3s cannot reach 4 without breaking

    Input:  sticks = [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]
    Output: True
    Why:    every side is 5 + 4 + 3

Approach:
    The side length is fixed at the total divided by four, so the question
    is whether the sticks split into four groups with that sum. The search
    places one stick per level, trying every side that still has room, and
    backs out when the remaining sticks cannot be placed. Three prunes make
    it fast. The totals check and the longest-stick check reject impossible
    inputs before any search. Sorting from longest to shortest means big
    sticks, which have the fewest options, are placed first and conflicts
    are found early. And at each level, sides with the same current length
    are interchangeable, so each distinct length is tried only once, which
    removes the symmetric copies of every failed branch. When all sticks are
    placed every side is exactly full, since no side ever exceeds the side
    length and the sum is four side lengths. The worst case is still O(4^n),
    but the prunes cut the real search to a tiny fraction of it, and space
    is O(n) for the recursion.

The lesson behind it: Word Search & Pruning
    https://bytepatterns.com/learn/backtracking/word-search-and-pruning
    python backtracking/05-word-search-and-pruning.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/matchsticks-into-a-square

Run it:  python problems/backtracking/10-matchsticks-into-a-square.py
"""


def makes_square(sticks):
    total = sum(sticks)
    if len(sticks) < 4 or total % 4:
        return False
    side = total // 4
    sticks = sorted(sticks, reverse=True)       # hardest sticks first
    if sticks[0] > side:
        return False
    sides = [0] * 4

    def place(i):
        if i == len(sticks):
            return True                         # every side is exactly full
        tried = set()
        for s in range(4):
            if sides[s] in tried or sides[s] + sticks[i] > side:
                continue                        # same length as a side already tried
            tried.add(sides[s])
            sides[s] += sticks[i]
            if place(i + 1):
                return True
            sides[s] -= sticks[i]               # undo and try the next side
        return False

    return place(0)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(makes_square([1, 1, 2, 2, 2]), True)
    check(makes_square([3, 3, 3, 3, 4]), False)
    check(makes_square([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]), True)
    check(makes_square([1, 1, 1]), False)
