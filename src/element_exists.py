# Given a sorted list of integers of length N, determine if an element x is in
# the list without performing any multiplication, division, or bit-shift
# operations.

# Do this in O(log N) time.


def binary_search(nums, x):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == nums[mid]:
            return mid
        elif x > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    nums = [2, 3, 8, 12, 18, 54, 82, 1000]
    for x in [3, 1, 2, 82, 18, 2000, 7]:
        print(binary_search(nums, x))
