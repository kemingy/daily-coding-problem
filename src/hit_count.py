# Design and implement a HitCounter class that keeps track of requests (or hits).
# It should support the following operations:

# •	record(timestamp): records a hit that happened at timestamp 
# •	total(): returns the total number of hits recorded 
# •	range(lower, upper): returns the number of hits that occurred between 
#     timestamps lower and upper (inclusive)

# Follow-up: What if our system has limited memory?  => quantization?

import random
import time


class HitCounter:
    def __init__(self):
        self.history = []

    def record(self, t):
        self.history.append(t)

    def total(self):
        return len(self.history)

    def range(self, lower, upper):
        assert lower <= upper
        return self.index(upper) - self.index(lower)

    def index(self, value):
        left, right = 0, len(self.history) - 1
        mid = right // 2

        while left < right:
            if value < self.history[mid]:
                right = mid
            elif value > self.history[mid]:
                left = mid
            else:
                return mid

            next_mid = (left + right) // 2
            if mid == next_mid:
                break
            mid = next_mid

        return mid


if __name__ == '__main__':
    hc = HitCounter()

    for _ in range(10):
        time.sleep(random.random() / 10)
        hc.record(time.time())

    print(hc.total())
    lower = time.time() - 0.5
    upper = time.time() - 0.2
    print(lower, upper)
    print(hc.history)
    print(hc.range(lower, upper))
