"""
Pie Slices With Two Friends (hard) · patterns: circular-dp, exact-count-dp

A round pie is cut into 3n slices of different sizes, arranged in a circle.
You take any remaining slice, then one friend takes the remaining slice just
before it on the circle and another friend takes the remaining slice just
after it. This repeats until the pie is gone. Return the largest total size
you can collect.

Examples:

    Input:  slices = [4, 1, 2, 8, 3, 5]
    Output: 13
    Why:    take 8 (friends take 2 and 3), then take 5 (friends take 4 and 1)

    Input:  slices = [8, 1, 1, 1, 1, 8]
    Output: 9
    Why:    the two 8s touch across the join of the circle, so taking
            one always hands the other to a friend

    Input:  slices = [5, 2, 7]
    Output: 7
    Why:    edge case, one round: take the biggest slice

Approach:
    Taking a slice always hands both of its current neighbours to your
    friends, so the slices you collect are never adjacent on the original
    circle. In the other direction, n slices with no two adjacent can always
    be collected: take a wanted slice that sits next to a run of at least
    two unwanted slices, and the rest stay separated. So the game is house
    robber on a circle with exactly n picks. Dropping the first slice or the
    last slice breaks the circle into a line, and the better of the two
    lines is the answer; the line table has a row per slice and a column per
    pick count, and only two rows are kept. Time is O(n²) and space is O(n).

The lesson behind it: House Robber in a Circle
    https://bytepatterns.com/learn/dynamic-programming/house-robber-circle
    python dynamic-programming/14-house-robber-circle.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/pie-slices-with-two-friends

Run it:  python problems/dynamic-programming/20-pie-slices-with-two-friends.py
"""


def best_share(slices):
    picks, NEG = len(slices) // 3, float("-inf")

    def best_line(a):
        # rows of best[i][j]: the most from the first i slices using exactly j picks
        two_back, one_back = [0] + [NEG] * picks, [0] + [NEG] * picks
        for x in a:
            row = [0] + [max(one_back[j], two_back[j - 1] + x) for j in range(1, picks + 1)]
            two_back, one_back = one_back, row
        return one_back[picks]

    # the first and last slices touch, so never allow both
    return max(best_line(slices[1:]), best_line(slices[:-1]))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(best_share([4, 1, 2, 8, 3, 5]), 13)
    check(best_share([8, 1, 1, 1, 1, 8]), 9)
    check(best_share([5, 2, 7]), 7)
