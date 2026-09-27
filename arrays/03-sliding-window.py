"""
Sliding Window: Reuse the last answer instead of recomputing it.

A window is a contiguous run of elements. Instead of rebuilding each window
from scratch, add the element entering and subtract the one leaving. The
cost drops from O(n·k) all the way to O(n).

Lesson 3 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/sliding-window

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python arrays/03-sliding-window.py
"""


def max_window_sum(nums, k):
    window = sum(nums[:k])       # the first window
    best = window
    for i in range(k, len(nums)):
        window += nums[i]        # element enters
        window -= nums[i - k]    # element leaves
        best = max(best, window)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_window_sum([1, 9, 2, 6, 3], 2), 11)
