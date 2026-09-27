"""
Radix Sort: Sort by the last digit first, and never compare a thing.

Radix sort is counting sort run once per digit, starting from the least
significant one. Each pass drops every number into one of ten buckets and
collects them back in bucket order. Because a pass is stable, numbers that
tie on the current digit keep the order the previous pass gave them — which
is exactly why starting from the right works. Cost is d passes over n
numbers, with no comparisons at all.

Lesson 10 of Sorting, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/sorting/radix-sort

Run it:  python sorting/10-radix-sort.py
"""


def radix_sort(nums):
    place = 1
    while place <= max(nums):
        buckets = [[] for _ in range(10)]
        for x in nums:
            buckets[(x // place) % 10].append(x)   # ties keep their order
        nums = [x for b in buckets for x in b]     # collect 0..9 in order
        place *= 10
    return nums


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(radix_sort([170, 45, 75, 90, 2, 802]), [2, 45, 75, 90, 170, 802])
