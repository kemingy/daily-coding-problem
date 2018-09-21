# We can determine how "out of order" an array A is by counting the number of 
# inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j]
# but i < j. That is, a smaller element appears after a larger element.

def merge(array, start, mid, end):
    len_left, len_right = mid - start + 1, end - mid
    left = array[start:mid+1]
    right = array[mid+1:end+1]
    i = j = 0
    for k in range(start, end+1):
        if j >= len_right or (i < len_left and left[i] <= right[j]):
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

def count_inversions(array, start=0, end=None):
    if end is None:
        end = len(array) - 1

    if start < end:
        mid = (start + end) // 2
        count = count_inversions(array, start, mid) + count_inversions(array, mid+1, end)

        cross = mid + 1
        for i in range(start, mid+1):
            while cross <= end and array[i] > array[cross]:
                cross += 1
            count += cross - mid - 1

        merge(array, start, mid, end)
        return count
    return 0


if __name__ == '__main__':
    for array in [[2, 4, 1, 3, 5], [5, 4, 3, 2, 1], list(range(10))]:
        print('Inversion of {}'.format(array), end=' ')
        print('is {}'.format(count_inversions(array)))
