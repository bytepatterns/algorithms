"""
Largest Bar Rectangle (hard) · patterns: monotonic-stack

A bar chart is described by a list of heights, where every bar has width one
and they stand side by side with no gaps. Find the area of the largest
rectangle that fits entirely inside the bars. The rectangle may span several
neighbouring bars, but its height can never exceed the shortest bar it
covers.

Examples:

    Input:  heights = [2, 1, 5, 6, 2, 3]
    Output: 10
    Why:    the bars of height 5 and 6 support a rectangle two wide and five tall

    Input:  heights = [2, 4]
    Output: 4
    Why:    one tall bar beats the two-wide rectangle of height two

    Input:  heights = []
    Output: 0
    Why:    edge case, an empty chart holds no rectangle

Approach:
    Each rectangle is limited by its shortest bar, so it is enough to
    compute, for every bar, how far it can stretch before hitting a shorter
    one on either side. A stack of positions with non-decreasing heights
    makes both walls appear exactly once: the incoming bar is the right wall
    of everything taller that it pops, and the position left underneath
    after the pop is the left wall. A zero-height sentinel at the end forces
    every remaining bar to be measured. Each position is pushed and popped
    once, so time is O(n) and space is O(n).

The lesson behind it: Largest Rectangle
    https://bytepatterns.com/learn/stacks-queues/largest-rectangle
    python stacks-queues/09-largest-rectangle.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/largest-bar-rectangle

Run it:  python problems/stacks-queues/05-largest-bar-rectangle.py
"""


def largest_rectangle(heights):
    stack = []                       # positions with non-decreasing heights
    best = 0
    for i, h in enumerate(heights + [0]):    # the sentinel drains the stack
        while stack and heights[stack[-1]] >= h:
            top = stack.pop()
            # whatever is left underneath is the first shorter bar on the left
            left = stack[-1] + 1 if stack else 0
            best = max(best, heights[top] * (i - left))
        stack.append(i)
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(largest_rectangle([2, 1, 5, 6, 2, 3]), 10)
    check(largest_rectangle([2, 4]), 4)
    check(largest_rectangle([]), 0)
