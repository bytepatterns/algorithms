"""
Trusted Town Judge (easy) · patterns: degree-counting, directed-graph

A town has n people labelled from 1 to n, and a list of pairs where the pair
a, b means a trusts b. Exactly one person can be the judge: the judge trusts
nobody, and every other person in town trusts the judge. Return the judge's
label, or -1 when no such person exists.

Examples:

    Input:  n = 2, trust = [[1, 2]]
    Output: 2
    Why:    person 2 trusts nobody and is trusted by the only other person

    Input:  n = 3, trust = [[1, 3], [2, 3], [3, 1]]
    Output: -1
    Why:    person 3 is trusted by everyone but trusts someone back

    Input:  n = 1, trust = []
    Output: 1
    Why:    edge case, the only resident vacuously satisfies both rules

Approach:
    Both rules are degree conditions, so one tally per person answers them
    together: being trusted adds one and trusting subtracts one. Only a
    person trusted by all n-1 others while trusting nobody can reach a score
    of n-1, because any outgoing trust would lower it below that ceiling.
    One pass over the pairs and one over the people is all it takes. Time is
    O(n + p) for p pairs, and space is O(n).

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/graphs/trusted-town-judge

Run it:  python problems/graphs/04-trusted-town-judge.py
"""


def find_judge(n, trust):
    score = [0] * (n + 1)            # times trusted minus times trusting
    for a, b in trust:
        score[a] -= 1
        score[b] += 1
    for person in range(1, n + 1):
        if score[person] == n - 1:   # trusted by all the others, trusts nobody
            return person
    return -1


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(find_judge(2, [[1, 2]]), 2)
    check(find_judge(3, [[1, 3], [2, 3], [3, 1]]), -1)
    check(find_judge(1, []), 1)
