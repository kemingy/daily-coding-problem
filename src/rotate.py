# Write a function that rotates a list by k elements. For example,
# [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. Try solving
# this without creating a copy of the list. How many swap or move operations
# do you need?

def rotate(nums, k):
    n = len(nums)
    k %= n

    count = 0
    for i in range(n):
        x, y = i, (i - k) % n
        tmp = nums[x]
        while True:
            tmp, nums[y] = nums[y], tmp
            x, y = y, (y - k) % n
            count += 1
            if x == i:
                break

        if count == n:
            break


if __name__ == '__main__':
    for k in range(1, 6):
        nums = [1, 2, 3, 4, 5, 6]
        print(f'{nums} rotate {k} is', end=': ')
        rotate(nums, k)
        print(nums)
