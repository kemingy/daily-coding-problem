# You are given an N by M matrix of 0s and 1s. Starting from the top left
# corner, how many ways are there to reach the bottom right corner?

# You can only move right and down. 0 represents an empty space while 1
# represents a wall you cannot walk through.

# For example, given the following matrix:

# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]

# Return two, as there are only two ways to get to the bottom right:

# •	Right, down, down, right
# •	Down, right, down, right

# The top left corner and bottom right corner will always be 0.


def ways_get_out(matrix):
    ways = []
    m = len(matrix)
    n = len(matrix[0])

    def move(x=0, y=0, d='', path=None):
        if x >= m or y >= n:
            return
        if matrix[x][y] == 1:
            return
        path = path if path is not None else []
        if d:
            path.append(d)
        if x == m - 1 and y == n - 1:
            ways.append(path)

        move(x + 1, y, 'down', path.copy())
        move(x, y + 1, 'right', path)

    move()
    return ways

if __name__ == "__main__":
    matrix = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
    for way in ways_get_out(matrix):
        print(way)
