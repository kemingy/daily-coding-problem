# Given an N by M matrix consisting only of 1's and 0's, find the largest
# rectangle containing only 1's and return its area.

# For example, given the following matrix:

# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]

# Return 4.


def largest_rectangle(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    ans = 0
    left = [0] * n
    right = [n] * n
    height = [0] * n

    for i in range(m):
        cur_left = 0
        cur_right = n
        for j in range(n):
            if matrix[i][j] == 1:
                height[j] += 1
                left[j] = max(left[j], cur_left)
            else:
                height[j] = 0
                left[j] = 0
                cur_left = j + 1

        for j in range(n-1, -1, -1):
            if matrix[i][j] == 1:
                right[j] = min(right[j], cur_right)
            else:
                right[j] = n
                cur_right = j

        for j in range(n):
            ans = max(ans, (right[j] - left[j]) * height[j])

    return ans


if __name__ == "__main__":
    matrix = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
    print(largest_rectangle(matrix))
