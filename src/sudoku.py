# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with 
# digits. The objective is to fill the grid with the constraint that every row, 
# column, and box (3 by 3 subgrid) must contain all of the digits from 1 to 9.


def sudoku(grid):
    def is_valid(i, j, v):
        for index in range(9):
            if grid[i][index] == cand:
                return False
            if grid[index][j] == cand:
                return False
            if grid[3 * (i // 3) + index // 3][3 * (j // 3) + index % 3] == cand:
                return False
        return True


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                for cand in range(1, 10):
                    if is_valid(i, j, cand):
                        grid[i][j] = cand

                        if sudoku(grid):
                            return True
                        else:
                            grid[i][j] = 0

                return False

    return True



if __name__ == '__main__':
    grid=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]

    from pprint import pprint
    if sudoku(grid):
        pprint(grid)
    else:
        print('Can not solve it.')
