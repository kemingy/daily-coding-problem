# A fixed point in an array is an element whose value is equal to its index.
# Given a sorted array of distinct elements, return a fixed point, if one
# exists.
# Otherwise, return False.

# For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8],
# you should return False.


def fixed_point(nums):
    for i, n in enumerate(nums):
        if i == n:
            return i
    return False


if __name__ == "__main__":
    for nums in [[-6, 0, 2, 40], [1, 5, 7, 8]]:
        print(fixed_point(nums))
