"""
Heapify and Sift: One wrong value walks a single path back into place.

Fixing a heap never touches the whole array. A value that is too big sinks
toward the leaves, swapping with its smaller child; a value that is too
small rises toward the root. Either way it walks one path — at most log n
swaps.

To build a heap from a raw pile, sift down starting at the last parent and
work backward. That is O(n), because most nodes are already near the bottom.

Lesson 2 of Heaps, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/heaps/heapify-and-sift

Run it:  python heaps/02-heapify-and-sift.py
"""


def sift_down(h, i):
    n = len(h)
    while 2 * i + 1 < n:                  # while a left child exists
        c = 2 * i + 1
        if c + 1 < n and h[c + 1] < h[c]:
            c += 1                        # take the smaller child
        if h[i] <= h[c]:
            break                         # parent already beats both
        h[i], h[c] = h[c], h[i]
        i = c                             # follow the value down


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    pile = [9, 4, 7, 1, 3]
    for i in range(len(pile) // 2 - 1, -1, -1):
        sift_down(pile, i)                    # last parent first, O(n) total
    check(pile, [1, 3, 7, 4, 9])
