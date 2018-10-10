# Given a 2D matrix of characters and a target word, write a function that 
# returns whether the word can be found in the matrix by going left-to-right, 
# or up-to-down.


def word_in_matrix(matrix, word):
    assert matrix
    assert word
    row, col = len(matrix), len(matrix[0])

    def get_start_point():
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == word[0]:
                    yield i, j

    def search(i, j, index):
        if index >= len(word):
            return True
        elif i >= row or j >= col:
            return False
        elif word[index] == matrix[i][j]:
            return any([search(i + 1, j, index + 1), search(i, j + 1, index + 1)])
        else:
            return False

    return any([search(i, j, 0) for i, j in get_start_point()])


if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']
    ]
    for word in ['FOAM', 'MASS', 'OBS', 'BNAM']:
        print('find word "{}": {}'.format(word, word_in_matrix(matrix, word)))
