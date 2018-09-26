# Given an array of numbers, find the maximum sum of any contiguous subarray of 
# the array.


def max_sum(array):
    maximum, cur = 0, 0
    for a in array:
        cur = max(0, cur + a)
        maximum = max(maximum, cur)

    return maximum


if __name__ == '__main__':
    for array in [
            [34, -50, 42, 14, -5, 86],
            [-5, -1, -8, -9],
            [-2, -3, 4, -1, -2, 1, 5, -3]]:
        print('Maximum sum of contiguous subarray of {} is {}'.format(
            array, max_sum(array)
        ))
