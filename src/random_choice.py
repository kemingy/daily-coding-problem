# You are given n numbers as well as n probabilities that sum up to 1. Write a
# function to generate one of the numbers with its corresponding probability.

# For example, given the numbers [1, 2, 3, 4] and probabilities
# [0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the time, 2 50%
# of the time, and 3 and 4 20% of the time.

# You can generate random numbers between 0 and 1 uniformly.

from random import random


def random_choice(nums, prob):
    assert len(nums) == len(prob)
    assert sum(prob) - 1 <= 1e-6

    r = random()
    for i, p in enumerate(prob):
        r -= p
        if r <= 0:
            return nums[i]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    prob = [0.1, 0.5, 0.2, 0.2]
    count = [0] * len(numbers)
    for _ in range(100000):
        count[random_choice(numbers, prob) - 1] += 1

    print(count)
