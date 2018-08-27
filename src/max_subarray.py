# Given an array of integers and a number k, where 1 <= k <= length of the array, 
# compute the maximum values of each subarray of length k.

from collections import deque

def max_subarray(array, k):
    assert 1 <= k <= len(array)

    dq = deque()

    for i, n in enumerate(array[:k]):
        while dq and n >= array[dq[-1]]:
            dq.pop()

        dq.append(i)

    for i, n in enumerate(array[k:], k):
        yield array[dq[0]]

        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and n >= array[dq[-1]]:
            dq.pop()

        dq.append(i)

    yield array[dq[0]]


if __name__ == '__main__':
    print(list(max_subarray([100, 1, 78, 60, 57, 89, 56], 3)))
