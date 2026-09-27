"""
Rabin-Karp Rolling Hash: Slide a number across the text instead of re-reading it.

Comparing a pattern against every position re-reads the same characters over
and over. Instead, turn each window into one number.

When the window slides, subtract the character leaving, shift the rest up a
digit, and add the character arriving. Equal hashes then need one cheap
check to confirm.

Lesson 6 of Strings, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/strings/rabin-karp-rolling-hash

Run it:  python strings/06-rabin-karp-rolling-hash.py
"""


def find(text, pat, base=26, mod=101):
    m, high = len(pat), pow(base, len(pat) - 1, mod)
    want = cur = 0
    for i in range(m):                 # hash the pattern and window 0
        want = (want * base + ord(pat[i]) - 97) % mod
        cur = (cur * base + ord(text[i]) - 97) % mod
    for i in range(len(text) - m + 1):
        if cur == want and text[i:i + m] == pat:   # hashes can collide
            return i
        if i + m < len(text):          # roll one step to the right
            cur = (cur - (ord(text[i]) - 97) * high) % mod
            cur = (cur * base + ord(text[i + m]) - 97) % mod
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find("abcabd", "abd"), 3)
