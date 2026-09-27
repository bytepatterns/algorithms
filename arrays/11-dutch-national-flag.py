"""
Dutch National Flag: Three values, three regions, one pass.

With only three distinct values, sorting is really partitioning. Hold three
walls: everything before low is the small value, everything after high is
the large one, and the stretch from i to high is still unseen. Read the
value at i and push it to the wall it belongs behind. A swap with high pulls
in a value nobody has looked at, so the cursor must stay put for one more
read.

Lesson 11 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/dutch-national-flag

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python arrays/11-dutch-national-flag.py
"""


def sort_colors(nums):
    low, i, high = 0, 0, len(nums) - 1
    while i <= high:
        if nums[i] == 0:                        # belongs in the front block
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
            i += 1
        elif nums[i] == 2:                      # belongs in the back block
            nums[high], nums[i] = nums[i], nums[high]
            high -= 1                           # i stays: that value is unseen
        else:
            i += 1
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(sort_colors([2, 0, 1, 2, 0]), [0, 0, 1, 2, 2])
