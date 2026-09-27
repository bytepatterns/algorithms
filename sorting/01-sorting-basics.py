"""
Sorting Basics: Comparisons, swaps, stability: the vocabulary of order.

Every comparison sort works by comparing pairs and rearranging them. Judge
one on three things: time, extra memory, and stability. A stable sort keeps
equal items in the order they arrived.

Lesson 1 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/sorting-basics

Run it:  python sorting/01-sorting-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    people = [("Ada", "Rome"), ("Bo", "Lima"), ("Cy", "Rome")]

    # Python's sort is stable: equal keys keep their original order
    by_city = sorted(people, key=lambda p: p[1])
    check(by_city, [('Bo', 'Lima'), ('Ada', 'Rome'), ('Cy', 'Rome')])
    # Ada still comes before Cy, exactly as in the input.

    nums = [5, 1, 4]
    nums.sort()          # sorts in place, O(n log n)
    check(nums, [1, 4, 5])
