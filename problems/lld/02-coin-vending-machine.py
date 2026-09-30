"""
Coin Vending Machine (easy) · patterns: class-design, state-machine

Design a vending machine class. It is built with a price per slot code and a
stock count per slot, and it keeps the credit inserted so far. insert(coin)
accepts only 5, 10, 25 and 100 and answers "credit N", or "rejected N" for
any other coin, which drops straight back out. select(code) answers "sold
out" for an empty slot, "need N" when the credit is N short, and otherwise
vends, returns the change and resets the credit: "vend CODE, change N".
cancel() returns the whole credit as "refund N". The machine must never vend
without payment or keep money after a vend or a cancel.

Examples:

    Input:  prices = A1 65, B2 40; stock = A1 1, B2 0
            insert(25), insert(3), select("A1")
    Output: ['credit 25', 'rejected 3', 'need 40']

    Input:  then insert(100), select("A1"), select("A1")
    Output: ['credit 125', 'vend A1, change 60', 'sold out']
    Why:    the only A1 is gone after the first vend

    Input:  then select("B2"), insert(10), cancel()
    Output: ['sold out', 'credit 10', 'refund 10']
    Why:    edge case, a slot that starts empty never takes money for itself

Approach:
    The machine's whole state is its price table, its stock and one credit
    counter, and every method guards its failure cases before touching any
    of them, so a rejected coin, a sold-out slot or a short credit leaves
    the state exactly as it was. Stock is checked before credit so that an
    empty slot is reported as sold out rather than as a price to be paid. On
    a vend the change and the reset credit are computed together, which
    makes it impossible to hand out change and still hold the credit. A
    small run helper replays a list of calls so each example is one line.
    Every call is O(1).

The lesson behind it: Vending Machine
    https://bytepatterns.com/learn/lld/vending-machine-design
    python lld/14-vending-machine-design.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/coin-vending-machine

Run it:  python problems/lld/02-coin-vending-machine.py
"""


class VendingMachine:
    COINS = {5, 10, 25, 100}

    def __init__(self, prices, stock):
        self.prices, self.stock, self.credit = prices, stock, 0

    def insert(self, coin):
        if coin not in self.COINS:
            return "rejected " + str(coin)     # the coin drops straight back out
        self.credit += coin
        return "credit " + str(self.credit)

    def select(self, code):
        if self.stock.get(code, 0) == 0:
            return "sold out"
        if self.credit < self.prices[code]:
            return "need " + str(self.prices[code] - self.credit)
        change, self.credit = self.credit - self.prices[code], 0
        self.stock[code] -= 1
        return "vend " + code + ", change " + str(change)

    def cancel(self):
        refund, self.credit = self.credit, 0
        return "refund " + str(refund)

def run(machine, calls):
    return [getattr(machine, name)(*args) for name, *args in calls]


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    vm = VendingMachine({"A1": 65, "B2": 40}, {"A1": 1, "B2": 0})
    check(run(vm, [("insert", 25), ("insert", 3), ("select", "A1")]), ['credit 25', 'rejected 3', 'need 40'])
    check(run(vm, [("insert", 100), ("select", "A1"), ("select", "A1")]), ['credit 125', 'vend A1, change 60', 'sold out'])
    check(run(vm, [("select", "B2"), ("insert", 10), ("cancel",)]), ['sold out', 'credit 10', 'refund 10'])
