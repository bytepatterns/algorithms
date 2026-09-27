"""
Heap Sort: Build a heap, then peel the maximum off n times.

Read the array as a binary heap: index i has children 2i+1 and 2i+2. Sift
every non-leaf down and the largest value ends up at index 0. Swap it with
the last slot — that value is now final — shrink the heap by one and sift
the new root down. Repeat and the array sorts itself, O(n log n) in the
worst case, with no second array anywhere.

Lesson 9 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/heap-sort

Run it:  python sorting/09-heap-sort.py
"""


def sift_down(a, i, size):
    while 2 * i + 1 < size:
        big = 2 * i + 1
        if big + 1 < size and a[big + 1] > a[big]:
            big += 1                    # take the larger child
        if a[i] >= a[big]:
            break
        a[i], a[big] = a[big], a[i]
        i = big

def heap_sort(a):
    for i in range(len(a) // 2 - 1, -1, -1):   # build the max-heap
        sift_down(a, i, len(a))
    for end in range(len(a) - 1, 0, -1):       # peel the max off the top
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)
    return a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(heap_sort([4, 10, 3, 5, 1]), [1, 3, 4, 5, 10])
