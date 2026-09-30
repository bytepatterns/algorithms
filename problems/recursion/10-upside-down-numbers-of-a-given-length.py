"""
Upside-Down Numbers of a Given Length (medium) · patterns: recursion, build-from-inside-out

A clock maker wants every number that still reads correctly when the display
is turned upside down. Rotated by 180 degrees, 0, 1 and 8 stay the same, 6
becomes 9 and 9 becomes 6, and every other digit becomes unreadable. Given n
between 1 and 14, return all n-digit numbers that look the same after the
rotation, as strings in ascending order. A number longer than one digit may
not start with 0.

Examples:

    Input:  n = 2
    Output: ["11", "69", "88", "96"]
    Why:    "00" is excluded because of the leading zero

    Input:  n = 1
    Output: ["0", "1", "8"]
    Why:    edge case, a lone middle digit must map to itself, so 6 and 9 cannot be used

    Input:  n = 3
    Output: ["101", "111", "181", "609", "619", "689", "808", "818", "888", "906", "916", "986"]

Approach:
    After a 180-degree turn the first digit ends up last and rotated, so a
    valid number is a valid rotating pair wrapped around a shorter valid
    number, and the inner part has the same property at length n - 2. That
    makes the recursion return its answers up the call chain: build(k) asks
    for build(k - 2) and wraps every inner string in each of the five pairs.
    The base cases are length 0, which contributes the empty string, and
    length 1, which allows only the self-rotating digits. Inner layers may
    use the (0, 0) pair freely, since a zero in the middle is fine; only the
    outermost layer, where k equals n, skips it to avoid a leading zero. The
    output has about 4 × 5^(n/2 - 1) strings of length n, so time and space
    are O(n × 5^(n/2)).

The lesson behind it: Return Up or Pass Down
    https://bytepatterns.com/learn/recursion/return-up-or-pass-down
    python recursion/06-return-up-or-pass-down.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/recursion/upside-down-numbers-of-a-given-length

Run it:  python problems/recursion/10-upside-down-numbers-of-a-given-length.py
"""


PAIRS = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

def upside_down(n):
    def build(k):
        if k == 0:
            return [""]
        if k == 1:
            return ["0", "1", "8"]
        return [a + mid + b
                for mid in build(k - 2)
                for a, b in PAIRS
                if not (k == n and a == "0")]   # no leading zero at the outer layer
    return sorted(build(n))


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(upside_down(2), ['11', '69', '88', '96'])
    check(upside_down(1), ['0', '1', '8'])
    check(len(upside_down(3)), 12)
    check(len(upside_down(4)), 20)
