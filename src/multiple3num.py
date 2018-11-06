# Given a list of integers, return the largest product that can be made by 
# multiplying any three integers.


def max_multiple(nums):
    assert len(nums) >= 3

    max_heap = [-float('inf')] * 3
    min_heap = [float('inf')] * 3

    for n in nums:
        for i in range(3):
            if n > max_heap[i]:
                max_heap[i], n = n, max_heap[i]

    for n in nums:
        for i in range(3):
            if n < min_heap[i]:
                min_heap[i], n = n, min_heap[i]

    return max(
        max_heap[0] * max_heap[1] * max_heap[2],
        max_heap[0] * min_heap[0] * min_heap[1],
    )




if __name__ == '__main__':
    for nums in [
            [-10, -10, 5, 2], 
            [10, -10, 5, 2], 
            [1, 4, 2, -9, -1], 
            [-1, -2, -3, -4], 
            [5, -4, -3, -5, -6],
            [8, 7, -1, -2, -3, -4],
            [-2, -1, -4, -5],
    ]:
        print('max 3 numbers multiple of {} is {}'.format(nums, max_multiple(nums)))
