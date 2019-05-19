# Given an array of integers, determine whether it contains a Pythagorean
# triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the
# equation a^2 + b^2= c^2.


def pythagorean_triplet(nums):
    nums = sorted([n*n for n in nums])
    for i in range(len(nums)-1, 1, -1):
        j, k = 0, i-1
        while j < k:
            if nums[j] + nums[k] == nums[i]:
                return '{} + {} = {}'.format(nums[j], nums[k], nums[i])
            elif nums[j] + nums[k] > nums[i]:
                k -= 1
            else:
                j += 1
    return False


if __name__ == "__main__":
    for nums in [
        [1, 2, 3, 4, 5, 6],
        [3, 12, 8, 5, 13],
        [100, 233, 456, 199],
    ]:
        print(pythogorean_triplet(nums))
