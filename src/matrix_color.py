# Given a 2-D matrix representing an image, a location of a pixel in the screen
# and a color C, replace the color of the given pixel and all adjacent same
# colored pixels with C.

# For example, given the following matrix, and location pixel of (2, 2), and
# 'G' for green:

# B B W
# W W W
# W W W
# B B B

# Becomes

# B B G
# G G G
# G G G
# B B B


def bucket_paint(matrix, x, y, color):
    m = len(matrix)
    n = len(matrix[0])
    assert 0 <= x < m
    assert 0 <= y < n

    if matrix[x][y] == color:
        return

    def paint(i, j, source, target):
        if i < 0 or i >= m:
            return
        if j < 0 or j >= n:
            return
        if matrix[i][j] != source:
            return

        matrix[i][j] = target
        paint(i - 1, j, source, target)
        paint(i + 1, j, source, target)
        paint(i, j - 1, source, target)
        paint(i, j + 1, source, target)

    paint(x, y, matrix[x][y], color)


def display(matrix):
    for vec in matrix:
        print(vec)
    print()


if __name__ == "__main__":
    matrix = [["B", "B", "W"], ["W", "W", "W"], ["W", "W", "W"], ["B", "B", "B"]]
    display(matrix)
    bucket_paint(matrix, 2, 2, "G")
    display(matrix)
