# Given an integer list where each number represents the number of hops you can 
# make, determine whether you can reach to the last index starting at index 0.

def reachable(nums):
    index = 0
    while index != len(nums) - 1:
        if nums[index] == 0:
            return False

        index += nums[index]
        if index >= len(nums):
            return False

    return True


if __name__ == '__main__':
    for nums in [[2, 0, 1, 0], [1, 1, 0, 1]]:
        print(nums, ':', reachable(nums))