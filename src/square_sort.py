# Given a sorted list of integers, square the elements and give the output
# in sorted order.


def sort_square(nums):
    i = j = 0

    for n in nums:
        if n >= 0:
            break
        i += 1

    ans = []
    j = i - 1
    while j >= 0 and i < len(nums):
        if nums[i] ** 2 < nums[j] ** 2:
            ans.append(nums[i] ** 2)
            i += 1
        else:
            ans.append(nums[j] ** 2)
            j -= 1

    while j >= 0:
        ans.append(nums[j] ** 2)
        j -= 1

    while i < len(nums):
        ans.append(nums[i] ** 2)
        i += 1

    return ans


if __name__ == '__main__':
    for nums in [[-9, -2, 0, 2, 3], [1, 2, 3], [-3, -1, 4]]:
        print(nums, end=' -> ')
        print(sort_square(nums))
