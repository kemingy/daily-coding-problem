# You are given a 2-d matrix where each cell represents number of coins in that 
# cell. Assuming we start at matrix[0][0], and can only move right or down, find 
# the maximum number of coins you can collect by the bottom right corner.

# For example, in this matrix
# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


def most_coins(matrix):
    m, n = len(matrix), len(matrix[0])

    def helper(i, j):
        if i >= m or j >= n:
            return 0
        return matrix[i][j] + max(helper(i + 1, j), helper(i, j + 1))

    return helper(0, 0)


if __name__ == '__main__':
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1],
    ]
    print(most_coins(matrix))