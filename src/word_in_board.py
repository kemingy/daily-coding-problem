# Given a 2D board of characters and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where 
# "adjacent" cells are those horizontally or vertically neighboring. The same 
# letter cell may not be used more than once.

def word_in_board(board, word):
    if not word or not board:
        return False

    path = []
    row = len(board)
    col = len(board[0])

    def search(i, j, pos, checked=[]):
        checked.append((i, j))

        if pos >= len(word):
            path.append(checked)
            return

        for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < row and 0 <= y < col:
                if board[x][y] == word[pos] and (x, y) not in checked:
                    search(x, y, pos+1, checked)

    for i in range(row):
        for j in range(col):
            if board[i][j] == word[0]:
                search(i, j, 1)

    return len(path) > 0



if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E'],
    ]
    for word in ['ABCCED', 'SEE', 'ABCB']:
        print(word_in_board(board, word))