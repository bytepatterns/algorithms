"""
Hash Table Basics: Turn a key into an address and skip the search.

A hash table runs each key through a hash function that returns a bucket
number. Storing and looking up both jump straight to that bucket, so the
average cost stays O(1) however many keys are inside. The price: keys must
be hashable, and order is never promised.

Lesson 1 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/hash-table-basics

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python hash-tables/01-hash-table-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    stock = {}                       # an empty hash table

    stock["SKU-118"] = 42            # hash the key -> bucket -> store
    stock["SKU-903"] = 7

    check(stock["SKU-118"], 42)  # average O(1)
    check("SKU-903" in stock, True)  # also O(1)

    stock["SKU-118"] += 1            # read and write, still O(1)
    check(stock.get("SKU-000", 0), 0)  # safe default, no crash
    check(len(stock), 2)  # count is stored
