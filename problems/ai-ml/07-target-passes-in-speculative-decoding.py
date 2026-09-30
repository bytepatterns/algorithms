"""
Target Passes in Speculative Decoding (medium) · patterns: speculative-decoding, draft-and-verify

Speculative decoding speeds up generation with a small draft model. Both
models here are greedy and deterministic, given as dicts from the last token
to the next token; a token missing from a dict produces "<eos>". Each round,
the draft proposes k tokens one after another, then one pass of the large
target model checks them: it accepts proposed tokens while they match what
the target itself would produce, and at the first mismatch it keeps its own
token instead. If all k match, the same pass adds one bonus token. Generate
exactly n tokens after the prompt, stopping mid-round if needed, and return
the tokens and the number of target passes used.

Examples:

    Input:  prompt = ["the"], draft guesses "a" after "on" where the target says "the", k = 4, n = 8
    Output: (['cat', 'sat', 'on', 'the', 'cat', 'sat', 'on', 'the'], 2)
    Why:    3 guesses are accepted and the target fixes the 4th, so each pass yields 4 tokens

    Input:  prompt = ["the"], draft = target, k = 3, n = 8
    Output: (['cat', 'sat', 'on', 'the', 'cat', 'sat', 'on', 'the'], 2)
    Why:    a perfect draft yields k + 1 tokens per pass: 3 accepted plus the bonus

    Input:  prompt = ["the"], draft = {}, k = 3, n = 3
    Output: (['cat', 'sat', 'on'], 3)
    Why:    edge case, a draft that is always wrong still gives the target's exact text, one token per pass

Approach:
    The draft model is cheap and the target is expensive, and one target
    pass can score several positions at once, so the draft proposes a run of
    tokens and the target checks them all in a single pass. Accepting a
    guess only when it equals the target's own choice is what guarantees the
    output is identical to plain target decoding, and the target's token at
    the first mismatch means every pass makes progress even when the draft
    is useless. The number of passes is the whole speed-up: 2 passes for 8
    tokens here instead of 8, and the more often the draft agrees with the
    target, the closer each pass gets to k + 1 tokens. Each round costs O(k)
    dictionary lookups and produces at least one token, so time is O(n × k)
    and space is O(n).

The lesson behind it: Speculative Decoding
    https://bytepatterns.com/learn/ai-ml/speculative-decoding

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/target-passes-in-speculative-decoding

Run it:  python problems/ai-ml/07-target-passes-in-speculative-decoding.py
"""


def speculative(prompt, target, draft, k, n):
    out, passes, goal = list(prompt), 0, len(prompt) + n
    while len(out) < goal:
        guess, last = [], out[-1]
        for _ in range(k):                 # the draft runs ahead k tokens
            last = draft.get(last, "<eos>")
            guess.append(last)
        passes += 1                        # one target pass checks them all
        last = out[-1]
        for g in guess:
            want = target.get(last, "<eos>")
            out.append(want)               # the target's token is always kept
            last = want
            if want != g or len(out) == goal:
                break                      # first mismatch ends the round
        else:
            if len(out) < goal:
                out.append(target.get(last, "<eos>"))   # all k matched: bonus token
    return out[len(prompt):], passes


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    target = {"the": "cat", "cat": "sat", "sat": "on", "on": "the"}
    draft = {"the": "cat", "cat": "sat", "sat": "on", "on": "a"}
    check(speculative(["the"], target, draft, 4, 8), (['cat', 'sat', 'on', 'the', 'cat', 'sat', 'on', 'the'], 2))
    check(speculative(["the"], target, target, 3, 8), (['cat', 'sat', 'on', 'the', 'cat', 'sat', 'on', 'the'], 2))
    check(speculative(["the"], target, {}, 3, 3), (['cat', 'sat', 'on'], 3))
