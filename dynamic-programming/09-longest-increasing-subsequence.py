"""
Longest Increasing Subsequence: Every element asks which smaller one it can extend.

Scan left to right. For each element, look back at every earlier element
that is smaller and ask which chain it can extend, keeping the longest one
found. The answer is the largest value anywhere in that table, not the final
cell, because the best chain may end in the middle. Elements are never
reordered.

Lesson 9 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/longest-increasing-subsequence

Run it:  python dynamic-programming/09-longest-increasing-subsequence.py
"""


def lis(nums):
    best = [1] * len(nums)              # best[i] = longest chain ending at i
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:       # nums[i] can extend the chain ending at j
                best[i] = max(best[i], best[j] + 1)
    return max(best) if best else 0


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
    check(lis([7, 7, 7]), 1)
