# You have an N by N board. Write a function that, given N, returns the number 
# of possible arrangements of the board where N queens can be placed on the 
# board without threatening each other, i.e. no two queens share the same row, 
# column, or diagonal


def nonattacking_queens(n, board=[]):
    if len(board) == n:
        return 1

    count = 0
    for col in range(n):
        if check_board(board, col):
            board.append(col)
            count += nonattacking_queens(n, board)
            board.pop()

    return count


def check_board(board, col):
    cur_row = len(board)
    for r, c in enumerate(board):
        diff = abs(col - c)
        # 1. in the same colume  2. in the same diagonal (abs(x1-x2)==abs(y1-y2))
        if diff == 0 or diff == cur_row - r:
            return False

    return True


if __name__ == '__main__':
    for n in range(1, 10):
        print('There are {} possible arrangements of board {}x{}.'.format(
                nonattacking_queens(n), n, n))
