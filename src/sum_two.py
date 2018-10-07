# Given a list of numbers and a number k, return whether any two numbers from 
# the list add up to k.

def sum_k(nums, k):
    nums.sort()
    left, right = 0, len(nums) - 1

    while nums[right] > k:
        right -= 1

    while left < right:
        sum2 = nums[left] + nums[right]
        if sum2 == k:
            return True
        elif sum2 > k:
            right -= 1
        else:
            left += 1

    return False


if __name__ == '__main__':
    for nums, k in [
        ([10, 15, 3, 7], 17),
        (list(range(10)), 17),
        ([2, 4, 8], 5),
    ]:
        print('Sum2: {} -- {} {}'.format(sum_k(nums, k), k, nums))
