# There is an N by M matrix of zeroes. Given N and M, write a function to count 
# the number of ways of starting at the top-left corner and getting to the 
# bottom-right corner. You can only move right or down.


def ways_of_matrix(n, m):
    if n == 1 and m == 1:
        return 1
    elif n > 1 and m > 1:
        return ways_of_matrix(n - 1, m) + ways_of_matrix(n, m - 1)
    elif n > 1 and m == 1:
        return ways_of_matrix(n - 1, m)
    elif n == 1 and m > 1:
        return ways_of_matrix(n, m - 1)



if __name__ == '__main__':
    for n, m in [(2, 2), (5, 5)]:
        print('There are {} ways in {}x{} matrix.'.format(ways_of_matrix(n, m), n, m))
