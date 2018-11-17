# Given a number represented by a list of digits, find the next greater 
# permutation of a number, in terms of lexicographic ordering. If there is not 
# greater permutation possible, return the permutation with the lowest 
# value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should 
# return [2,1,3]. The list [3,2,1] should return [1,2,3].


def next_permutation(nums):
    assert nums
    n = len(nums)
    end = nums[-1]
    start = 0
    for i in range(n - 2, -1, -1):
        if end > nums[i]:
            start = i
            break

    nums[start], nums[-1] = nums[-1], nums[start]
    nums[start+1:end+1] = sorted(nums[start+1:end+1])


if __name__ == '__main__':
    for nums in [
        [1, 2, 3],
        [1, 3, 2],
        [3, 2, 1],
    ]:
        print(nums, end=': ')
        next_permutation(nums)
        print(nums)