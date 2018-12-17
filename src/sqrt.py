# Given a real number n, find the square root of n.

# For example, given n = 9, return 3.

def sqrt(x):
    last, z = x, x / 2
    for _ in range(10):
        if abs(last - z) < 1e-6:
            break

        last = z
        z -= (z*z - x) / (2*z)

    return z


if __name__ == '__main__':
    for num in [2, 4, 6, 8, 9, 10, 1234567890]:
        print('square root of {} is {}'.format(num, sqrt(num)))
