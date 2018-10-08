# Given a multiset of integers, return whether it can be partitioned into two 
# subsets whose sums are the same.
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return 
# true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which 
# both add up to 55.
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't 
# split it up into two subsets that add up to the same sum.


def sub_sum(nums):
    sum_of_nums = sum(nums)
    if sum_of_nums & 1:
        return False

    half = sum_of_nums // 2
    dp = [False] * (half + 1)
    dp[0] = True

    for n in nums:
        for i in range(half, n - 1, -1):
            dp[i] = dp[i] | dp[i - n]

    return dp[half]


if __name__ == '__main__':
    for nums in [[15, 5, 20, 10, 35, 15, 10], [15, 5, 20, 10, 35], [1, 5, 3], [1, 5, 11, 5]]:
        print(sub_sum(nums), nums)
