"""
Cache Hit Ratio for a News Feed (easy) · patterns: lru-cache, hit-ratio

A news feed service keeps recently viewed posts in an LRU cache in front of
its database. Given the sequence of post ids that readers request and the
cache capacity in posts, replay the requests: a request for a cached post is
a hit and makes it the most recently used; a miss loads the post into the
cache, evicting the least recently used post if the cache is over capacity.
Return the hit ratio as a percentage rounded to 1 decimal. Call it for
several capacities to see how much each extra slot buys. There are up to
1,000,000 requests.

Examples:

    Input:  feed = ["p1", "p2", "p1", "p3", "p1", "p2", "p4", "p1", "p5", "p2", "p1", "p3"],
            capacities 1, 2, 3 and 4
    Output: [0.0, 16.7, 41.7, 50.0]
    Why:    the third slot adds the most, because it is enough to keep both hot posts, p1 and p2

    Input:  feed = ["a", "b", "c", "a", "b", "c"], capacity = 2
    Output: 0.0
    Why:    a loop one post longer than the cache evicts each post just before it is needed again

    Input:  feed = ["x", "x", "x"], capacity = 1
    Output: 66.7
    Why:    edge case, only the very first request for a post can miss

Approach:
    Feed traffic is skewed, a few posts get most of the views, and that skew
    is what makes a small cache worth having. The simulation is an LRU cache
    on an OrderedDict: a hit moves the post to the most recently used end,
    and a miss inserts it and evicts from the other end when the cache
    overflows. Running the same trace against several capacities gives the
    hit-ratio curve an interview answer should reason about: the first
    example jumps once the cache can hold both hot posts and then flattens.
    The second example is LRU's known weak spot, a cyclic scan slightly
    larger than the cache, where the hit ratio drops to zero. Each request
    is O(1), so time is O(n) per capacity and space is O(c) for c cached
    posts.

The lesson behind it: Design a Distributed Cache
    https://bytepatterns.com/learn/system-design-cases/design-a-distributed-cache

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design-cases/cache-hit-ratio-for-a-news-feed

Run it:  python problems/system-design-cases/04-cache-hit-ratio-for-a-news-feed.py
"""


from collections import OrderedDict

def hit_ratio(requests, capacity):
    cache, hits = OrderedDict(), 0         # front = least recently used
    for post in requests:
        if post in cache:
            hits += 1
            cache.move_to_end(post)        # now the most recently used
        else:
            cache[post] = True
            if len(cache) > capacity:
                cache.popitem(last=False)  # evict the least recently used
    return round(100 * hits / len(requests), 1)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    feed = ["p1", "p2", "p1", "p3", "p1", "p2", "p4", "p1", "p5", "p2", "p1", "p3"]
    check([hit_ratio(feed, c) for c in (1, 2, 3, 4)], [0.0, 16.7, 41.7, 50.0])
    check(hit_ratio(["a", "b", "c", "a", "b", "c"], 2), 0.0)
    check(hit_ratio(["x", "x", "x"], 1), 66.7)
