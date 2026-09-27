"""
Container With Most Water: The shorter wall decides. So move the shorter wall.

Given a row of wall heights, the water between two walls is the width times
the shorter height. Start at the widest pair and always move the shorter
wall inward. Moving the taller one can only lose area, so skipping it is
safe.

Lesson 7 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/container-with-most-water

Run it:  python arrays/07-container-with-most-water.py
"""


def max_area(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))
        if height[left] < height[right]:
            left += 1        # only the shorter wall can help
        else:
            right -= 1
    return best


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
