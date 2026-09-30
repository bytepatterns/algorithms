"""
Legal Moves That Keep the King Safe (hard) · patterns: board-model, move-generation, check-detection

Model a chess board with kings, queens, rooks, bishops and knights (no
pawns, no castling). A position is a dict from square to piece, such as
{"e1": "K", "e8": "r"}, with white pieces in upper case and black in lower
case. Write analyse(position, white) for the side to move. A move is legal
if the piece can reach the square, sliding pieces stop at the first occupied
square and may capture it only if it holds an enemy, and afterwards the
mover's own king is not attacked. Return the state, "checkmate",
"stalemate", "check" or "play", together with the sorted legal moves written
as from-square plus to-square, like "e2e4".

Examples:

    Input:  {"h8": "k", "g7": "Q", "f6": "K"}, black to move
    Output: ('checkmate', [])
    Why:    the queen attacks every square around the king and the white king guards the queen

    Input:  {"a8": "k", "b6": "Q", "c1": "K"}, black to move
    Output: ('stalemate', [])
    Why:    the king is not attacked, but every square it could step to is

    Input:  {"e1": "K", "e8": "r", "b4": "b", "c3": "N", "h8": "k"}, white to move
    Output: ('check', ['e1d1', 'e1d2', 'e1f1', 'e1f2'])
    Why:    edge case, the knight could block on e2 or e4, but the bishop pins it to the king

Approach:
    The design splits the board into data and two small rules. The data is a
    dict from (file, rank) to piece, and a table of directions per piece
    kind, with one flag for whether the piece slides or steps. The first
    rule, reach, walks those directions and stops at the board edge or the
    first piece, keeping the square only if it is empty or holds an enemy;
    the same function answers both where a piece may move and what it
    attacks, so the two can never disagree. The second rule checks legality
    the robust way: make the move on a copy and ask whether the mover's king
    is attacked, which handles pins, moving into check and capturing the
    checker without a special case for each, as the pinned knight in the
    third example shows. The state follows from whether any move survived
    and whether the king is attacked now. With P pieces and up to 27
    reachable squares each, one position costs O(P² × 27²) reach calls in
    the worst case, which is small on an 8 × 8 board, and space is O(P) per
    board copy.

The lesson behind it: Chess Board Model
    https://bytepatterns.com/learn/lld/chess-board-model
    python lld/15-chess-board-model.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/legal-moves-that-keep-the-king-safe

Run it:  python problems/lld/08-legal-moves-that-keep-the-king-safe.py
"""


LINES = {"R": [(1, 0), (-1, 0), (0, 1), (0, -1)], "B": [(1, 1), (1, -1), (-1, 1), (-1, -1)]}
LINES["Q"] = LINES["R"] + LINES["B"]                 # sliding pieces
STEPS = {"N": [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)],
         "K": LINES["Q"]}                            # one-step pieces

def reach(board, sq):
    f, r = sq
    white, kind = board[sq].isupper(), board[sq].upper()
    out = []
    for df, dr in LINES.get(kind) or STEPS[kind]:
        x, y = f + df, r + dr
        while 0 <= x < 8 and 0 <= y < 8:
            other = board.get((x, y))
            if other is None or other.isupper() != white:
                out.append((x, y))                   # empty, or an enemy to capture
            if other is not None or kind in STEPS:
                break                                # blocked, or a one-step piece
            x, y = x + df, y + dr
    return out

def attacked(board, sq, by_white):
    return any(p.isupper() == by_white and sq in reach(board, s) for s, p in board.items())

def analyse(position, white):
    board = {(ord(s[0]) - 97, int(s[1]) - 1): p for s, p in position.items()}
    name = lambda sq: chr(97 + sq[0]) + str(sq[1] + 1)
    king = "K" if white else "k"
    moves = []
    for sq, piece in list(board.items()):
        if piece.isupper() != white:
            continue
        for to in reach(board, sq):
            nxt = dict(board)
            nxt[to] = nxt.pop(sq)                    # try the move on a copy
            home = next(s for s, p in nxt.items() if p == king)
            if not attacked(nxt, home, not white):
                moves.append(name(sq) + name(to))
    home = next(s for s, p in board.items() if p == king)
    check = attacked(board, home, not white)
    if moves:
        return ("check" if check else "play"), sorted(moves)
    return ("checkmate" if check else "stalemate"), []


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(analyse({"h8": "k", "g7": "Q", "f6": "K"}, white=False), ('checkmate', []))
    check(analyse({"a8": "k", "b6": "Q", "c1": "K"}, white=False), ('stalemate', []))
    check(analyse({"e1": "K", "e8": "r", "b4": "b", "c3": "N", "h8": "k"}, white=True), ('check', ['e1d1', 'e1d2', 'e1f1', 'e1f2']))
    check(analyse({"e1": "K", "e2": "R", "e8": "r", "a8": "k"}, white=True), ('play', ['e1d1', 'e1d2', 'e1f1', 'e1f2', 'e2e3', 'e2e4', 'e2e5', 'e2e6', 'e2e7', 'e2e8']))
