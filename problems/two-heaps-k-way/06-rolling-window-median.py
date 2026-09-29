"""
Rolling Window Median (hard) · patterns: two-heaps, lazy-deletion, sliding-window

Slide a window of k consecutive values across a list of numbers, one
position at a time from left to right, and report the median of every
window. When k is even the median is the average of the two middle values.
Return the medians as floats. Re-sorting each window from scratch is too
slow for long lists.

Examples:

    Input:  nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Output: [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]

    Input:  nums = [1, 2, 3, 4], k = 4
    Output: [2.5]
    Why:    an even window averages its two middle values

    Input:  nums = [5, 5, 5], k = 1
    Output: [5.0, 5.0, 5.0]
    Why:    edge case, a window of one value is its own median

Approach:
    The small half lives in a max-heap and the large half in a min-heap, so
    the median always sits at one or both tops. When a value leaves the
    window it is only recorded in a pending-removal counter, and the heap it
    logically belongs to is decided by comparing it with the small half's
    top; it is physically discarded later, when it reaches a top. A balance
    counter tracks live sizes rather than list lengths, and tops are moved
    across until the small half holds as many live values as the large half,
    or one more. Each value is pushed and popped a constant number of times,
    so time is O(n log n) and space is O(n).

The lesson behind it: Sliding Window Median
    https://bytepatterns.com/learn/two-heaps-k-way/sliding-window-median
    python two-heaps-k-way/04-sliding-window-median.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/rolling-window-median

Run it:  python problems/two-heaps-k-way/06-rolling-window-median.py
"""


import heapq
from collections import Counter

def window_medians(nums, k):
    lo, hi, gone, out, bal = [], [], Counter(), [], 0   # lo holds negated values
    def clean(h, sign):                                 # drop tops that already left
        while h and gone[sign * h[0]]:
            gone[sign * heapq.heappop(h)] -= 1
    for i, x in enumerate(nums):
        if lo and x <= -lo[0]: heapq.heappush(lo, -x); bal += 1
        else: heapq.heappush(hi, x); bal -= 1
        if i >= k:                                      # retire nums[i - k] lazily
            y = nums[i - k]; gone[y] += 1
            bal += -1 if lo and y <= -lo[0] else 1
        while bal > 1 or bal < 0:                       # live sizes must be equal or +1
            clean(lo, -1); clean(hi, 1)
            if bal > 1: heapq.heappush(hi, -heapq.heappop(lo)); bal -= 2
            else: heapq.heappush(lo, -heapq.heappop(hi)); bal += 2
        clean(lo, -1); clean(hi, 1)
        if i >= k - 1:
            out.append(float(-lo[0]) if k % 2 else (-lo[0] + hi[0]) / 2)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(window_medians([1, 3, -1, -3, 5, 3, 6, 7], 3), [1.0, -1.0, -1.0, 3.0, 5.0, 6.0])
    check(window_medians([1, 2, 3, 4], 4), [2.5])
    check(window_medians([5, 5, 5], 1), [5.0, 5.0, 5.0])
