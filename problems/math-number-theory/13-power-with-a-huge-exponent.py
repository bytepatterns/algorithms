"""
Power With a Huge Exponent (medium) · patterns: fast-exponentiation, modular-arithmetic

A checksum scheme needs a^b mod 1337, where a is a positive integer up to
2^31 - 1 and the exponent b is so large it arrives as a list of its decimal
digits, most significant first, up to 2,000 digits long. Return the result.
Turning the digit list into one integer and calling a general power routine
is not allowed; work from the digits directly.

Examples:

    Input:  a = 2, b = [3]
    Output: 8

    Input:  a = 2, b = [1, 0]
    Output: 1024
    Why:    the exponent is 10, and 2^10 = 1024 is still below 1337

    Input:  a = 1, b = [4, 3, 3, 8, 5, 2]
    Output: 1
    Why:    edge case, 1 to any power is 1

Approach:
    The exponent is never built. Reading its digits left to right, each new
    digit d turns the exponent e into 10e + d, and the power follows the
    same rule: a^(10e + d) = (a^e)^10 · a^d. So the running result only
    needs to be raised to the tenth power and multiplied by a^d, both done
    with square-and-multiply, and every product is reduced modulo 1337 so
    the numbers stay small. Each digit costs a constant number of
    multiplications, so time is O(len(b)), and space is O(1).

The lesson behind it: Fast Exponentiation
    https://bytepatterns.com/learn/math-number-theory/fast-exponentiation
    python math-number-theory/04-fast-exponentiation.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/math-number-theory/power-with-a-huge-exponent

Run it:  python problems/math-number-theory/13-power-with-a-huge-exponent.py
"""


MOD = 1337

def fast_pow(x, e):
    x %= MOD
    out = 1
    while e:
        if e & 1:
            out = out * x % MOD
        x = x * x % MOD                       # square for the next bit
        e >>= 1
    return out

def huge_power(a, digits):
    result = 1
    for d in digits:                          # exponent e becomes 10e + d
        result = fast_pow(result, 10) * fast_pow(a, d) % MOD
    return result


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    check(huge_power(2, [3]), 8)
    check(huge_power(2, [1, 0]), 1024)
    check(huge_power(1, [4, 3, 3, 8, 5, 2]), 1)
    check(huge_power(2147483647, [2, 0, 0]), 1198)
