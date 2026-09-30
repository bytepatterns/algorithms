"""
Next Greater Value Lookup (easy) · patterns: monotonic-stack, hash-map

You are given a list nums of distinct integers and a list queries whose
values all appear somewhere in nums. For each query value, find the first
value to its right in nums that is larger than it, or -1 when no larger
value follows. Return the answers in query order.

Examples:

    Input:  nums = [4, 1, 3, 6, 2, 5], queries = [1, 3, 2, 6]
    Output: [3, 6, 5, -1]
    Why:    1 is followed by 3, 3 by 6 and 2 by 5, while nothing after 6 is larger

    Input:  nums = [5, 4, 3, 2, 1], queries = [4, 1]
    Output: [-1, -1]
    Why:    the list only falls, so no value ever has a larger one after it

    Input:  nums = [7], queries = [7]
    Output: [-1]
    Why:    edge case, a single value has nothing to its right

Approach:
    A value waits on the stack until the first larger value arrives, and at
    that moment it is on top, because anything pushed after it and still
    waiting is smaller than it. So one left-to-right pass pops each value
    exactly when its answer shows up and records the pair in a dictionary,
    and whatever is still on the stack at the end never got an answer. The
    queries are then plain lookups. Every value is pushed and popped at most
    once, so time is O(n + q) and space is O(n).

The lesson behind it: Monotonic Stack
    https://bytepatterns.com/learn/stacks-queues/monotonic-stack
    python stacks-queues/05-monotonic-stack.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/next-greater-value-lookup

Run it:  python problems/stacks-queues/12-next-greater-value-lookup.py
"""


def next_greater_lookup(nums, queries):
    answer = {}
    stack = []                        # waiting values, falling from bottom to top
    for x in nums:
        while stack and stack[-1] < x:
            answer[stack.pop()] = x   # x is the first larger value after it
        stack.append(x)
    return [answer.get(q, -1) for q in queries]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(next_greater_lookup([4, 1, 3, 6, 2, 5], [1, 3, 2, 6]), [3, 6, 5, -1])
    check(next_greater_lookup([5, 4, 3, 2, 1], [4, 1]), [-1, -1])
    check(next_greater_lookup([7], [7]), [-1])
