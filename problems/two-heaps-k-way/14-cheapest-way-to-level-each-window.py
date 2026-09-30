"""
Cheapest Way to Level Each Window (hard) · patterns: two-heaps, sliding-window, lazy-deletion

You may add or subtract 1 from any value, one unit per step. For every
window of k consecutive values in a list, return the fewest steps needed to
make all values in that window equal. Windows are costed independently, and
the list itself never changes. There are up to 100,000 values and k can be
as large as the list.

Examples:

    Input:  nums = [1, 3, 2, 8, 5, 5], k = 3
    Output: [2, 6, 6, 3]
    Why:    [3, 2, 8] is levelled to its median 3 for 1 + 0 + 5 = 6 steps

    Input:  nums = [4, 4, 4, 1], k = 2
    Output: [0, 0, 3]
    Why:    the last window [4, 1] costs 3 whichever value both end up at between 1 and 4

    Input:  nums = [7, 2, 9], k = 1
    Output: [0, 0, 0]
    Why:    edge case, a single value is already level

Approach:
    For a fixed set of values, the total distance to a point is minimised at
    the median: moving the point toward the side with more values always
    helps, so it settles in the middle. Each window's answer is therefore a
    sum of distances to its median, and with two heaps that sum is available
    in constant time from each half's size and total, since every value
    below the median contributes median - x and every value above
    contributes x - median. The difficult part is removing the value that
    slides out, which sits somewhere inside a heap. Storing (value, index)
    pairs makes every entry unique, so comparing the leaving pair with the
    lower half's top says exactly which half it is in; that half's size and
    sum are fixed at once, while the entry itself stays in the heap until it
    surfaces at a top and is discarded as expired. Rebalancing moves live
    tops between the halves so the lower half has the same size as the upper
    or one more. Each value is pushed and popped a constant number of times,
    so time is O(n log n) and space is O(n).

The lesson behind it: Sliding Window Median
    https://bytepatterns.com/learn/two-heaps-k-way/sliding-window-median
    python two-heaps-k-way/04-sliding-window-median.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/two-heaps-k-way/cheapest-way-to-level-each-window

Run it:  python problems/two-heaps-k-way/14-cheapest-way-to-level-each-window.py
"""


import heapq

def level_costs(nums, k):
    lo, hi = [], []                  # lo: max-heap of (-value, -index); hi: min-heap of (value, index)
    size, total = [0, 0], [0, 0]     # live count and sum of each half: [lo, hi]
    left, out = 0, []                # left: first index still in the window

    def top(h):                      # discard expired entries, then peek
        while h[0][1] * (-1 if h is lo else 1) < left:
            heapq.heappop(h)
        return (-h[0][0], -h[0][1]) if h is lo else h[0]

    def shift(src, dst):             # move the live top of src into dst
        value, index = top(src)
        heapq.heappop(src)
        a, b = (0, 1) if src is lo else (1, 0)
        size[a] -= 1
        total[a] -= value
        size[b] += 1
        total[b] += value
        heapq.heappush(dst, (value, index) if dst is hi else (-value, -index))

    for i, x in enumerate(nums):
        if i >= k:                   # the pair sliding out, removed lazily
            old = (nums[i - k], i - k)
            half = 0 if old <= top(lo) else 1
            size[half] -= 1
            total[half] -= old[0]
            left = i - k + 1
        if size[0] and (x, i) < top(lo):
            heapq.heappush(lo, (-x, -i))
            size[0] += 1
            total[0] += x
        else:
            heapq.heappush(hi, (x, i))
            size[1] += 1
            total[1] += x
        while size[0] > size[1] + 1:
            shift(lo, hi)
        while size[0] < size[1]:
            shift(hi, lo)
        if i >= k - 1:
            med = top(lo)[0]         # the lower median
            out.append(med * size[0] - total[0] + total[1] - med * size[1])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(level_costs([1, 3, 2, 8, 5, 5], 3), [2, 6, 6, 3])
    check(level_costs([4, 4, 4, 1], 2), [0, 0, 3])
    check(level_costs([7, 2, 9], 1), [0, 0, 0])
