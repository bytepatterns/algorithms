"""
Depth Weighted Nested Sum (easy) · patterns: recursion, pass-down

A list holds integers and further lists, nested to any depth. Items in the
outer list sit at depth 1, items in a list inside it at depth 2, and so on.
Return the sum of every integer multiplied by the depth it sits at.

Examples:

    Input:  items = [[1, 1], 2, [1, 1]]
    Output: 10
    Why:    four 1s at depth 2 give 8, and the 2 at depth 1 gives 2

    Input:  items = [1, [4, [6]]]
    Output: 27
    Why:    1  1 + 4  2 + 6 * 3

    Input:  items = [[[]]]
    Output: 0
    Why:    edge case, deep nesting with no integers adds nothing

Approach:
    The depth of an integer is decided entirely by the path from the outer
    list down to it, so it is information that flows downwards, which makes
    it a parameter rather than a return value. Each call adds its own
    integers weighted by the depth it was handed and passes depth plus one
    to the lists inside it, while the partial sums flow back up as return
    values. An empty list simply returns zero. Every integer and every list
    is visited once, so time is O(n) in the total number of items, and the
    call stack is as deep as the nesting.

The lesson behind it: Return Up or Pass Down
    https://bytepatterns.com/learn/recursion/return-up-or-pass-down
    python recursion/06-return-up-or-pass-down.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/depth-weighted-nested-sum

Run it:  python problems/recursion/04-depth-weighted-nested-sum.py
"""


def weighted_sum(items, depth=1):
    total = 0
    for item in items:
        if isinstance(item, list):
            total += weighted_sum(item, depth + 1)   # depth travels down
        else:
            total += item * depth                    # sums travel back up
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(weighted_sum([[1, 1], 2, [1, 1]]), 10)
    check(weighted_sum([1, [4, [6]]]), 27)
    check(weighted_sum([[[]]]), 0)
