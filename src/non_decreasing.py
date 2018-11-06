# Given an array of integers, write a function to determine whether the array
# could become non-decreasing by modifying at most 1 element.


def non_decreasing_with_1(nums):
    modified = False
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i + 1]:
            continue
        if not modified:
            nums[i] = nums[i + 1]
            modified = True
        else:
            return False

    return True


if __name__ == '__main__':
    for nums in [[10, 5, 7], [10, 5, 1], [2, 2, 3, 2, 4], [1, 1, 2, 1]]:
        print(nums, end=' -> ')
        print('{}: {}'.format(nums, non_decreasing_with_1(nums)))