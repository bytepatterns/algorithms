"""
Group Anagrams: Give every item a canonical key, then bucket by it.

Two words are anagrams when their letters match and only the order differs.
So give each word a canonical signature — its letters sorted — and use that
signature as a dictionary key. Words sharing a signature drop into the same
bucket, and no two words are ever compared directly.

Lesson 4 of Hash Tables, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/hash-tables/group-anagrams

Run it:  python hash-tables/04-group-anagrams.py
"""


def group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))              # canonical signature
        groups.setdefault(key, []).append(w)  # bucket by signature
    return list(groups.values())


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(group_anagrams(["listen", "silent", "enlist", "google"]), [['listen', 'silent', 'enlist'], ['google']])
