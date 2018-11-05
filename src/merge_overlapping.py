# Given a list of possibly overlapping intervals, return a new list of intervals
# where all overlapping intervals have been merged.

def merge_overlapping(nums):
    nums.sort()
    res = []
    last = nums[0]
    for n in nums:
        if n[0] <= last[1]:
            last = (last[0], max(last[1], n[1]))
        else:
            res.append(last)
            last = n
    res.append(last)
    return res


if __name__ == '__main__':
    print(merge_overlapping([(1, 3), (5, 8), (4, 10), (20, 25)]))