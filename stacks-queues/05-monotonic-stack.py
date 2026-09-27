"""
Monotonic Stack: Keep the stack ordered and every item waits only once.

Hold a stack whose values only ever decrease from bottom to top. A new value
pops everything smaller than itself — and it is the answer for each one it
pops. Since every index is pushed once and popped once, a search that looks
O(n²) finishes in O(n).

Lesson 5 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/monotonic-stack

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python stacks-queues/05-monotonic-stack.py
"""


def next_greater(nums):
    result = [-1] * len(nums)
    stack = []                            # indexes, values decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x       # x answers everyone smaller
        stack.append(i)
    return result                         # -1 means nothing bigger ahead


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(next_greater([2, 1, 3]), [3, 3, -1])
    check(next_greater([5, 4, 3]), [-1, -1, -1])
