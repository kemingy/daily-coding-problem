# Suppose you have a multiplication table that is N by N. That is, a 2D array 
# where the value at the i-th row and j-th column is (i + 1) * (j + 1) 
# (if 0-indexed) or i * j (if 1-indexed).
# Given integers N and X, write a function that returns the number of times X 
# appears as a value in an N by N multiplication table.


def count_appearance(n, x):
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            multip = i * j
            if multip > x:
                break
            if multip == x:
                count += 1
                break

    return count



if __name__ == '__main__':
    print(count_appearance(6, 12))
