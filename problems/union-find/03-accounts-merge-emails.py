"""
Accounts Merge By Email (hard) · patterns: union-find, hash-map

Each account is a name followed by one or more email addresses. Two accounts
belong to the same person when they share at least one email, and that
sharing is transitive: A shares with B and B with C means all three are one
person. Merge them, and return each person as their name followed by all
their emails in sorted order. Different people may have the same name.

Examples:

    Input:  [["Jo", "a@x", "b@x"], ["Jo", "b@x", "c@x"], ["Kim", "d@x"]]
    Output: [["Jo", "a@x", "b@x", "c@x"], ["Kim", "d@x"]]
    Why:    the two Jo accounts share b@x, so they are one person

    Input:  [["Jo", "a@x"], ["Jo", "z@x"]]
    Output: [["Jo", "a@x"], ["Jo", "z@x"]]
    Why:    the same name with no shared email is two different people

    Input:  [["Kim", "d@x"]]
    Output: [["Kim", "d@x"]]
    Why:    edge case, a single account merges with nothing

Approach:
    Emails are the elements; an account is just an instruction to join its
    own emails together. After one pass the sets are exactly the people,
    whatever order the accounts arrived in. A second pass buckets each email
    under its representative, and the name is carried along on any email of
    the group since every account in a group agrees on it. Sorting inside
    each bucket gives the required output order. Time is O(E log E)
    dominated by the sorting, space O(E).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/union-find/accounts-merge-emails

Run it:  python problems/union-find/03-accounts-merge-emails.py
"""


def merge_accounts(accounts):
    parent, owner = {}, {}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]        # path halving
            x = parent[x]
        return x
    for name, *emails in accounts:
        for e in emails:
            parent.setdefault(e, e)
            owner[e] = name                      # any email carries the name
        for e in emails[1:]:
            parent[find(e)] = find(emails[0])    # one account, one set
    groups = {}
    for e in parent:
        groups.setdefault(find(e), []).append(e)
    return sorted([owner[root]] + sorted(es) for root, es in groups.items())


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(merge_accounts([["Jo", "a@x", "b@x"], ["Jo", "b@x", "c@x"], ["Kim", "d@x"]]), [['Jo', 'a@x', 'b@x', 'c@x'], ['Kim', 'd@x']])
    check(merge_accounts([["Jo", "a@x"], ["Jo", "z@x"]]), [['Jo', 'a@x'], ['Jo', 'z@x']])
