"""
Two Colour Split Check (medium) · patterns: bfs, graph-colouring

An undirected graph is given as a neighbour list, where entry i holds the
nodes joined to node i. Decide whether the nodes can be split into two
groups so that every edge joins a node in one group to a node in the other.
The graph may be disconnected, so every part has to be checked.

Examples:

    Input:  adj = [[1, 3], [0, 2], [1, 3], [0, 2]]
    Output: True
    Why:    the four-node ring alternates between the two groups

    Input:  adj = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    Output: False
    Why:    nodes 0, 1 and 2 form a triangle, and a triangle cannot alternate

    Input:  adj = [[]]
    Output: True
    Why:    edge case, a lone node with no edges satisfies the rule

Approach:
    Choosing a colour for one node forces the colour of everything reachable
    from it, so a traversal that paints each neighbour the opposite colour
    explores the only possible assignment for that component. A
    contradiction can only appear as an edge whose ends share a colour,
    which is checked as each edge is crossed. Restarting from every
    uncoloured node handles disconnected graphs, since each component gets
    its own free first choice. Time is O(V + E) and space is O(V).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/two-colour-split-check

Run it:  python problems/graphs/07-two-colour-split-check.py
"""


from collections import deque
def is_two_colourable(adj):
    colour = [0] * len(adj)          # 0 means unassigned, 1 and -1 are the groups
    for start in range(len(adj)):
        if colour[start]:
            continue                 # this component was already painted
        colour[start] = 1            # the first choice in a component is free
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for nb in adj[node]:
                if colour[nb] == colour[node]:
                    return False     # an edge inside one group
                if colour[nb] == 0:
                    colour[nb] = -colour[node]
                    queue.append(nb)
    return True


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(is_two_colourable([[1, 3], [0, 2], [1, 3], [0, 2]]), True)
    check(is_two_colourable([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]), False)
    check(is_two_colourable([[]]), True)
