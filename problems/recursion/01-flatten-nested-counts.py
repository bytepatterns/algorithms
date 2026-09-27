"""
Flatten a Nested List (easy) · patterns: recursion, tree-walk

You are given a list whose items are either integers or further lists,
nested to any depth. Return a single flat list holding every integer in the
order they appear when reading the structure left to right. Empty lists
contribute nothing.

Examples:

    Input:  items = [1, [2, [3, 4]], 5]
    Output: [1, 2, 3, 4, 5]
    Why:    depth does not change the reading order

    Input:  items = [[], [[]], [1]]
    Output: [1]
    Why:    empty lists at any depth disappear

    Input:  items = []
    Output: []
    Why:    edge case, nothing to read at all

Approach:
    Every item is either a value to keep or a smaller copy of the same
    problem, which is exactly the shape recursion is for. Walking the items
    in order preserves the reading order, and extending with the sub-result
    keeps the nesting invisible in the output. The empty list needs no
    special case: the loop simply never runs. Every integer and every list
    node is visited once, so time is O(n) in the total number of nodes, and
    the stack goes as deep as the nesting does.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/flatten-nested-counts

Run it:  python problems/recursion/01-flatten-nested-counts.py
"""


def flatten(items):
    flat = []
    for item in items:
        if isinstance(item, list):
            flat.extend(flatten(item))   # a nested list is a smaller problem
        else:
            flat.append(item)
    return flat


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
    check(flatten([[], [[]], [1]]), [1])
    check(flatten([]), [])
