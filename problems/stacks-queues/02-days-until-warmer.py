"""
Days Until Warmer (medium) · patterns: monotonic-stack

You are given daily temperature readings in order. For each day, report how
many days you must wait before a strictly warmer reading appears. Write 0
for any day that is never followed by a warmer one.

Examples:

    Input:  temps = [30, 32, 31, 35]
    Output: [1, 2, 1, 0]
    Why:    day 0 waits one day, day 1 waits until day 3, day 3 never warms up

    Input:  temps = [40, 39, 38]
    Output: [0, 0, 0]
    Why:    the readings only cool down

    Input:  temps = [20]
    Output: [0]
    Why:    edge case, a single day has no future at all

Approach:
    Positions of days still waiting for a warmer reading are held on a
    stack, and their temperatures always decrease from bottom to top. Each
    new day resolves every waiting day it beats by popping them and
    recording the gap between the positions. Any day left on the stack at
    the end never warms up and keeps its zero. Each position is pushed and
    popped at most once, so time is O(n) and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/stacks-queues/days-until-warmer

Run it:  python problems/stacks-queues/02-days-until-warmer.py
"""


def days_until_warmer(temps):
    out = [0] * len(temps)           # unresolved days keep their zero
    stack = []                       # positions still waiting for warmth
    for i, t in enumerate(temps):
        # today resolves every waiting day it beats
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            out[j] = i - j
        stack.append(i)
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(days_until_warmer([30, 32, 31, 35]), [1, 2, 1, 0])
    check(days_until_warmer([40, 39, 38]), [0, 0, 0])
    check(days_until_warmer([20]), [0])
