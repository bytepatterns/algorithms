"""
Chess Board Model: The piece owns its shape; the board owns who is standing where.

Cut the question in two. A piece answers only about geometry — is this
offset shaped like my move? The board answers about occupancy — is the path
clear, is the target one of mine, is it my turn?

Neither object needs the other's data, so a new piece is a new class and
nothing else.

Lesson 15 of Low-Level Design, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/lld/chess-board-model

Run it:  python lld/15-chess-board-model.py
"""


class Rook:
    def shape_ok(self, a, b): return a[0] == b[0] or a[1] == b[1]

class Knight:
    def shape_ok(self, a, b):
        return sorted((abs(a[0] - b[0]), abs(a[1] - b[1]))) == [1, 2]

class Board:
    def __init__(self, pieces): self.pieces = pieces      # square -> piece
    def legal(self, a, b):                                # geometry, then state
        piece = self.pieces.get(a)
        return bool(piece) and piece.shape_ok(a, b) and b not in self.pieces


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

import re


def _same(printed, expected):
    """Printed text vs the lesson's comment, which may add a note after it."""
    printed, expected = printed.strip(), expected.strip()
    wants = [expected] + [expected.rsplit(s, 1)[1].strip() for s in (" -> ", " = ") if s in expected]
    for want in wants + [w[1:] for w in wants if w.startswith("~")]:
        rest = want[len(printed):] if want.startswith(printed) else None
        if rest == "" or (rest and re.match(r"[\s,;:]+([A-Za-z]|\u2014|\u2013|-(?!\d)|\u2192|<-|\([A-Za-z]|#)", rest)):
            return True
    return False


def check_printed(*values, expect, sep=" ", end="\n"):
    """print(*values), then assert the line reads the way the lesson's comment says."""
    print(*values, sep=sep, end=end)
    forms = [sep.join(map(str, values))]
    if len(values) == 1 and isinstance(values[0], str):
        forms += [repr(values[0]), '"%s"' % values[0]] + (["(empty string)"] if not values[0] else [])
    if len(values) > 1 and isinstance(values[0], str):  # a leading label
        forms.append(sep.join(map(str, values[1:])))
    assert any(_same(f, expect) for f in forms), f"expected {expect!r}, got {forms[0]!r}"


if __name__ == "__main__":
    b = Board({(0, 0): Rook(), (1, 0): Knight()})
    check_printed(b.legal((0, 0), (0, 5)), b.legal((1, 0), (2, 2)), b.legal((0, 0), (1, 0)), expect="True True False")
