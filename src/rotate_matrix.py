# Given an N by N matrix, rotate it by 90 degrees clockwise.

# For example, given the following matrix:

# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# you should return:

# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

# Follow-up: What if you couldn't use any extra space?


def rotate(matrix):
    n = len(matrix)
    for i in range(n // 2 + 1):
        for j in range(i, n - i - 1):
            print(i, j)
            (
                matrix[j][n - 1 - i],
                matrix[n - i - 1][n - j - 1],
                matrix[n - 1 - j][i],
                matrix[i][j],
            ) = (
                matrix[i][j],
                matrix[j][n - 1 - i],
                matrix[n - i - 1][n - j - 1],
                matrix[n - 1 - j][i],
            )

            for vec in matrix:
                print(vec)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    for vec in matrix:
        print(vec)
