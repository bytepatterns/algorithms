"""
Producer and Consumer: A bounded belt between the two sides.

Producers put work in a queue, consumers take it out, and neither knows the
other exists. The queue is bounded on purpose: a full queue blocks the
producer, an empty one blocks the consumer, and both sides scale
independently.

Lesson 6 of Concurrency, with the step-by-step animation, an
exercise and a quiz:
    https://bytepatterns.com/learn/concurrency/producer-consumer

Short video on this lesson: https://www.youtube.com/@bytepatterns

Run it:  python concurrency/06-producer-consumer.py
"""


import queue, threading

belt = queue.Queue(maxsize=2)         # bounded: the chef waits when it is full

def diner():
    while True:
        plate = belt.get()
        if plate is None: break       # sentinel: the belt is closing
        print("served", plate)


if __name__ == "__main__":
    t = threading.Thread(target=diner); t.start()
    for plate in ["tuna", "egg", "eel"]:
        belt.put(plate)
    belt.put(None)
    t.join()
