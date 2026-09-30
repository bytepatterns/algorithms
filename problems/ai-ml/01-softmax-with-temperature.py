"""
Softmax With Temperature (easy) · patterns: softmax, numerical-stability

A language model scores every candidate next token with a raw number called
a logit, and sampling turns those scores into probabilities with a softmax:
divide each logit by the temperature T, exponentiate, and normalise so the
results sum to 1. Write softmax(logits, temperature) returning the
probabilities rounded to 3 decimals. It must not overflow on large logits
such as 1000, and a temperature of 0 means greedy decoding, so all of the
probability goes to the highest logit, the first one on a tie.

Examples:

    Input:  logits = [2.0, 1.0, 0.1], temperature = 1.0
    Output: [0.659, 0.242, 0.099]

    Input:  logits = [2.0, 1.0, 0.1], temperature = 0.5
    Output: [0.864, 0.117, 0.019]
    Why:    a low temperature stretches the gaps, so the favourite takes more

    Input:  logits = [1000.0, 999.0], temperature = 1.0
    Output: [0.731, 0.269]
    Why:    edge case, exp(1000) overflows, but only the differences between logits matter

Approach:
    Dividing by the temperature before the softmax scales the gaps between
    logits: below 1 the gaps grow and the distribution sharpens toward the
    top token, above 1 they shrink and it flattens toward uniform.
    Subtracting the maximum scaled logit first is the standard stability
    trick, since it multiplies the numerator and the denominator by the same
    factor, leaving the answer unchanged while keeping every exponent at or
    below zero. Temperature 0 is the limit of that sharpening and cannot be
    computed by division, so it is handled as greedy decoding directly. Time
    and space are O(v) for v logits.

The lesson behind it: Temperature and Sampling
    https://bytepatterns.com/learn/ai-ml/temperature-and-sampling
    python ai-ml/09-temperature-and-sampling.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/softmax-with-temperature

Run it:  python problems/ai-ml/01-softmax-with-temperature.py
"""


import math

def softmax(logits, temperature=1.0):
    if temperature == 0:                   # greedy: all the mass on the top logit
        best = logits.index(max(logits))
        return [1.0 if i == best else 0.0 for i in range(len(logits))]
    scaled = [x / temperature for x in logits]
    top = max(scaled)                      # shift by the max so exp never overflows
    exps = [math.exp(x - top) for x in scaled]
    total = sum(exps)
    return [round(e / total, 3) for e in exps]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(softmax([2.0, 1.0, 0.1]), [0.659, 0.242, 0.099])
    check(softmax([2.0, 1.0, 0.1], 0.5), [0.864, 0.117, 0.019])
    check(softmax([2.0, 1.0, 0.1], 5.0), [0.4, 0.327, 0.273])
    check(softmax([1000.0, 999.0]), [0.731, 0.269])
    check(softmax([3.0, 5.0, 5.0], 0), [0.0, 1.0, 0.0])
