"""
Feed Fan-Out Cost (medium) · patterns: fan-out, cost-model

A news feed can be built three ways, and each costs a different number of
storage operations per day. With push, every post is written into each
follower's feed, and opening a feed is 1 read. With pull, nothing is fanned
out, and opening a feed reads from every account the user follows. The
hybrid pushes posts from ordinary accounts but pulls posts from celebrities,
accounts with at least threshold followers, so opening a feed costs 1 read
plus 1 per celebrity followed. Given the follow edges as (follower,
followee), posts per day per author and feed opens per day per user, return
each model's daily operations (fan-out writes plus reads) and the cheapest
one, preferring push, then pull, then hybrid on a tie.

Examples:

    Input:  4 fans follow "star" and each other; star posts 20 a day, the others 1;
            each fan opens the feed 10 times a day; threshold = 4
    Output: ({'push': 132, 'pull': 160, 'hybrid': 92}, 'hybrid')
    Why:    pushing star's 20 posts to 4 feeds is the expensive part, and the hybrid skips exactly that

    Input:  the same graph and posts, but only ann opens the feed, once a day
    Output: ({'push': 93, 'pull': 4, 'hybrid': 14}, 'pull')
    Why:    when feeds are rarely read, writing posts into them ahead of time is wasted work

    Input:  follows = [("ann", "bob")], posts = {"bob": 50}, opens = {"ann": 1}, threshold = 100
    Output: ({'push': 51, 'pull': 1, 'hybrid': 51}, 'pull')
    Why:    edge case, with no celebrity the hybrid is just push

Approach:
    The cost model makes the classic trade-off concrete: push pays at write
    time in proportion to follower counts, and pull pays at read time in
    proportion to how many accounts each reader follows. A celebrity with
    millions of followers makes push explode, while heavy readers make pull
    expensive, and the hybrid takes the cheap side of each by pushing
    ordinary posts and pulling only celebrity posts at read time. The code
    counts followers and followees once, then evaluates the three formulas.
    Which model wins depends on the read-to-write mix, as the first two
    examples show with the same graph. Time is O(E + U) for E follow edges
    and U users, and space is O(E + U).

The lesson behind it: Design a News Feed
    https://bytepatterns.com/learn/system-design-cases/design-a-news-feed

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/system-design-cases/feed-fan-out-cost

Run it:  python problems/system-design-cases/02-feed-fan-out-cost.py
"""


from collections import defaultdict

def fan_out_cost(follows, posts, opens, threshold):
    followers, followees = defaultdict(int), defaultdict(list)
    for fan, star in follows:
        followers[star] += 1
        followees[fan].append(star)
    celeb = {u for u, c in followers.items() if c >= threshold}
    push = sum(p * followers[u] for u, p in posts.items()) + sum(opens.values())
    pull = sum(o * len(followees[v]) for v, o in opens.items())
    hybrid = (sum(p * followers[u] for u, p in posts.items() if u not in celeb)   # push the rest
              + sum(o * (1 + sum(s in celeb for s in followees[v])) for v, o in opens.items()))
    cost = {"push": push, "pull": pull, "hybrid": hybrid}
    return cost, min(cost, key=cost.get)   # first listed wins a tie


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    fans = ["ann", "bob", "cat", "dan"]
    follows = [(f, "star") for f in fans] + [(f, g) for f in fans for g in fans if f != g]
    posts = {"star": 20, "ann": 1, "bob": 1, "cat": 1, "dan": 1}
    check(fan_out_cost(follows, posts, {f: 10 for f in fans}, 4), ({'push': 132, 'pull': 160, 'hybrid': 92}, 'hybrid'))
    check(fan_out_cost(follows, posts, {"ann": 1}, 4), ({'push': 93, 'pull': 4, 'hybrid': 14}, 'pull'))
    check(fan_out_cost([("ann", "bob")], {"bob": 50}, {"ann": 1}, 100), ({'push': 51, 'pull': 1, 'hybrid': 51}, 'pull'))
