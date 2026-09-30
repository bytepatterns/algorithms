"""
Trim a Chat to Fit the Context (medium) · patterns: token-budget, newest-first

A chat app must fit each request into the model's context window of budget
tokens. The request always carries the system prompt (system tokens) and
must leave reserve tokens free for the reply. turns lists the conversation's
token counts oldest first; it alternates user and assistant and ends with
the new user message, so its length is odd. Keep the newest user message,
then keep older (user, assistant) pairs from newest to oldest while they
fit, never dropping half of a pair and never leaving a gap in the history.
Return how many of the oldest turns are dropped, or None if even the system
prompt, the new message and the reserve do not fit.

Examples:

    Input:  budget = 100, system = 20, reserve = 25, turns = [10, 30, 10, 20, 15]
    Output: 2
    Why:    55 tokens are free: 15 for the new message and 30 for the newest pair, and the oldest pair of 40 does not fit in the 10 left

    Input:  budget = 200, system = 20, reserve = 25, turns = [10, 30, 10, 20, 15]
    Output: 0
    Why:    the whole conversation fits

    Input:  budget = 50, system = 20, reserve = 10, turns = [10, 30, 40]
    Output: None
    Why:    edge case, the new message alone is larger than the 20 tokens left

Approach:
    The system prompt and the reply reserve are fixed costs, so they come
    off the budget first, and the new user message is next, since a request
    without it is pointless; if that already overflows there is no valid
    request and the answer is None. Older history is kept from the newest
    end, a pair at a time, because the most recent exchanges are what the
    model most needs and an answer without its question confuses it. The
    walk stops at the first pair that does not fit rather than skipping to a
    smaller older one, since a conversation with a hole in the middle reads
    as if the user had said something different. Time is O(t) for t turns
    and space is O(1).

The lesson behind it: Context Windows
    https://bytepatterns.com/learn/ai-ml/context-windows
    python ai-ml/10-context-windows.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/trim-a-chat-to-fit-the-context

Run it:  python problems/ai-ml/04-trim-a-chat-to-fit-the-context.py
"""


def fit_context(budget, system, turns, reserve):
    left = budget - system - reserve - turns[-1]   # the newest user turn always stays
    if left < 0:
        return None                        # not even the new message fits
    kept = 1
    for i in range(len(turns) - 2, 0, -2): # older (user, assistant) pairs, newest first
        pair = turns[i - 1] + turns[i]
        if pair > left:
            break                          # stop at the first misfit: no holes in history
        left -= pair
        kept += 2
    return len(turns) - kept               # how many of the oldest turns are dropped


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(fit_context(100, 20, [10, 30, 10, 20, 15], 25), 2)
    check(fit_context(200, 20, [10, 30, 10, 20, 15], 25), 0)
    check(fit_context(50, 20, [10, 30, 40], 10), None)
