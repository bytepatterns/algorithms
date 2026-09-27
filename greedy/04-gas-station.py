"""
Gas Station: One pass picks the start, because every failed prefix is proof.

Each station gives you gas[i] and charges cost[i] to reach the next one, so
only the difference matters.

Sweep once with two totals. The running tank tests the current candidate
start; the grand total tests whether any loop is possible. When the tank
dips below zero at station i, no station from the candidate up to i can work
either, so jump the start to i + 1 and reset. If the grand total ends
non-negative, the surviving start is the answer.

Lesson 4 of Greedy, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/greedy/gas-station

Run it:  python greedy/04-gas-station.py
"""


if __name__ == "__main__":
    gas  = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    total = tank = start = 0
    for i in range(len(gas)):
        step = gas[i] - cost[i]
        total += step
        tank += step
        if tank < 0:                  # station i+1 is out of range from start
            start, tank = i + 1, 0    # so every earlier candidate fails too
    print(start if total >= 0 else -1)
