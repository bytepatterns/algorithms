"""
Linear Search: The simple one that always works. Often that's enough.

Check items one at a time until you find the target or run out of items. It
needs no ordering and no preparation at all. The worst case is O(n), and for
small or unsorted data that is genuinely the right choice.

Lesson 1 of Searching, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/searching/linear-search

Run it:  python searching/01-linear-search.py
"""


def linear_search(items, target):
    for i, item in enumerate(items):
        # check one at a time, in order
        if item == target:
            return i          # found it: return the index
    return -1                 # not here


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(linear_search(["red", "blue", "green"], "green"), 2)
    check(linear_search(["red", "blue", "green"], "pink"), -1)
