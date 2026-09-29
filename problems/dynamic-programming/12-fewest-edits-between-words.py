"""
Fewest Edits Between Words (medium) · patterns: string-dp, bottom-up-dp

A spell checker scores how far a typed word is from a dictionary word. One
edit inserts a character, deletes a character, or replaces one character
with another. Given two strings a and b, return the smallest number of edits
that turns a into b. Either string may be empty.

Examples:

    Input:  a = "carpet", b = "parrot"
    Output: 3
    Why:    replace c with p, the second p with r, and e with o

    Input:  a = "stone", b = "notes"
    Output: 4
    Why:    the shared letters are in a different order, so few can be kept

    Input:  a = "", b = "abc"
    Output: 3
    Why:    edge case, three inserts

Approach:
    Let cell i, j be the fewest edits that turn the first i characters of a
    into the first j characters of b. When those last characters match they
    can be kept for free, so the cell equals the diagonal one. Otherwise the
    last move is a replace (diagonal), a delete from a (the cell above) or
    an insert of b's character (the cell to the left), each costing one.
    Only the previous row is needed at any time, so two rows replace the
    full table. Time is O(len(a) times len(b)), and space is O(len(b)).

The lesson behind it: Edit Distance
    https://bytepatterns.com/learn/dynamic-programming/edit-distance
    python dynamic-programming/08-edit-distance.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/dynamic-programming/fewest-edits-between-words

Run it:  python problems/dynamic-programming/12-fewest-edits-between-words.py
"""


def edit_distance(a, b):
    prev = list(range(len(b) + 1))       # turning "" into each prefix of b
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)         # turning a's prefix into "" takes i deletes
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                cur[j] = prev[j - 1]     # matching last letters cost nothing
            else:                        # replace, delete, insert
                cur[j] = 1 + min(prev[j - 1], prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(edit_distance("carpet", "parrot"), 3)
    check(edit_distance("stone", "notes"), 4)
    check(edit_distance("", "abc"), 3)
