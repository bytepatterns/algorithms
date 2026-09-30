"""
Fewest Clips to Cover a Broadcast (medium) · patterns: greedy, reach-frontier, interval-cover

A live broadcast ran from second 0 to second T. Several cameras recorded
clips given as [start, end], and clips may overlap or run past T. Any clip
can be trimmed. Return the fewest clips needed to cover the whole broadcast
from 0 to T, or -1 if some moment is missing from every clip.

Examples:

    Input:  clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], T = 10
    Output: 3
    Why:    [0, 2], then [1, 9], then [8, 10]

    Input:  clips = [[0, 1], [1, 2]], T = 5
    Output: -1
    Why:    nothing was recorded after second 2

    Input:  clips = [[0, 4]], T = 3
    Output: 1
    Why:    edge case, one clip longer than the broadcast is simply trimmed

Approach:
    This is the reach frontier from the jump game with clips in place of
    jumps. For every start second only the longest clip matters, so the
    clips collapse into one furthest end per second. The walk keeps the end
    of the covered stretch and the furthest end offered by any clip starting
    inside it. When the walk reaches the covered end, a new clip is
    unavoidable, and choosing the one that reaches furthest is safe because
    any other choice covers a prefix of what it covers. If the furthest end
    is not past the current second at that moment, no clip bridges the gap.
    Time is O(n + T) for n clips, and space is O(T).

The lesson behind it: Jump Game
    https://bytepatterns.com/learn/greedy/jump-game
    python greedy/03-jump-game.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/greedy/fewest-clips-to-cover-a-broadcast

Run it:  python problems/greedy/10-fewest-clips-to-cover-a-broadcast.py
"""


def fewest_clips(clips, T):
    furthest = [0] * (T + 1)              # longest reach of a clip starting at each second
    for start, end in clips:
        if start <= T:
            furthest[start] = max(furthest[start], end)
    count = covered = frontier = 0
    for t in range(T):
        frontier = max(frontier, furthest[t])
        if t == covered:                  # the current coverage runs out here
            if frontier <= t:             # no clip reaches past this second
                return -1
            count += 1
            covered = frontier
    return count


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fewest_clips([[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10), 3)
    check(fewest_clips([[0, 1], [1, 2]], 5), -1)
    check(fewest_clips([[0, 4]], 3), 1)
