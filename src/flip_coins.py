# You have 100 fair coins and you flip them all at the same time. Any that come 
# up tails you set aside. The ones that come up heads you flip again. How many 
# rounds do you expect to play before only one coin remains?

# Write a function that, given n, returns the number of rounds you'd expect 
# to play until one coin remains.

from random import random
from math import log2


def expect_round(n):
    def helper(heads):
        count = 0
        while heads > 1:
            heads = sum([1 if random() > 0.5 else 0 for _ in range(heads)])
            count += 1
        return count

    total = 0
    rounds = 10000
    for _ in range(rounds):
        total += helper(n)

    return total / rounds


if __name__ == '__main__':
    for n in [10 ** i for i in range(1, 5)]:
        print(n, expect_round(n), log2(n))
