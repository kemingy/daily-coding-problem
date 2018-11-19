# Given a list of integers and a number K, return which contiguous elements of 
# the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should 
# return [2, 3, 4].

def contiguous_sum_k(nums, k):
    candidates = []
    summary = 0

    i = 0
    while i < len(nums):
        if summary == k:
            return candidates
        elif summary < k:
            candidates.append(nums[i])
            summary += nums[i]
            i += 1
        else:
            summary -= candidates.pop(0)

    return None


if __name__ == '__main__':
    print(contiguous_sum_k([1, 2, 3, 4, 5], 9))