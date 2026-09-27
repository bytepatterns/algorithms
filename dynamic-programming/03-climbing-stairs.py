"""
Climbing Stairs: Ways to reach step n = ways to n-1 plus ways to n-2.

You may step up one stair or two. To be standing on step n you must have
arrived from step n-1 or from step n-2, so the ways to reach n are those two
counts added together. That is Fibonacci wearing a different hat, and
because nothing older is ever read, two rolling variables replace the entire
table.

Lesson 3 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/climbing-stairs

Run it:  python dynamic-programming/03-climbing-stairs.py
"""


def climb(n):
    a, b = 1, 1                  # ways to reach step 0 and step 1
    for _ in range(2, n + 1):
        a, b = b, a + b          # slide the window forward one step
    return b


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(climb(5), 8)
    check(climb(10), 89)
