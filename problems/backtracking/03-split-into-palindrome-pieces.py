"""
Split Into Palindromes (medium) · patterns: backtracking, pruning

Cut a string into pieces so that every piece reads the same forwards and
backwards. Return every way of doing that, with each way given as the list
of pieces in order. Single characters count as palindromes, so at least one
cutting always exists.

Examples:

    Input:  s = "aab"
    Output: [["a", "a", "b"], ["aa", "b"]]
    Why:    "ab" is not a palindrome, so no cutting starts with it

    Input:  s = "aaa"
    Output: 4 cuttings
    Why:    "a|a|a", "aa|a", "a|aa" and "aaa" all qualify

    Input:  s = "a"
    Output: [["a"]]
    Why:    edge case, a single character is already a palindrome

Approach:
    The start index is the whole state: everything before it is already cut,
    everything from it onwards is a smaller copy of the same problem. Each
    branch is a candidate next piece, and the palindrome test rejects a
    branch before any recursion happens underneath it, which is what keeps
    the search away from most of the two to the n-1 possible cuttings.
    Reaching the end of the string means the path is complete, so it is
    copied out. Worst case, on a string of identical characters, time is O(n
    times 2 to the n).

The lesson behind it: Word Search & Pruning
    https://bytepatterns.com/learn/backtracking/word-search-and-pruning
    python backtracking/05-word-search-and-pruning.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/backtracking/split-into-palindrome-pieces

Run it:  python problems/backtracking/03-split-into-palindrome-pieces.py
"""


def palindrome_splits(s):
    out = []
    def build(start, path):
        if start == len(s):              # the whole string is cut up
            out.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece != piece[::-1]:     # not a palindrome: prune the branch
                continue
            path.append(piece)           # choose
            build(end, path)             # explore
            path.pop()                   # un-choose
    build(0, [])
    return out


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(palindrome_splits("aab"), [['a', 'a', 'b'], ['aa', 'b']])
    check(len(palindrome_splits("aaa")), 4)
    check(palindrome_splits("a"), [['a']])
