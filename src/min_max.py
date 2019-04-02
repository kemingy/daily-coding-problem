# Given an array of numbers of length N, find both the minimum and maximum
# using less than 2 * (N - 2) comparisons.


from random import randint


class Compare:
    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum

    def __repr__(self):
        return '<Compare>--<min: {}><max: {}>'.format(self.min, self.max)


def min_max(nums):
    n = len(nums)
    assert n > 1
    if n & 1:
        cmp = Compare(nums[0], nums[0])
        i = 1
    else:
        if nums[0] > nums[1]:
            cmp = Compare(nums[1], nums[0])
        else:
            cmp = Compare(nums[0], nums[1])
        i = 2

    while i < n - 1:
        if nums[i] < nums[i+1]:
            cmp.min = min(cmp.min, nums[i])
            cmp.max = max(cmp.max, nums[i+1])
        else:
            cmp.min = min(cmp.min, nums[i+1])
            cmp.max = max(cmp.max, nums[i])
        i += 1

    return cmp


if __name__ == '__main__':
    nums = [randint(0, 1000) for _ in range(100)]
    print(min_max(nums))
    print(min(nums), max(nums))
