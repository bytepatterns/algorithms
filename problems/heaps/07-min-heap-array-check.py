"""
Min-Heap Array Check (easy) · patterns: heap, array-as-tree

A list of numbers can be read as a binary tree: the value at index i has its
children at indexes 2i + 1 and 2i + 2, when those exist. Decide whether the
list already satisfies the min-heap rule, meaning no value is larger than
either of its children. Return True if it does and False otherwise. An empty
list or a single value counts as a valid heap.

Examples:

    Input:  values = [1, 3, 2, 7, 4]
    Output: True
    Why:    1 sits above 3 and 2, and 3 sits above 7 and 4

    Input:  values = [2, 1, 3]
    Output: False
    Why:    the root 2 is larger than its left child 1

    Input:  values = [5, 5, 5]
    Output: True
    Why:    edge case, equal values never break the rule

Approach:
    The heap rule is local: if each parent is no larger than its children,
    then every ancestor is no larger than every descendant, because the
    comparisons chain. So it is enough to check each non-root index against
    its parent, which lives at (i - 1) // 2. Checking from the child side
    visits every parent-child pair exactly once. Time is O(n) and space is
    O(1).

The lesson behind it: Heapify and Sift
    https://bytepatterns.com/learn/heaps/heapify-and-sift
    python heaps/02-heapify-and-sift.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/min-heap-array-check

Run it:  python problems/heaps/07-min-heap-array-check.py
"""


def is_min_heap(values):
    for child in range(1, len(values)):
        parent = (child - 1) // 2     # the array position of this value's parent
        if values[parent] > values[child]:
            return False              # one broken pair is enough to fail
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_min_heap([1, 3, 2, 7, 4]), True)
    check(is_min_heap([2, 1, 3]), False)
    check(is_min_heap([5, 5, 5]), True)
