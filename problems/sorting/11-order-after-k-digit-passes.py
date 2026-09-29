"""
Order After K Digit Passes (medium) · patterns: radix-sort, stable-sort, bucket-sort

A radix sort on whole numbers that are zero or more works one decimal digit
at a time, starting from the ones digit. Each pass stably regroups the list
by the current digit, 0 first and 9 last, keeping the existing order inside
each group. Given a list and a number k, return the list exactly as it looks
after the first k passes.

Examples:

    Input:  nums = [53, 7, 318, 90, 41, 206, 17], k = 1
    Output: [90, 41, 53, 206, 7, 17, 318]
    Why:    grouped by ones digit: 0, 1, 3, 6, 7, 7, 8; 7 stays ahead of 17

    Input:  nums = [53, 7, 318, 90, 41, 206, 17], k = 2
    Output: [206, 7, 17, 318, 41, 53, 90]
    Why:    the second pass regroups the first pass's output by the tens digit

    Input:  nums = [30, 3, 300], k = 0
    Output: [30, 3, 300]
    Why:    edge case, no passes, so nothing moves

Approach:
    Each pass drops every number into one of ten buckets by its current
    digit, in the order the list already has, then concatenates the buckets
    from 0 to 9. Because the buckets are filled in list order, numbers with
    the same digit keep their earlier relative order, which is the stability
    that makes the later passes build on the earlier ones. After k passes
    the list is ordered by its last k digits, ties in original order. Time
    is O(k(n + 10)), and space is O(n) for the buckets.

The lesson behind it: Radix Sort
    https://bytepatterns.com/learn/sorting/radix-sort
    python sorting/10-radix-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/order-after-k-digit-passes

Run it:  python problems/sorting/11-order-after-k-digit-passes.py
"""


def after_passes(nums, k):
    order, place = list(nums), 1
    for _ in range(k):
        buckets = [[] for _ in range(10)]
        for x in order:                          # list order in, so the pass is stable
            buckets[x // place % 10].append(x)
        order = [x for b in buckets for x in b]  # read back digit 0 to 9
        place *= 10
    return order


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(after_passes([53, 7, 318, 90, 41, 206, 17], 1), [90, 41, 53, 206, 7, 17, 318])
    check(after_passes([53, 7, 318, 90, 41, 206, 17], 2), [206, 7, 17, 318, 41, 53, 90])
    check(after_passes([30, 3, 300], 0), [30, 3, 300])
