# You are given an array of length n + 1 whose elements belong to the set
# {1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.

# Find it in linear time and space.

from random import random, shuffle


def duplicate(nums):
    return sum(nums) - sum(range(1, len(nums)))


if __name__ == "__main__":
    for _ in range(10):
        nums = list(range(1, 1001))
        dup = int(1000 * random())
        nums.append(dup)
        shuffle(nums)
        print("{} -> {}".format(dup, duplicate(nums)))
