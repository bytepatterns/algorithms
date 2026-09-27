"""
Top K Without a Heap: Counts are small integers, so index by them.

A heap gives you the top k in O(n log k). But a count can never be larger
than the array itself, so counts make perfectly good array indices:
buckets[c] holds every value seen exactly c times. Tally with a map, drop
each value into its count bucket, then walk the buckets downwards and take
until you have k. Linear, and nothing is compared with anything.

Lesson 7 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/top-k-buckets

Run it:  python hash-tables/07-top-k-buckets.py
"""


def top_k(nums, k):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]   # index = how often
    for value, c in counts.items():
        buckets[c].append(value)
    out = []
    for c in range(len(nums), 0, -1):              # walk down from the top
        out += buckets[c]
        if len(out) >= k:
            return out[:k]
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(top_k([1, 1, 1, 2, 2, 3], 2), [1, 2])
