# Given an array of integers out of order, determine the bounds of the smallest
# window that must be sorted in order for the entire array to be sorted.
# For example, given [3, 7, 5, 6, 9], you should return (1, 3).


def unsorted_bounds(nums):
    n = len(nums)
    left, right = 0, n - 1

    i = 1
    move = True
    while i < n:
        if left < 0:
            break
        if nums[left] > nums[i]:
            left -= 1
            move = False
            continue
        if move:
            left += 1
        i += 1

    i = right - 1
    move = True
    while i > 0:
        if right >= n:
            break
        if nums[right] < nums[i]:
            right += 1
            move = False
            continue
        if move:
            right -= 1
        i -= 1

    left = 0 if left < 0 else left + 1
    right = n - 1 if right >= n else right - 1
    return left, right


if __name__ == '__main__':
    for nums in [[3, 7, 5, 6, 9], [0, 7, 3, 2, 1], [4, 2, 1, 5, 7, 8]]:
        print(unsorted_bounds(nums))
