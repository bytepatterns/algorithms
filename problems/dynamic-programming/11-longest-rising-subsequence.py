"""
Longest Rising Subsequence (medium) · patterns: bottom-up-dp, subsequence-dp

Given a list of numbers, pick some of them while keeping their original
order so that every picked number is strictly larger than the one picked
before it. Return the largest number of values such a pick can contain. The
values do not have to be next to each other in the list, and an empty list
gives 0.

Examples:

    Input:  nums = [4, 1, 3, 2, 5, 3, 6]
    Output: 4
    Why:    1, 3, 5, 6 rises four times; 1, 2, 3, 6 does too

    Input:  nums = [5, 5, 5]
    Output: 1
    Why:    equal values do not count as rising

    Input:  nums = []
    Output: 0
    Why:    edge case, nothing to pick

Approach:
    Let ends_here[i] be the length of the longest rising pick that finishes
    with nums[i]. Such a pick is either nums[i] alone or a pick ending at
    some earlier, smaller value with nums[i] appended, so ends_here[i] is
    one more than the best of those earlier entries. Filling the table left
    to right means every earlier entry is final before it is read, and the
    answer is the largest entry. Time is O(n squared) and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/longest-rising-subsequence

Run it:  python problems/dynamic-programming/11-longest-rising-subsequence.py
"""


def longest_rise(nums):
    ends_here = [1] * len(nums)      # longest rise that finishes at index i
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:    # nums[i] can extend any rise ending on a smaller value
                ends_here[i] = max(ends_here[i], ends_here[j] + 1)
    return max(ends_here, default=0)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(longest_rise([4, 1, 3, 2, 5, 3, 6]), 4)
    check(longest_rise([5, 5, 5]), 1)
    check(longest_rise([]), 0)
