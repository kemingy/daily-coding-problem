# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]


def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    ans = []
    if len(matrix) < 1:
        return ans
    
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        # left -> right
        for i in range(col_start, col_end + 1):
            ans.append(matrix[row_start][i])
        row_start += 1
        
        # up -> down
        for i in range(row_start, row_end + 1):
            ans.append(matrix[i][col_end])
        col_end -= 1
            
        # right -> left
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                ans.append(matrix[row_end][i])
        row_end -= 1
        
        # down -> up
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                ans.append(matrix[i][col_start])
        col_start += 1
        
    return ans


if __name__ == '__main__':
    # matrix = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    # ]
    matrix = [
        [1, 2],
        [3, 4],
    ]
    print(spiralOrder(matrix))
