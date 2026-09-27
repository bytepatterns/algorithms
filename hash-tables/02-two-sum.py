"""
Two Sum: Remember what you have seen and the pair finds itself.

Comparing every pair costs O(n²). Instead, walk the list once and ask a map
of seen values one question: has the complement — target minus this value —
already gone past? A hash lookup answers instantly, so a single pass settles
it.

Lesson 2 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/two-sum

Run it:  python hash-tables/02-two-sum.py
"""


def two_sum(nums, target):
    seen = {}                    # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:         # the partner already went past
            return (seen[need], i)
        seen[x] = i              # remember x for whoever needs it
    return None


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(two_sum([90, 40, 200, 150], 240), (1, 2))  # 40 + 200
    check(two_sum([5, 5], 10), (0, 1))
