# Assume you have access to a function toss_biased() which returns 0 or 1 with a 
# probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the 
# bias of the coin.
# Write a function to simulate an unbiased coin toss.


import random

p = random.random()

def bias():
    r = random.random()
    if r < p:
        return 0
    return 1


def unbiased_coin():
    while True:
        x = bias()
        y = bias()
        if x != y:
            return x


if __name__ == '__main__':
    count = [0, 0]
    for _ in range(100000):
        count[unbiased_coin()] += 1

    print(count)