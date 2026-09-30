"""
Can the Last Index Be Reached (easy) · patterns: greedy, farthest-reach

You start at index 0 of a list of non-negative integers. The value at each
index is the longest jump you can make from there, so from index i you can
land on any index from i + 1 to i + jumps[i]. Return True if you can reach
the last index, otherwise False.

Examples:

    Input:  jumps = [2, 3, 1, 1, 4]
    Output: True
    Why:    jump 1 step to index 1, then 3 steps to the end

    Input:  jumps = [3, 2, 1, 0, 4]
    Output: False
    Why:    every route lands on index 3, whose value 0 goes nowhere

    Input:  jumps = [0]
    Output: True
    Why:    edge case, you already stand on the last index

Approach:
    The reachable indices always form one unbroken block starting at 0,
    because if you can land on index i you can also stop anywhere before
    your full jump. So the whole state is one number, the right edge of that
    block. Walking left to right, each index inside the block may push the
    edge further; the first index outside it proves that nothing beyond can
    be reached, since no reachable index jumped far enough. That is why the
    greedy choice is safe: keeping the farthest reach loses no information
    about which route got there. One pass, O(n) time and O(1) space.

The lesson behind it: Jump Game
    https://bytepatterns.com/learn/greedy/jump-game
    python greedy/03-jump-game.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/can-the-last-index-be-reached

Run it:  python problems/greedy/13-can-the-last-index-be-reached.py
"""


def can_reach_end(jumps):
    reach = 0                            # farthest index reachable so far
    for i, step in enumerate(jumps):
        if i > reach:                    # a gap nobody can jump over
            return False
        reach = max(reach, i + step)
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(can_reach_end([2, 3, 1, 1, 4]), True)
    check(can_reach_end([3, 2, 1, 0, 4]), False)
    check(can_reach_end([0]), True)
