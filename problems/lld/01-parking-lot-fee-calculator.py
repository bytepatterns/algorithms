"""
Parking Lot Fee Calculator (easy) · patterns: class-design, pricing-rules

Design the pricing part of a parking lot as a small class. It is built with
a rate table, mapping each vehicle kind to a price for the first hour and a
price for every further started hour, and a daily cap per kind. fee(kind,
minutes) returns what a stay costs: stays of 15 minutes or less are free,
every full 24 hours costs exactly the daily cap, and the remaining part of a
day is priced by the hourly rates but never above the cap. An unknown
vehicle kind must raise a ValueError rather than be priced as something
else.

Examples:

    Input:  rates = car (4, 2), motorbike (2, 1); caps = car 20, motorbike 8
            fee("car", 150)
    Output: 8
    Why:    first hour 4, then 90 more minutes start 2 more hours at 2 each

    Input:  same lot, fee("car", 26 * 60)
    Output: 26
    Why:    one full day at the cap of 20, then 2 hours for 4 + 2

    Input:  same lot, fee("motorbike", 10)
    Output: 0
    Why:    edge case, the stay is inside the 15-minute grace period

Approach:
    The class holds data, the rate table and the caps, and one method
    applies the rules, so adding a van is a change to the table rather than
    to the code. A stay splits into whole days, each worth exactly the cap,
    and a remainder that goes through the hourly rule: the first hour, then
    every started hour after it, rounded up with negated floor division and
    capped for the day. The grace period is checked against the whole stay,
    so the 10 minutes after a full day are billed as a started hour instead
    of slipping through as grace. Raising on an unknown kind keeps a typo
    from being billed at some default rate. Each call is O(1).

The lesson behind it: Designing a Parking Lot
    https://bytepatterns.com/learn/lld/designing-a-parking-lot
    python lld/10-designing-a-parking-lot.py

Try it first with progressive hints on the site:
    https://bytepatterns.com/practice/lld/parking-lot-fee-calculator

Run it:  python problems/lld/01-parking-lot-fee-calculator.py
"""


class FeeSchedule:
    GRACE, HOUR, DAY = 15, 60, 24 * 60

    def __init__(self, rates, daily_cap):
        self.rates = rates                 # kind -> (first hour, each further hour)
        self.daily_cap = daily_cap

    def fee(self, kind, minutes):
        if kind not in self.rates:
            raise ValueError("unknown vehicle kind: " + kind)
        if minutes <= self.GRACE:
            return 0
        days, rest = divmod(minutes, self.DAY)
        first, extra = self.rates[kind]
        started = -(-max(0, rest - self.HOUR) // self.HOUR)      # started hours after the first
        part = min(self.daily_cap[kind], first + extra * started) if rest else 0
        return days * self.daily_cap[kind] + part


# ---------------------------------------------------------------------------
# Self-check: the example below prints the output its page on
# bytepatterns.com states, and `python run_all.py` fails if it ever drifts.

def check(value, expected):
    """Print the value, then assert it is what the lesson says it is."""
    print(value)
    assert value == expected, f"expected {expected!r}, got {value!r}"


if __name__ == "__main__":
    lot = FeeSchedule({"car": (4, 2), "motorbike": (2, 1)}, {"car": 20, "motorbike": 8})
    check(lot.fee("car", 150), 8)
    check(lot.fee("car", 26 * 60), 26)
    check(lot.fee("motorbike", 10), 0)
    check(lot.fee("car", 24 * 60 + 10), 24)
