# Given an unsorted array, in which all elements are distinct, find a "peak"
# element in O(log N) time.

# An element is considered a peak if it is greater than both its left and right
# neighbors. It is guaranteed that the first and last elements are lower than
# all others.


def peak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return nums[mid]
        elif nums[mid] < nums[mid-1]:
            right = mid
        elif nums[mid] < nums[mid+1]:
            left = mid


if __name__ == '__main__':
    for nums in [[4, 23, 24, 19, 8], [1, 3, 5, 8, 9, 2], [2, 7, 5, 10, 11, 1]]:
        print(peak(nums))
