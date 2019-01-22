# Given a list of elements, find the majority element, which appears more than
# half the time (> floor(len(lst) / 2.0)).

# You can assume that such element exists.

# For example, given [1, 2, 1, 1, 3, 4, 0], return 1.


def appears_half(nums):
    n = len(nums)
    index = 0
    count = 1
    for i in range(n):
        if nums[i] == nums[index]:
            count += 1
        else:
            count -= 1
        if count == 0:
            index = i
            count = 1

    if check(nums, nums[index]):
        return nums[index]
    return None

def check(nums, target):
    length = len(nums)
    limit = length / 2.0
    count = 0
    for n in nums:
        if n == target:
            count += 1
        if count >= limit:
            return True

    return False



if __name__ == "__main__":
    for nums in [
        [1, 2, 1, 1, 3, 4, 0],
        [2, 2, 3, 1, 2, 2],
        [1, 2, 3, 4, 3, 1, 3, 3],
        [0, 0, 1, 0, 1, 0, 1, 1, 0],
    ]:
        print(nums, end=" -> ")
        print(appears_half(nums))
