# Given three 32-bit integers x, y and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or 0.

def x_or_y(x, y, b):
    return x * b + y * (1 - b)


if __name__ == '__main__':
    for x, y, b in [(2, 3, 0), (2, 1, 1)]:
        print(x_or_y(x, y, b))
