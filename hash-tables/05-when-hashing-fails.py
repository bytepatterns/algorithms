"""
When Hashing Fails: O(1) is an average, not a promise.

Two keys can land in one bucket. Real tables absorb that by chaining or
probing, and the average stays O(1). But a hash function that crowds keys
into a few buckets drags lookups toward O(n). Keys must also be immutable:
mutate a key after insertion and its hash stops pointing where it lives.

Lesson 5 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/when-hashing-fails

Run it:  python hash-tables/05-when-hashing-fails.py
"""


def bad_bucket(key, n):
    return len(key) % n          # clusters hard: most names are short


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    names = ["ana", "bob", "cal", "dee"]
    check([bad_bucket(x, 8) for x in names], [3, 3, 3, 3])  # one bucket

    point = [1, 2]
    try:
        seats = {point: "aisle"}     # keys must be hashable
    except TypeError:
        print("unhashable:", type(point).__name__)   # unhashable: list

    check({tuple(point): "aisle"}, {(1, 2): 'aisle'})  # tuples work
