# Pascal's triangle is a triangular array of integers constructed with the
# following formula:

# •	The first row consists of the number 1.
# •	For each subsequent row, each element is the sum of the numbers directly
#   above it, on either side.

# For example, here are the first few rows:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Given an input k, return the kth row of Pascal's triangle.

# Bonus: Can you do this using only O(k) space?


def pascal(k):
    if k == 0:
        return [1]
    pre = pascal(k-1)
    return [1] + [pre[i] + pre[i+1] for i in range(len(pre) - 1)] + [1]


if __name__ == "__main__":
    for i in range(10):
        print(pascal(i))
