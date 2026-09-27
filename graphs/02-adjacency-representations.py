"""
List vs Matrix: Store the edges you have, or a cell for every pair you don't.

Two ways to store the same graph. An adjacency list keeps, per node, only
the neighbours it actually has — small when edges are scarce. An adjacency
matrix reserves a cell for every possible pair, so "is A joined to B?" is
one lookup, but blanks dominate.

Lesson 2 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/adjacency-representations

Run it:  python graphs/02-adjacency-representations.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    players = ["GK", "DF", "MF", "FW"]
    passes = [("GK", "DF"), ("DF", "MF"), ("MF", "FW"), ("MF", "DF")]

    adj = {p: [] for p in players}          # adjacency list
    for a, b in passes:
        adj[a].append(b)                    # directed: a passed to b

    idx = {p: i for i, p in enumerate(players)}
    mat = [[0] * len(players) for _ in players]   # adjacency matrix
    for a, b in passes:
        mat[idx[a]][idx[b]] = 1

    check(adj["MF"], ['FW', 'DF'])
    check(mat[idx["MF"]], [0, 1, 0, 1])
