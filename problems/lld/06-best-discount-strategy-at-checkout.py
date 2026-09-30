"""
Best Discount Strategy at Checkout (easy) · patterns: strategy-pattern, class-design

A shop runs several promotions but applies only one per order. A cart is a
list of (item, price, quantity) with prices in cents. Write three promotion
classes that share one interface, a name and a discount(cart) method:
PercentOff(pct) takes pct percent off the subtotal, rounded down;
AmountOffOver(threshold, amount) takes a flat amount off when the subtotal
reaches the threshold; and BuyNGetOneFree(item, n) makes every (n + 1)th
unit of one item free. Then write checkout(cart, promotions), which picks
the promotion with the largest discount, the first one listed on a tie, and
returns its name with the total to pay. If no promotion saves anything,
return "no discount" with the subtotal.

Examples:

    Input:  cart = [("coffee", 1200, 3), ("mug", 900, 2)], all three promotions
    Output: ('buy 2 coffee get 1 free', 4200)
    Why:    one free coffee saves 1200, more than 10% (540) or 800 off over 5000

    Input:  cart = [("grinder", 9900, 1)], all three promotions
    Output: ('10% off', 8910)
    Why:    on a large order the percentage beats the flat amount

    Input:  cart = [("mug", 900, 1)], only AmountOffOver(5000, 800)
    Output: ('no discount', 900)
    Why:    edge case, the order is below the threshold, so nothing applies

Approach:
    This is the strategy pattern: each promotion is a small class behind one
    interface, so checkout compares them without an if-chain and a new
    promotion is a new class rather than an edit to checkout. Each class
    keeps its own rule, a percentage of the subtotal, a flat amount behind a
    threshold, or a free unit for every n bought, and all of them return
    integer cents so no rounding error creeps into the total. Checkout asks
    every promotion for its saving and keeps the largest, relying on max
    returning the first of equal keys for the tie rule. A saving of 0 is
    reported as no discount rather than as a promotion that did nothing.
    Time is O(p × c) for p promotions and c cart lines, and space is O(1)
    beyond the input.

The lesson behind it: Strategy Pattern
    https://bytepatterns.com/learn/lld/strategy-pattern
    python lld/06-strategy-pattern.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/best-discount-strategy-at-checkout

Run it:  python problems/lld/06-best-discount-strategy-at-checkout.py
"""


def subtotal(cart):
    return sum(price * qty for _, price, qty in cart)

class PercentOff:
    def __init__(self, pct):
        self.name, self.pct = f"{pct}% off", pct
    def discount(self, cart):
        return subtotal(cart) * self.pct // 100        # round down, in cents

class AmountOffOver:
    def __init__(self, threshold, amount):
        self.name = f"{amount} off over {threshold}"
        self.threshold, self.amount = threshold, amount
    def discount(self, cart):
        return self.amount if subtotal(cart) >= self.threshold else 0

class BuyNGetOneFree:
    def __init__(self, item, n):
        self.name = f"buy {n} {item} get 1 free"
        self.item, self.n = item, n
    def discount(self, cart):
        return sum(price * (qty // (self.n + 1)) for name, price, qty in cart if name == self.item)

def checkout(cart, promotions):
    best = max(promotions, key=lambda p: p.discount(cart), default=None)   # first wins a tie
    if best is None or best.discount(cart) == 0:
        return "no discount", subtotal(cart)
    return best.name, subtotal(cart) - best.discount(cart)


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    offers = [PercentOff(10), AmountOffOver(5000, 800), BuyNGetOneFree("coffee", 2)]
    check(checkout([("coffee", 1200, 3), ("mug", 900, 2)], offers), ('buy 2 coffee get 1 free', 4200))
    check(checkout([("grinder", 9900, 1)], offers), ('10% off', 8910))
    check(checkout([("mug", 900, 1)], [AmountOffOver(5000, 800)]), ('no discount', 900))
    check(checkout([("tea", 1000, 5)], offers), ('800 off over 5000', 4200))
