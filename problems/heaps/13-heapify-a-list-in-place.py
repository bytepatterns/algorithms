"""
Heapify a List in Place (easy) · patterns: heapify, sift-down

Rearrange a list of numbers into a min-heap in place, without the heapq
module, and return it. In a min-heap stored in a list, the children of index
i are at 2i + 1 and 2i + 2, and every parent is at most each of its
children. Use the bottom-up method: sift each parent down, starting from the
last parent and moving towards the root, so the whole build runs in O(n).

Examples:

    Input:  nums = [5, 3, 8, 1, 2]
    Output: [1, 2, 8, 3, 5]
    Why:    3 swaps with its child 1, then 5 sinks from the root past 1 and 2

    Input:  nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Output: [1, 2, 3, 6, 5, 4, 7, 8, 9]

    Input:  nums = [42]
    Output: [42]
    Why:    edge case, one element is already a heap

Approach:
    Bottom-up heapify treats the list as a tree and repairs it from the
    lowest parents upwards. Sift down only works when both subtrees of a
    node are already heaps, and processing indices from n // 2 - 1 down to 0
    guarantees that, because every child has a larger index and was handled
    first. Each sift down swaps the node with its smaller child until
    neither child is smaller, which restores the heap order in that subtree.
    Pushing the values one by one would cost O(n log n), but here most nodes
    sit near the bottom and can only sink a level or two: the total work
    sums to O(n). Space is O(1) because everything happens inside the list.

The lesson behind it: Heapify and Sift
    https://bytepatterns.com/learn/heaps/heapify-and-sift
    python heaps/02-heapify-and-sift.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/heaps/heapify-a-list-in-place

Run it:  python problems/heaps/13-heapify-a-list-in-place.py
"""


def sift_down(a, i, n):
    while True:
        smallest, left, right = i, 2 * i + 1, 2 * i + 2
        if left < n and a[left] < a[smallest]:
            smallest = left
        if right < n and a[right] < a[smallest]:
            smallest = right
        if smallest == i:                     # both children are larger: done
            return
        a[i], a[smallest] = a[smallest], a[i]
        i = smallest                          # follow the value down

def heapify(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):       # last parent back to the root
        sift_down(a, i, n)
    return a


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(heapify([5, 3, 8, 1, 2]), [1, 2, 8, 3, 5])
    check(heapify([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 6, 5, 4, 7, 8, 9])
    check(heapify([42]), [42])
