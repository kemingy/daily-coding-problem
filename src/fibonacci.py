# Implement the function fib(n), which returns the nth number in the Fibonacci
# sequence, using only O(1) space.


def fibonacci(n):
    x, y = 1, 1
    while n > 2:
        x, y = x + y, x
        n -= 1
    return x


if __name__ == '__main__':
    for i in range(1, 100):
        print(i, ':', fibonacci(i))
