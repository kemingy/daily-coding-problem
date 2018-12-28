# Given an array of integers in which two elements appear exactly once and all
# other elements appear exactly twice, find the two elements that appear only
# once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
# The order does not matter.

# Follow-up: Can you do this in linear time and constant space?


def once_in_list(nums):
    assert len(nums) >= 2
    xor = 0

    for n in nums:
        xor ^= n

    right_most = xor & ~(xor - 1)

    x = y = 0
    for n in nums:
        if n & right_most:
            x ^= n
        else:
            y ^= n

    return x, y


if __name__ == "__main__":
    for nums in [[2, 4, 6, 8, 10, 2, 6, 10]]:
        print(once_in_list(nums))
