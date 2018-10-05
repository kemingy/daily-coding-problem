# An sorted array of integers was rotated an unknown number of times.
# Given such an array, find the index of the element in the array in faster than
# linear time. If the element doesn't exist in the array, return null.


def search_rotated(array, target):
    if not array:
        return -1

    left, right = 0, len(array) - 1
    head = array[0]
    while left < right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        if (head > target) ^ (head > array[mid]) ^(target > array[mid]):
            left = mid + 1
        else:
            right = mid

    return left if target == array[left] else -1



if __name__ == '__main__':
    for array, target in [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([13, 18, 25, 2, 8, 10], 8),
    ]:
        index = search_rotated(array, target)
        if index >= 0:
            print('"{}" is in the {}-th of {}'.format(target, index, array))
        else:
            print('"{}" is not in {}'.format(target, array))
