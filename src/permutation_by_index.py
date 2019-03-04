# A permutation can be specified by an array P, where P[i] represents the
# location of the element at i in the permutation. For example, [2, 1, 0]
# represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array.
# For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
# return ["c", "b", "a"].

def permutate(array, index):
    return [x for y, x in sorted(zip(index, array))]


if __name__ == '__main__':
    for array, index in [
        (['a', 'b', 'c'], [2, 1, 0]),
        (['a', 'b', 'c', 'd'], [3, 0, 2, 1])
    ]:
        print('[ ]', array)
        print('[x]', permutate(array, index))