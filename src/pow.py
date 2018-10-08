# Implement integer exponentiation. That is, implement the pow(x, y) function,
# where x and y are integers and returns x^y.
# Do this faster than the naive method of repeated multiplication.


def quick_pow(x, y):
    ans = 1
    while y:
        if y & 1:
            ans *= x
        y >>= 1
        x *= x

    return ans


if __name__ == '__main__':
    print(pow(2, 10))
    print(pow(5, 5))
