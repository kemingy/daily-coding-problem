# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array 
# except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would 
# be [2, 3, 6].


def product_except_self(nums):
    n = len(nums)
    p = 1
    output = []

    for i in range(n):
        output.append(p)
        p *= nums[i]

    p = 1
    for i in range(n - 1, -1, -1):
        output[i] *= p
        p *= nums[i]

    return output


if __name__ == '__main__':
    for nums in [[1,2,3,4,5], [3,2,1]]:
        print('Product except self of {} is {}.'.format(nums, product_except_self(nums)))
