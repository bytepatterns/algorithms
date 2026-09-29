"""
Disc Tower Moves (medium) · patterns: recursion, divide-and-conquer

Three pegs are named A, B and C. Peg A holds n discs of different sizes,
largest at the bottom. Move the whole stack to peg C, one disc at a time,
never placing a larger disc on a smaller one. Return the moves in order,
each written as the peg moved from and the peg moved to.

Examples:

    Input:  n = 1, src = "A", dst = "C", spare = "B"
    Output: [("A", "C")]
    Why:    a single disc goes straight across

    Input:  n = 2, src = "A", dst = "C", spare = "B"
    Output: [("A", "B"), ("A", "C"), ("B", "C")]
    Why:    park the small disc on the spare peg, move the big one, put it back

    Input:  n = 0, src = "A", dst = "C", spare = "B"
    Output: []
    Why:    edge case, an empty stack needs no moves

Approach:
    The largest disc can only move when every smaller disc is out of the way
    on the spare peg, so the problem splits into two copies of itself around
    a single move. The recursion writes itself once the roles are named:
    destination and spare trade places in the first call and source and
    spare trade places in the second. The base case is an empty stack, which
    needs no moves. The move count doubles with each disc plus one, so time
    is O(2 to the n) and the stack depth is O(n).

The lesson behind it: The Call Stack
    https://bytepatterns.com/learn/recursion/call-stack-visualized
    python recursion/02-call-stack-visualized.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/disc-tower-moves

Run it:  python problems/recursion/02-disc-tower-moves.py
"""


def moves(n, src, dst, spare):
    if n == 0:
        return []                              # nothing left to move
    above = moves(n - 1, src, spare, dst)      # clear the smaller discs first
    return above + [(src, dst)] + moves(n - 1, spare, dst, src)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(moves(1, "A", "C", "B"), [('A', 'C')])
    check(moves(2, "A", "C", "B"), [('A', 'B'), ('A', 'C'), ('B', 'C')])
    check(len(moves(3, "A", "C", "B")), 7)
