# estimate pi to 3 decimal places using a Monte Carlo method.

from random import random

def estimate_pi():
    count = 0
    n = 10000000
    for _ in range(n):
        x, y = random(), random()
        if x ** 2 + y ** 2 < 1:
            count += 1

    return 4 * count / n


if __name__ == '__main__':
    print(estimate_pi())
