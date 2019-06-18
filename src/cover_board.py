# You are given a 2 x N board, and instructed to completely cover the board
# with the following shapes:

# •	Dominoes, or 2 x 1 rectangles.
# •	Trominoes, or L-shapes.

# For example, if N = 4, here is one possible configuration, where A is a
# domino, and B and C are trominoes.

# A B B C
# A B C C

# Given an integer N, determine in how many ways this task is possible.


def cover_board(n):
    ways = []

    def helper(n, path):
        if n < 3:
            path += ['Dominoes'] * n
            ways.append(path)
            return
        helper(n-1, path+['Dominoes'])
        helper(n-3, path+['Trominoes', 'Trominoes'])

    helper(n, [])
    return ways


if __name__ == '__main__':
    for n in [2, 4, 8, 10]:
        print(n, cover_board(n))
