"""
Graphs You Never Build: Generate the neighbours on demand and BFS works the same.

A graph does not have to exist in memory. If a rule tells you which states
follow a state, BFS can walk it exactly as before: pop a state, generate its
neighbours, keep the unseen ones. Word ladders, puzzle boards and lock
combinations are all graphs that are cheaper to compute than to store.

Lesson 14 of Graphs, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/graphs/implicit-graph-bfs

Run it:  python graphs/14-implicit-graph-bfs.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    from collections import deque
    words = {"cold", "cord", "card", "ward", "warm", "wolf"}

    q = deque([("cold", 1)])
    seen = {"cold"}
    steps = 0
    while q:
        word, d = q.popleft()
        if word == "warm":
            steps = d
            break
        for i in range(len(word)):                       # neighbours are computed,
            for ch in "abcdefghijklmnopqrstuvwxyz":      # never stored
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in words and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))

    check(steps, 5)  # cold, cord, card, ward, warm
