"""
Split String Into Blocks (medium) · patterns: greedy, last-occurrence

Cut a lowercase string into as many pieces as possible so that every letter
appears in at most one piece. Joining the pieces back together must rebuild
the original string exactly. Return the length of each piece, in order.

Examples:

    Input:  s = "abacdc"
    Output: [3, 3]
    Why:    "aba" holds every a and b, "cdc" holds every c and d

    Input:  s = "abcabc"
    Output: [6]
    Why:    every letter reappears late, so no cut is legal

    Input:  s = "xyz"
    Output: [1, 1, 1]
    Why:    edge case, no letter repeats so every character is its own piece

Approach:
    Record each letter's last index in a first pass. Then sweep once,
    stretching a running boundary to the last index of every letter met
    since the previous cut. Reaching that boundary means every letter inside
    the piece is finished, so cutting here is legal — and cutting at the
    first legal point is what maximises the number of pieces, since waiting
    longer only merges two pieces into one. Both passes are linear, so time
    is O(n) and space is O(1) for the fixed 26-letter map.

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/split-string-into-blocks

Run it:  python problems/greedy/03-split-string-into-blocks.py
"""


def block_sizes(s):
    last = {ch: i for i, ch in enumerate(s)}   # final index of each letter
    sizes, start, end = [], 0, 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])               # the piece cannot close before this
        if i == end:                           # every letter inside is finished
            sizes.append(i - start + 1)
            start = i + 1
    return sizes


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(block_sizes("abacdc"), [3, 3])
    check(block_sizes("abcabc"), [6])
    check(block_sizes("xyz"), [1, 1, 1])
