# A knight's tour is a sequence of moves by a knight on a chessboard such that 
# all squares are visited once.
# Given N, write a function to return the number of knight's tours on an N by N 
# chessboard.

from pprint import pprint

def knight_tour(n):
    board = [[-1 for i in range(n)] for j in range(n)]
    horizontal = [2, 1, -1, -2, -2, -1, 1, 2]
    vertical = [1, 2, 2, 1, -1, -2, -2, -1]

    board[0][0] = 0

    def tour(x, y, step):
        if step == n * n:
            return True
        for i in range(8):
            next_x, next_y = x + horizontal[i], y + vertical[i]
            if 0 <= next_x < n and 0 <= next_y < n and board[next_x][next_y] < 0:
                board[next_x][next_y] = step
                if tour(next_x, next_y, step + 1):
                    return True
                board[next_x][next_y] = -1

    if not tour(0, 0, 1):
        print('Solution does not exist when n is {}'.format(n))
    else:
        pprint(board)


if __name__ == '__main__':
    for i in range(3, 8):
        knight_tour(i)
