"""
Sliding Window Maximum: A queue that drops anyone it has already outgrown.

Recomputing the maximum for every window costs O(nk). Instead hold a deque
of indexes whose values decrease from front to back.

A new value pops every smaller one from the back — they are older and
weaker, so they are finished. The front expires when it leaves the window.
The front is always the answer.

Lesson 7 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/sliding-window-maximum

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python stacks-queues/07-sliding-window-maximum.py
"""


from collections import deque

def window_max(nums, k):
    dq, out = deque(), []                  # dq holds indexes, their values decreasing
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                       # smaller and older than x: never the max again
        dq.append(i)
        if dq[0] == i - k: dq.popleft()    # the front just slid out of the window
        if i >= k - 1: out.append(nums[dq[0]])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(window_max([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
