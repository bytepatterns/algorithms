"""
Merge Sorted Arrays: Fill from the back and you never overwrite unread data.

Merging two sorted arrays into a third one is easy. Merging into the first
one is where it bites: writing at the front tramples values you still need
to read. So write from the back. The larger of the two tails takes the last
free slot, and that slot always sits past everything still unread. No
shifting, no second array, one pass.

Lesson 10 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/merge-sorted-arrays

Run it:  python arrays/10-merge-sorted-arrays.py
"""


def merge(a, m, b, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        # the bigger tail takes the last free slot
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1
    return a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(merge([1, 4, 7, 0, 0], 3, [3, 5], 2), [1, 3, 4, 5, 7])
