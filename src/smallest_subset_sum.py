# Given a sorted array, find the smallest positive integer that is not the sum
# of a subset of the array.

# For example, for the input [1, 2, 3, 10], you should return 7.

# Do this in O(N) time.


def smallest_positive_not_sum(nums):
    ans = 1
    for n in nums:
        if n <= ans:
            ans += n
        else:
            break
    return ans


if __name__ == '__main__':
    for nums in [[1, 2, 3, 10],
                 [1, 2, 3, 4, 5],
                 [2, 3, 5],
                 [1, 1, 1, 1],
                 [1, 2, 6, 10, 11, 15],
                 [1, 2, 3, 6, 10, 20, 40]]:
        print(nums, smallest_positive_not_sum(nums))
