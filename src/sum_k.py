# Given a list of integers S and a target number k, write a function that 
# returns a subset of S that adds up to k. If such a subset cannot be made,
# then return null.

def sum_k(array, k):
    array = list(filter(lambda x: x < k, sorted(array)))

    def is_subset_sum_k(i, k, path):
        if i < 0:
            return None

        if array[i] == k:
            return path + [array[i]]

        return is_subset_sum_k(i - 1, k, path) or \
                is_subset_sum_k(i - 1, k - array[i], path + [array[i]])

    return is_subset_sum_k(len(array) - 1, k, [])

if __name__ == '__main__':
    for arr, k in [([12, 1, 61, 5, 9, 2], 24), ([2, 3, 4, 5], 13)]:
        print('{} subset sum({})={}'.format(arr, sum_k(arr, k), k))
