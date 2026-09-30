"""
Count Out-of-Order Pairs (hard) · patterns: merge-sort, divide-and-conquer, inversion-count

A ranking service measures how far a user's list is from sorted by counting
inverted pairs: positions i < j where nums[i] > nums[j]. Given a list of up
to 100,000 integers, return that count. Equal values never form a pair.
Comparing every pair would take about five billion steps at the upper limit,
so the count has to come out of an O(n log n) process.

Examples:

    Input:  nums = [2, 4, 1, 3, 5]
    Output: 3
    Why:    (2, 1), (4, 1) and (4, 3)

    Input:  nums = [5, 4, 3, 2, 1]
    Output: 10
    Why:    fully reversed, every one of the 5 × 4 / 2 pairs is inverted

    Input:  nums = [1, 1, 1]
    Output: 0
    Why:    edge case, equal values are not out of order

Approach:
    Merge sort already compares elements across the two halves, and that
    comparison is where cross pairs can be counted in bulk. After both
    halves are sorted recursively, their own inversions are counted and the
    order inside each half no longer matters for the cross pairs, since
    sorting a half keeps every element on the same side. During the merge,
    taking right[j] while left[i:] is still waiting means right[j] is
    smaller than all of those left elements, so it contributes len(left) - i
    pairs in one step. Taking the left element on ties keeps equal values
    from being counted. The total is the left count plus the right count
    plus the cross count, and the work is the same as merge sort: O(n log n)
    time and O(n) space.

The lesson behind it: Merge Sort
    https://bytepatterns.com/learn/sorting/merge-sort
    python sorting/05-merge-sort.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/sorting/count-out-of-order-pairs

Run it:  python problems/sorting/12-count-out-of-order-pairs.py
"""


def count_inversions(nums):
    def sort(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, x = sort(a[:mid])
        right, y = sort(a[mid:])
        merged, i, j, cross = [], 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:          # ties go left: not inverted
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                cross += len(left) - i       # beats every waiting left element
        merged += left[i:] + right[j:]
        return merged, x + y + cross
    return sort(list(nums))[1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(count_inversions([2, 4, 1, 3, 5]), 3)
    check(count_inversions([5, 4, 3, 2, 1]), 10)
    check(count_inversions([1, 1, 1]), 0)
