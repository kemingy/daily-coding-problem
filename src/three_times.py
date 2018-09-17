# Given an array of integers where every integer occurs three times except for
# one integer, which only occurs once, find and return the non-duplicated integer.

INT_SIZE = 32

def once(array):
    count = [0] * INT_SIZE
    for a in array:
        index = INT_SIZE - 1
        while a:
            if a & 1:
                count[index] += 1
            index -= 1
            a >>= 1

    ans = int(''.join([str(c % 3) for c in count]), 2)
    return ans


if __name__ == '__main__':
    for array in [[6, 1, 3, 3, 3, 6, 6], [13, 19, 13, 13]]:
        print('Once in {} is {}.'.format(array, once(array)))
