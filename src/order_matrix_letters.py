# You are given an N by M 2D matrix of lowercase letters. Determine the minimum 
# number of columns that can be removed to ensure that each row is ordered from 
# top to bottom lexicographically. That is, the letter at each column is 
# lexicographically later as you go down each row. It does not matter whether 
# each row itself is ordered lexicographically.


def removed_count(matrix):
    count = 0
    for j in range(len(matrix[0])):
        for i in range(1, len(matrix)):
            if matrix[i - 1][j] > matrix[i][j]:
                count += 1
                break

    return count


if __name__ == '__main__':
    for matrix in [
        ['cba', 'daf', 'ghi'],
        ['abcdef'],
        ['zyx', 'wvu', 'tsr'],
    ]:
        print(removed_count(matrix))
