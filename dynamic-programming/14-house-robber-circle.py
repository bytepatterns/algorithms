"""
House Robber in a Circle: First and last are now neighbours, so run the line twice.

On a circle the only new rule is that the first and last houses touch.
Rather than invent a recurrence for it, forbid one of them: solve the line
without the last house, solve it again without the first, and keep the
better. Every legal circular plan misses at least one end, so one of those
two runs contains it.

Lesson 14 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/house-robber-circle

Run it:  python dynamic-programming/14-house-robber-circle.py
"""


def rob_line(vals):
    take, skip = 0, 0
    for v in vals:
        take, skip = skip + v, max(skip, take)   # take v, or keep the best so far
    return max(take, skip)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]

    check(rob_line(houses), 12)  # on a line
    check(max(rob_line(houses[:-1]), rob_line(houses[1:])), 11)  # on a circle
