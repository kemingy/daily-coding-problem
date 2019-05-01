# Find the maximum of two numbers without using any if-else statements,
# branching, or direct comparisons.


import sys

def maximum(x, y):
    diff = x - y
    return x - (diff & (diff >> (sys.getsizeof(diff) - 1)))


if __name__ == '__main__':
    for x, y in [
        (21, 5), (2, 19), (-2, -5), (-12, -3),
        (-2, 5), (5, -2), (-9, 2), (2, -9),
    ]:
        print(x, y, '->', maximum(x, y))
