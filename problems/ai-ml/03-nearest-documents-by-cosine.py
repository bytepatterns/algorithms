"""
Nearest Documents by Cosine (medium) · patterns: vector-math, partial-sort

A help-centre search embeds every article as a vector and embeds the user's
question the same way. Given the query vector, a dict from article name to
vector, and k, return the k articles with the highest cosine similarity to
the query as (name, score) pairs, scores rounded to 3 decimals, best first.
Equal scores are ordered by name so the result is stable. A zero vector has
no direction, so it is never returned, and a zero query returns nothing.
There can be 100,000 articles while k is small, so avoid sorting all of
them.

Examples:

    Input:  query = [1.0, 0.2, 0.0], k = 2, articles = refunds [0.9, 0.1, 0.0], shipping [0.1, 0.9, 0.1],
            returns [0.8, 0.3, 0.1], careers [0.0, 0.1, 0.9], blank [0, 0, 0]
    Output: [('refunds', 0.996), ('returns', 0.98)]

    Input:  query = [2, 0, 0], k = 2, articles = b [1, 0, 0], a [3, 0, 0], c [0, 1, 0]
    Output: [('a', 1.0), ('b', 1.0)]
    Why:    length does not matter to cosine, so a and b tie and the name decides

    Input:  query = [0, 0, 0], k = 3, the articles from the first example
    Output: []
    Why:    edge case, a zero query points nowhere

Approach:
    Cosine similarity divides the dot product by both lengths, so it
    compares directions only, which is what embedding search wants: a long
    article and a short one about the same topic point the same way. The
    query's length is computed once and zero vectors are skipped, because a
    vector with no direction has no angle to compare. heapq.nsmallest(k, …,
    key=(-score, name)) keeps only k candidates in a heap while it scans,
    which is O(n log k) instead of the O(n log n) of a full sort. Scores are
    rounded to 6 places before ranking so that two mathematically equal
    scores cannot be split by floating-point noise and the name tie-break
    really decides. Scoring is O(n × d) for n vectors of d dimensions, and
    extra space is O(n).

The lesson behind it: Cosine Similarity
    https://bytepatterns.com/learn/ai-ml/cosine-similarity
    python ai-ml/04-cosine-similarity.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/nearest-documents-by-cosine

Run it:  python problems/ai-ml/03-nearest-documents-by-cosine.py
"""


import heapq, math

def top_k_similar(query, docs, k):
    qn = math.sqrt(sum(x * x for x in query))
    scored = []
    for name, vec in docs.items():
        vn = math.sqrt(sum(x * x for x in vec))
        if qn == 0 or vn == 0:
            continue                       # a zero vector has no direction to compare
        cos = sum(a * b for a, b in zip(query, vec)) / (qn * vn)
        scored.append((round(cos, 6), name))
    best = heapq.nsmallest(k, scored, key=lambda s: (-s[0], s[1]))   # high score, then name
    return [(name, round(score, 3)) for score, name in best]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    docs = {"refunds": [0.9, 0.1, 0.0], "shipping": [0.1, 0.9, 0.1],
            "returns": [0.8, 0.3, 0.1], "careers": [0.0, 0.1, 0.9], "blank": [0, 0, 0]}
    check(top_k_similar([1.0, 0.2, 0.0], docs, 2), [('refunds', 0.996), ('returns', 0.98)])
    check(top_k_similar([2, 0, 0], {"b": [1, 0, 0], "a": [3, 0, 0], "c": [0, 1, 0]}, 2), [('a', 1.0), ('b', 1.0)])
    check(top_k_similar([0, 0, 0], docs, 3), [])
