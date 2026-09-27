"""
Repeated DNA Sequences (medium) · patterns: rolling-hash, hash-set

A DNA strand is a string over the letters A, C, G and T. Return every
length-10 substring that occurs more than once in the strand, sorted, with
each such substring listed only once no matter how often it repeats.

Examples:

    Input:  dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    Output: ["AAAAACCCCC", "CCCCCAAAAA"]
    Why:    both windows appear twice inside the strand

    Input:  dna = "AAAAAAAAAAAA"
    Output: ["AAAAAAAAAA"]
    Why:    the same window slides along and repeats

    Input:  dna = "ACGT"
    Output: []
    Why:    edge case, the strand is shorter than one window

Approach:
    Two bits per letter turn a ten-letter window into a twenty-bit integer,
    so the whole window is one machine word rather than a string. Sliding is
    then three constant-time operations — shift in the arriving letter, mask
    out the departing one — instead of a fresh ten-character slice. A set of
    seen window values catches repeats, and a second set keeps the answer
    free of duplicates. Time is O(n) and space is O(n) in the number of
    distinct windows.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/strings/repeated-dna-sequences

Run it:  python problems/strings/07-repeated-dna-sequences.py
"""


def repeated(dna, k=10):
    seen, twice = set(), set()
    code = {"A": 0, "C": 1, "G": 2, "T": 3}
    h, mask = 0, (1 << (2 * k)) - 1
    for i, ch in enumerate(dna):
        h = ((h << 2) | code[ch]) & mask          # shift in, mask out
        if i >= k - 1:
            if h in seen:
                twice.add(dna[i - k + 1:i + 1])   # slice only on a hit
            seen.add(h)
    return sorted(twice)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(repeated("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ['AAAAACCCCC', 'CCCCCAAAAA'])
    check(repeated("AAAAAAAAAAAA"), ['AAAAAAAAAA'])
    check(repeated("ACGT"), [])
