"""
Array Basics: One block of memory, instant access to any slot.

An array stores items back to back in memory, so the computer can compute
any slot's address with simple arithmetic. Reading or writing by index is
O(1). Inserting in the middle is not, because everything after it has to
shift.

Lesson 1 of Arrays, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/arrays/array-basics

Run it:  python arrays/01-array-basics.py
"""


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    prices = [12, 7, 30, 5]

    check(prices[2], 30)  # O(1) direct access
    prices[0] = 99          # O(1) overwrite
    check(len(prices), 4)  # O(1), length is stored

    prices.append(8)        # O(1) amortized, lands at the end
    prices.insert(1, 42)    # O(n), shifts everything right
    check(prices, [99, 42, 7, 30, 5, 8])
