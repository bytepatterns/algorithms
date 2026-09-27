"""
Top K in a Stream: Count once, then let a k-sized heap keep only the winners.

Ranking everything is wasted work when you only want k. Count first, then
walk the distinct items through a min-heap capped at k.

The root is the weakest item still held. Anything that beats it takes its
place; anything that does not is dropped and never looked at again.

Lesson 3 of Two Heaps & K-Way Merge, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/two-heaps-k-way/top-k-frequent-stream

Run it:  python two-heaps-k-way/03-top-k-frequent-stream.py
"""


import heapq
from collections import Counter

def top_k_frequent(items, k):
    counts = Counter(items)             # pass one: how often each appears
    keep = []                           # min-heap of (count, item), size k
    for item, n in counts.items():
        heapq.heappush(keep, (n, item))
        if len(keep) > k:               # over budget: evict the weakest
            heapq.heappop(keep)
    return [item for n, item in sorted(keep, reverse=True)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(top_k_frequent(["ux", "db", "ux", "api", "db", "ux"], 2), ['ux', 'db'])
    check(top_k_frequent(["a"], 3), ['a'])
