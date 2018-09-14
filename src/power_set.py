# The power set of a set is the set of all its subsets. Write a function that,
# given a set, generates its power set.


def power_set(array):
    ans = []

    def helper(array, n):
        if n == 0:
            return [[]]
        elif n == 1:
            return [[a] for a in array]
        else:
            for i in range(len(array) - n + 1):
                for a in array:
                    return [[a] + sub for sub in helper(array[i + 1:], n - 1)]

    for i in range(len(array) + 1):
        for e in helper(array, i):
            ans.append(e)

    return ans


if __name__ == '__main__':
    for array in [[1, 2, 3], [0], [1, 3, 5, 7, 9]]:
        print('The power set of "{}" is "{}"'.format(array, power_set(array)))
