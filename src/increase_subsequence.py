# Given an array of numbers, find the length of the longest increasing 
# subsequence in the array. The subsequence does not necessarily have to be 
# contiguous.


def longest_increasing_subsequence(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    return max(lis)



if __name__ == '__main__':
    print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
