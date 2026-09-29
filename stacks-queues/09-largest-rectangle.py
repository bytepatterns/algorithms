"""
Largest Rectangle: Every bar waits on the stack until both its walls are known.

A rectangle is a height times a width, and the width is what is hard: how
far left and right can this bar stretch before something shorter blocks it?

Keep a stack of bars with increasing heights. A shorter bar arriving is the
right wall for every taller bar on the stack — and the bar left underneath
is the left wall.

Lesson 9 of Stacks & Queues, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/stacks-queues/largest-rectangle

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python stacks-queues/09-largest-rectangle.py
"""


def largest_rect(h):
    stack, best = [], 0                        # indexes, their heights increasing
    for i, x in enumerate(h + [0]):            # the trailing 0 flushes the stack
        while stack and h[stack[-1]] >= x:
            top = h[stack.pop()]               # this bar can grow no further right
            left = stack[-1] + 1 if stack else 0
            best = max(best, top * (i - left)) # it reaches back to `left`
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
    check(largest_rect([2, 1, 5, 6, 2, 3]), 10)  # bars 5 and 6, width 2
    check(largest_rect([3, 3, 3]), 9)
