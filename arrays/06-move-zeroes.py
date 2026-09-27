"""
Move Zeroes: Push the junk to the back without losing the order.

Keep a write pointer for the next slot that should hold a non-zero value.
Scan with a read pointer and copy every non-zero forward. Then pad the tail
with zeros: one pass, no second array, order preserved.

Lesson 6 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/move-zeroes

Run it:  python arrays/06-move-zeroes.py
"""


def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]   # keeps relative order
            write += 1
    while write < len(nums):
        nums[write] = 0                # pad the tail
        write += 1
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(move_zeroes([0, 4, 0, 9, 2]), [4, 9, 2, 0, 0])
