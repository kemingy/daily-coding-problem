# Given an array of integers, find the first missing positive integer in linear 
# time and constant space. In other words, find the lowest positive integer that 
# does not exist in the array. The array can contain duplicates and negative 
# numbers as well.


def min_positive(nums):
    n = len(nums)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            continue

        val = nums[i]
        while nums[val - 1] != val:
            next_val = nums[val - 1]
            nums[val - 1] = val
            val = next_val
            # val, nums[val - 1] = nums[val - 1], val
            # this can cause problems because val is alse index...
            if val <= 0 or val > n:
                break

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    for nums in [[3, 4, -1, 1], [1, 2, 0], [1, 1, 2, 4]]:
        print('Min positive number in {} is '.format(nums), end='')
        print(min_positive(nums))
