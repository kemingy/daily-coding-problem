# Given an array of numbers N and an integer k, your task is to split N into k
# partitions such that the maximum sum of any partition is minimized.
# Return this sum.

# For example, given N = [5, 1, 2, 7, 3, 4] and k = 3, you should return 8,
# since the optimal partition is [5, 1, 2], [7], [3, 4].

from typing import List

class Partition:
    def __init__(self):
        self.nums = []
        self._sum = 0

    def add(self, num: int):
        self.nums.append(num)
        self._sum += num

    @property
    def sum(self) -> int:
        return self._sum

    def __repr__(self) -> str:
        return '<Partition: {}>'.format(self.nums)

def min_sum(nums: List[int], k: int) -> int:
    partitions = [Partition() for _ in range(k)]
    nums.sort(reverse=True)
    for n in nums:
        min_index = min(range(k), key=lambda x: partitions.__getitem__(x).sum)
        partitions[min_index].add(n)

    return max([x.sum for x in partitions])


if __name__ == '__main__':
    for nums, k in [
        ([5, 1, 2, 7, 3, 4], 3),
        ([1, 3, 122, 128, 110, 115, 2], 2),
    ]:
        print(min_sum(nums, k))