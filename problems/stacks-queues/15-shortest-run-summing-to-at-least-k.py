"""
Shortest Run Summing to at Least K (hard) · patterns: monotonic-deque, prefix-sum

Given a list of integers nums, which may include negative numbers, and a
positive integer k, return the length of the shortest non-empty contiguous
run whose sum is at least k. If no run reaches k, return -1.

Examples:

    Input:  nums = [2, -1, 2], k = 3
    Output: 3
    Why:    only the whole list sums to 3

    Input:  nums = [84, -37, 32, 40, 95], k = 167
    Output: 3
    Why:    32 + 40 + 95 = 167; the whole list sums to 214 but is longer

    Input:  nums = [1, 2], k = 4
    Output: -1
    Why:    edge case, even the whole list falls short

Approach:
    Prefix sums turn "a run summing to at least k" into "a pair i < j with
    prefix[j] - prefix[i] >= k", and the goal becomes the pair with the
    smallest j - i. The deque holds the starts still worth trying, with
    their prefix values increasing from front to back, the same monotonic
    deque that answers sliding window maximum. Two pruning rules keep it
    small. From the back: a start whose prefix is at least prefix[j] can
    never beat j as a start, since j is later and not larger. From the
    front: once a start works for end j, any later end would only make that
    run longer, so the start is recorded and dropped. Every index enters and
    leaves the deque at most once, so time is O(n) and space is O(n).

The lesson behind it: Sliding Window Maximum
    https://bytepatterns.com/learn/stacks-queues/sliding-window-maximum
    python stacks-queues/07-sliding-window-maximum.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/shortest-run-summing-to-at-least-k

Run it:  python problems/stacks-queues/15-shortest-run-summing-to-at-least-k.py
"""


from collections import deque

def shortest_run(nums, k):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    best = len(nums) + 1
    starts = deque()                             # candidate starts, prefix values increasing
    for j, p in enumerate(prefix):
        while starts and p - prefix[starts[0]] >= k:
            best = min(best, j - starts.popleft())   # no later end can beat this for that start
        while starts and prefix[starts[-1]] >= p:
            starts.pop()                         # j is a later and no larger start
        starts.append(j)
    return best if best <= len(nums) else -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(shortest_run([2, -1, 2], 3), 3)
    check(shortest_run([84, -37, 32, 40, 95], 167), 3)
    check(shortest_run([1, 2], 4), -1)
