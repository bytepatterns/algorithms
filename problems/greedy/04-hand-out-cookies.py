"""
Hand Out Cookies (easy) · patterns: greedy, sorting, two-pointers

Each child has a smallest cookie size that will make them happy, and each
cookie has a size. A child gets at most one cookie and a cookie goes to at
most one child. Return the largest number of children you can make happy.

Examples:

    Input:  wants = [1, 2, 3], sizes = [1, 1]
    Output: 1
    Why:    both cookies only satisfy the child who wants size 1

    Input:  wants = [1, 2], sizes = [1, 2, 3]
    Output: 2

    Input:  wants = [5], sizes = []
    Output: 0
    Why:    edge case, no cookies means no happy children

Approach:
    After sorting, the least demanding waiting child is the one most worth
    serving, and the smallest cookie that satisfies them is the one whose
    use costs the least; an exchange argument shows that swapping any
    optimal assignment towards this choice never loses a happy child. A
    cookie too small for the least demanding waiting child is too small for
    everyone after them too, so it is discarded. One pass over the cookies
    with a pointer into the children does the rest. Time is O(n log n + m
    log m) for the sorts, and space is O(1) beyond them.

The lesson behind it: What Makes Greedy Work
    https://bytepatterns.com/learn/greedy/what-makes-greedy-work
    python greedy/01-what-makes-greedy-work.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/hand-out-cookies

Run it:  python problems/greedy/04-hand-out-cookies.py
"""


def happy_children(wants, sizes):
    wants, sizes = sorted(wants), sorted(sizes)
    child = 0                                  # least demanding child still waiting
    for s in sizes:                            # smallest cookie first
        if child < len(wants) and s >= wants[child]:
            child += 1                         # this cookie is enough, hand it over
    return child


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(happy_children([1, 2, 3], [1, 1]), 1)
    check(happy_children([1, 2], [1, 2, 3]), 2)
    check(happy_children([5], []), 0)
