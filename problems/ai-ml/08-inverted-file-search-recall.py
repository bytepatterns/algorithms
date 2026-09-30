"""
Inverted-File Search Recall (hard) · patterns: vector-search, inverted-file-index, recall-at-k

An inverted-file index speeds up vector search by clustering. Given integer
vectors and fixed centroids, put each vector in the list of its nearest
centroid by squared Euclidean distance, the lowest centroid index on a tie.
A search for a query ranks the centroids by distance to it, scans only the
lists of the nprobe nearest, and returns the k closest vectors found there,
ties broken by vector index. Measure the index against exact search: for
every nprobe from 1 to the number of centroids, return the recall at k, the
fraction of the exact top-k vectors that the index also returned, averaged
over all queries and rounded to 2 decimals.

Examples:

    Input:  vectors = [(0, 0), (1, 1), (2, 0), (9, 9), (8, 10), (10, 8), (5, 4), (4, 6)],
            centroids = [(1, 0), (9, 9), (5, 5)], queries = [(3, 2), (7, 7)], k = 3
    Output: [0.83, 1.0, 1.0]
    Why:    (3, 2) probes only the (1, 0) cluster and misses (5, 4), which sits in the next one

    Input:  the same vectors and centroids, queries = [(6, 1)], k = 2
    Output: [0.5, 1.0, 1.0]
    Why:    the query's nearest centroid holds one of its two true neighbours; probing a second list finds the other

    Input:  vectors = [(0, 0), (1, 0)], centroids = [(0, 0)], queries = [(5, 5)], k = 2
    Output: [1.0]
    Why:    edge case, with a single list the index scans everything and matches exact search

Approach:
    An inverted-file index trades recall for speed: instead of comparing a
    query with every vector, it compares with a handful of centroids and
    scans only the closest few lists. That misses true neighbours that sit
    just across a cluster boundary, which is exactly what the first query
    shows, and nprobe is the dial: more lists scanned, higher recall, more
    work. The solution builds the lists once, then measures recall by
    running exact search and index search through the same top-k helper, so
    the only difference between them is which candidates they see, and
    tie-breaking by index keeps both deterministic. Recall at k is then a
    set intersection per query, averaged. With n vectors, c centroids and q
    queries, building costs O(n × c) and measuring costs O(c × q × (n log
    n)) in the worst case, with O(n + c) space.

The lesson behind it: Approximate Neighbours
    https://bytepatterns.com/learn/ai-ml/approximate-nearest-neighbours

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/inverted-file-search-recall

Run it:  python problems/ai-ml/08-inverted-file-search-recall.py
"""


from collections import defaultdict

def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))

def ivf_recall(vectors, centroids, queries, k):
    lists = defaultdict(list)              # centroid index -> vector indices
    for i, v in enumerate(vectors):
        c = min(range(len(centroids)), key=lambda j: (dist(v, centroids[j]), j))
        lists[c].append(i)

    def top_k(q, ids):
        return sorted(ids, key=lambda i: (dist(q, vectors[i]), i))[:k]

    recalls = []
    for nprobe in range(1, len(centroids) + 1):
        hits = 0
        for q in queries:
            exact = set(top_k(q, range(len(vectors))))
            near = sorted(range(len(centroids)), key=lambda j: (dist(q, centroids[j]), j))[:nprobe]
            found = top_k(q, [i for c in near for i in lists[c]])   # scan probed lists only
            hits += len(exact.intersection(found))
        recalls.append(round(hits / (k * len(queries)), 2))
    return recalls


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    vectors = [(0, 0), (1, 1), (2, 0), (9, 9), (8, 10), (10, 8), (5, 4), (4, 6)]
    centroids = [(1, 0), (9, 9), (5, 5)]
    check(ivf_recall(vectors, centroids, [(3, 2), (7, 7)], 3), [0.83, 1.0, 1.0])
    check(ivf_recall(vectors, centroids, [(6, 1)], 2), [0.5, 1.0, 1.0])
    check(ivf_recall([(0, 0), (1, 0)], [(0, 0)], [(5, 5)], 2), [1.0])
