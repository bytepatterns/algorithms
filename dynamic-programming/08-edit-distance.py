"""
Edit Distance: Insert, delete, or replace — count the cheapest route.

Turn one string into another with inserts, deletes, and replacements,
counting the cheapest sequence. Every grid cell asks what the three slightly
shorter problems cost. Matching characters are free and copy the diagonal; a
mismatch pays one on top of whichever of the three neighbours is cheapest.
Only the previous row is ever needed.

Lesson 8 of Dynamic Programming, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/dynamic-programming/edit-distance

Run it:  python dynamic-programming/08-edit-distance.py
"""


def edit(a, b):
    row = list(range(len(b) + 1))                 # cost of building b's prefixes from ""
    for i in range(1, len(a) + 1):
        new = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            new[j] = min(row[j] + 1,              # delete
                         new[j - 1] + 1,          # insert
                         row[j - 1] + cost)       # match or replace
        row = new
    return row[len(b)]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(edit("kitten", "sitting"), 3)
    check(edit("flaw", "lawn"), 2)
