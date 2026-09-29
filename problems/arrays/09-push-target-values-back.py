"""
Push Target Values Back (easy) · patterns: two-pointers, write-pointer

A playlist editor wants every copy of one song id moved to the end of the
queue without shuffling anything else. Given a list nums and a value v,
rearrange the list in place so that the elements different from v keep their
original relative order at the front and every copy of v sits at the back.
Return the same list object, and use only a constant amount of extra memory.

Examples:

    Input:  nums = [4, 0, 7, 0, 2], v = 0
    Output: [4, 7, 2, 0, 0]
    Why:    4, 7 and 2 stay in the order they arrived

    Input:  nums = [3, 1, 3, 3, 5], v = 3
    Output: [1, 5, 3, 3, 3]
    Why:    three copies of 3 collect at the back

    Input:  nums = [], v = 9
    Output: []
    Why:    edge case, there is nothing to move

Approach:
    The write index only moves when a keeper is copied, so it never
    overtakes the reader and no keeper is overwritten before it has been
    read. Copying in reading order preserves the relative order of the
    keepers for free. Every slot after the last keeper must hold a copy of
    v, because the number of copies equals the number of slots left over.
    Time is O(n) with one pass plus the fill, and space is O(1).

The lesson behind it: Move Zeroes
    https://bytepatterns.com/learn/arrays/move-zeroes
    python arrays/06-move-zeroes.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/arrays/push-target-values-back

Run it:  python problems/arrays/09-push-target-values-back.py
"""


def push_back(nums, v):
    write = 0                        # slot for the next value we keep in front
    for x in nums:
        if x != v:
            nums[write] = x          # copy forward, order is preserved
            write += 1
    for i in range(write, len(nums)):
        nums[i] = v                  # the leftover slots belong to v
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(push_back([4, 0, 7, 0, 2], 0), [4, 7, 2, 0, 0])
    check(push_back([3, 1, 3, 3, 5], 3), [1, 5, 3, 3, 3])
    check(push_back([], 9), [])
