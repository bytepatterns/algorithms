"""
Window Maximums (hard) · patterns: sliding-window, monotonic-deque

A window of fixed width k slides across a list of integers, one position at
a time, from the far left to the far right. Report the maximum value inside
the window at every stop. The output therefore holds one number for each
window position.

Examples:

    Input:  nums = [1, 4, 2, 7, 3, 3], k = 3
    Output: [4, 7, 7, 7]
    Why:    the windows are 1,4,2 then 4,2,7 then 2,7,3 then 7,3,3

    Input:  nums = [5, 5, 5], k = 1
    Output: [5, 5, 5]
    Why:    edge case, a width of one makes every element its own maximum

    Input:  nums = [2, 1], k = 2
    Output: [2]
    Why:    the window covers the whole list, so there is a single stop

Approach:
    A double-ended queue stores positions whose values decrease from front
    to back, which makes the front position the current maximum by
    construction. A new element evicts every smaller value at the back,
    because those can never win again while the newer, larger one is in
    range. The front is dropped as soon as it slides out of the window. Each
    position is pushed and popped at most once, so time is O(n) and space is
    O(k).

The lesson behind it: Sliding Window Maximum
    https://bytepatterns.com/learn/stacks-queues/sliding-window-maximum
    python stacks-queues/07-sliding-window-maximum.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/window-maximums

Run it:  python problems/arrays/05-window-maximums.py
"""


from collections import deque
def window_maximums(nums, k):
    out, dq = [], deque()            # dq holds positions, values decreasing
    for i, x in enumerate(nums):
        if dq and dq[0] <= i - k:    # the front just slid out of the window
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()                 # smaller older values can never win again
        dq.append(i)
        if i >= k - 1:               # the first full window ends here
            out.append(nums[dq[0]])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(window_maximums([1, 4, 2, 7, 3, 3], 3), [4, 7, 7, 7])
    check(window_maximums([5, 5, 5], 1), [5, 5, 5])
    check(window_maximums([2, 1], 2), [2])
