"""
Int8 Quantization Round Trip (easy) · patterns: quantization, scale-and-round

Quantization stores model weights as small integers plus one float scale.
Implement symmetric int8 quantization for a list of weights: the scale is
the largest absolute weight divided by 127, each weight becomes round(w /
scale) clamped to the range -127 to 127, and dequantizing multiplies back by
the scale. Return the integer codes, the scale rounded to 6 decimals, and
the largest absolute error between a weight and its dequantized value, also
rounded to 6 decimals. If every weight is 0, use a scale of 1.0.

Examples:

    Input:  [0.4, -2.54, 0.013, 1.0]
    Output: ([20, -127, 1, 50], 0.02, 0.007)
    Why:    the scale is 2.54 / 127 = 0.02, so 0.013 lands on 1 step and comes back as 0.02

    Input:  [0.01, 0.02, -0.03, 10.0]
    Output: ([0, 0, 0, 127], 0.07874, 0.03)
    Why:    one outlier stretches the scale, and every small weight collapses to 0

    Input:  [0.0, 0.0]
    Output: ([0, 0], 1.0, 0.0)
    Why:    edge case, an all-zero list has no largest weight to divide, so a scale of 1.0 avoids dividing by zero

Approach:
    Int8 quantization trades precision for memory: each weight shrinks from
    4 bytes to 1, and the only extra storage is one float scale per tensor.
    The scale maps the largest absolute weight onto 127, so every other
    weight is expressed in steps of that size and rounding can move it by at
    most half a step. The second example shows the weakness of a single
    scale per tensor: one outlier of 10.0 makes the step about 0.079, and
    every small weight rounds to 0, which is why practical schemes use a
    scale per channel or per block, or keep outliers in higher precision.
    Clamping guards against codes just outside the range. Time is O(n) and
    space is O(n) for the codes.

The lesson behind it: Quantization
    https://bytepatterns.com/learn/ai-ml/quantization
    python ai-ml/18-quantization.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/ai-ml/int8-quantization-round-trip

Run it:  python problems/ai-ml/06-int8-quantization-round-trip.py
"""


def quantize_int8(weights):
    peak = max(abs(w) for w in weights)
    scale = peak / 127 if peak else 1.0    # largest weight maps to 127
    codes = [max(-127, min(127, round(w / scale))) for w in weights]
    back = [c * scale for c in codes]      # dequantize
    err = max(abs(w - b) for w, b in zip(weights, back))
    return codes, round(scale, 6), round(err, 6)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(quantize_int8([0.4, -2.54, 0.013, 1.0]), ([20, -127, 1, 50], 0.02, 0.007))
    check(quantize_int8([0.01, 0.02, -0.03, 10.0]), ([0, 0, 0, 127], 0.07874, 0.03))
    check(quantize_int8([0.0, 0.0]), ([0, 0], 1.0, 0.0))
