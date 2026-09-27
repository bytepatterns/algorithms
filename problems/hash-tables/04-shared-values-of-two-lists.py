"""
Shared Values Of Two Lists (easy) · patterns: hash-set, membership-test

Given two lists of values, return the values that occur in both of them.
Each shared value appears once in the result even when either list repeats
it, and the result follows the order in which the values first show up in
the first list.

Examples:

    Input:  a = [1, 2, 2, 1], b = [2, 2]
    Output: [2]
    Why:    a shared value is reported once no matter how often it repeats

    Input:  a = [4, 9, 5], b = [9, 4, 9, 8, 4]
    Output: [4, 9]
    Why:    the order comes from the first list, not the second

    Input:  a = [1, 2], b = [3]
    Output: []
    Why:    edge case, the lists have nothing in common

Approach:
    Loading the second list into a set turns each of the n comparisons into
    a constant-time lookup instead of a scan. Walking the first list in
    order means the output order falls out for free, and a second set of
    already-reported values keeps repeats out without sorting or
    post-processing. Time is O(n + m) on average, and space is O(m) for the
    lookup set plus the reported values.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/hash-tables/shared-values-of-two-lists

Run it:  python problems/hash-tables/04-shared-values-of-two-lists.py
"""


def shared_values(a, b):
    pool = set(b)                    # membership in b is now a constant-time test
    out, reported = [], set()
    for x in a:
        if x in pool and x not in reported:
            out.append(x)            # first appearance in a fixes the order
            reported.add(x)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(shared_values([1, 2, 2, 1], [2, 2]), [2])
    check(shared_values([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
    check(shared_values([1, 2], [3]), [])
