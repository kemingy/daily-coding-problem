# You are given a list of N numbers, in which each number is located at most k
# places away from its sorted position. For example, if k = 1, a given element
# at index 4 might end up at indices 3, 4, or 5.

# Come up with an algorithm that sorts this list in O(N log k) time.


from heapq import heapify, heappop, heappush


def k_sort(nums, k):
    heap = nums[:k+1]
    heapify(heap)
    target_index = 0
    for i in range(k+1, len(nums)):
        nums[target_index] = heappop(heap)
        heappush(heap, nums[i])
        target_index += 1

    while heap:
        nums[target_index] = heappop(heap)
        target_index += 1

    return nums


if __name__ == '__main__':
    for nums, k in [([2, 6, 3, 12, 56, 8], 3),
                    ([10, 9, 8, 7, 4, 70, 60, 50], 4)]:
        print(nums)
        k_sort(nums, k)
        print(nums)
