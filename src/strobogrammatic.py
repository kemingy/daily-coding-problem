# A strobogrammatic number is a positive number that appears the same after
# being rotated 180 degrees. For example, 16891 is strobogrammatic.

# Create a program that finds all strobogrammatic numbers with N digits.


TABLE = str.maketrans('01689', '01986')


def is_strobogrammatic(n):
    rev = str(n)[::-1]
    return str(n) == rev.translate(TABLE)


def find_strobogrammatic(n):
    for i in range(10**n, 10**(n+1)):
        if is_strobogrammatic(i):
            yield i


if __name__ == '__main__':
    for n in range(1, 5):
        print(list(find_strobogrammatic(n)))
