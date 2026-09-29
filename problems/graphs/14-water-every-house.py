"""
Water Every House (hard) · patterns: prim, virtual-node

A village has n houses numbered 1 to n. House i can get water from a well of
its own at cost wells[i - 1], or through pipes: a pipe [a, b, c] joins
houses a and b in both directions at cost c. Return the smallest total cost
that gives every house water, either from its own well or through a chain of
pipes leading to a house that has a well.

Examples:

    Input:  wells = [3, 4, 2], pipes = [[1, 2, 1], [2, 3, 5]]
    Output: 6
    Why:    wells at houses 1 and 3, plus the pipe from 1 to 2

    Input:  wells = [1, 1], pipes = [[1, 2, 10]]
    Output: 2
    Why:    two cheap wells beat the expensive pipe

    Input:  wells = [5], pipes = []
    Output: 5
    Why:    edge case, one house and no pipes

Approach:
    With a node 0 for the ground water, a well at house i is the edge from 0
    to i, and a plan that waters every house is exactly a set of edges that
    connects all n + 1 nodes. The cheapest connecting set is a minimum
    spanning tree, because a cycle could always drop its most expensive
    edge. Prim's algorithm grows the tree from node 0 with a min-heap of
    candidate edges and skips stale entries whose far end is already inside.
    Time is O((n + m) log(n + m)) for m pipes, and space is O(n + m).

The lesson behind it: Prim's Spanning Tree
    https://bytepatterns.com/learn/graphs/prim-mst
    python graphs/11-prim-mst.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/water-every-house

Run it:  python problems/graphs/14-water-every-house.py
"""


import heapq

def water_cost(wells, pipes):
    adj = [[] for _ in range(len(wells) + 1)]   # node 0 is the ground water
    for house, cost in enumerate(wells, 1):
        adj[0].append((cost, house))            # a well is an edge to node 0
    for a, b, cost in pipes:
        adj[a].append((cost, b))
        adj[b].append((cost, a))
    inside, heap, total = set(), [(0, 0)], 0
    while heap:
        cost, node = heapq.heappop(heap)        # the cheapest edge out of the tree
        if node in inside:
            continue                            # stale: both ends already inside
        inside.add(node)
        total += cost
        for edge in adj[node]:
            if edge[1] not in inside:
                heapq.heappush(heap, edge)
    return total


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(water_cost([3, 4, 2], [[1, 2, 1], [2, 3, 5]]), 6)
    check(water_cost([1, 1], [[1, 2, 10]]), 2)
    check(water_cost([5], []), 5)
