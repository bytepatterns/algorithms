"""
Signs That Hit a Target (medium) · patterns: 0-1-knapsack, subset-count

Given a list of non-negative integers and a target, put a plus or a minus
sign in front of every number and add them all up. Return how many different
sign choices give exactly the target. A zero counts twice, since +0 and -0
are different choices.

Examples:

    Input:  nums = [1, 2, 3, 4], target = 2
    Output: 2
    Why:    -1 + 2 - 3 + 4 and 1 + 2 + 3 - 4 both give 2

    Input:  nums = [0, 5], target = 5
    Output: 2
    Why:    +0 + 5 and -0 + 5 are different choices

    Input:  nums = [3], target = 2
    Output: 0
    Why:    edge case, only 3 and -3 are possible

Approach:
    Choosing signs is the same as choosing the subset that gets a plus, and
    P - M = target together with P + M = total forces P = (total + target) /
    2. Counting subsets with a fixed sum is 0/1 knapsack with counts in
    place of values, and walking the sums downward stops a number from being
    used twice in one pass. Zeros need no special case: each zero doubles
    every count, matching its two signs. Time is O(n × goal) and space is
    O(goal).

The lesson behind it: 0/1 Knapsack
    https://bytepatterns.com/learn/dynamic-programming/knapsack-01
    python dynamic-programming/07-knapsack-01.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/signs-that-hit-a-target

Run it:  python problems/dynamic-programming/18-signs-that-hit-a-target.py
"""


def sign_ways(nums, target):
    total = sum(nums)
    if abs(target) > total or (total + target) % 2:
        return 0                              # out of reach, or the wrong parity
    goal = (total + target) // 2              # what the plus-signed numbers must add to
    ways = [1] + [0] * goal
    for x in nums:
        for s in range(goal, x - 1, -1):      # downward: each number used at most once
            ways[s] += ways[s - x]
    return ways[goal]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(sign_ways([1, 2, 3, 4], 2), 2)
    check(sign_ways([0, 5], 5), 2)
    check(sign_ways([3], 2), 0)
