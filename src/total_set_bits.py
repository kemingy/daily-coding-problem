# Write an algorithm that finds the total number of set bits in all integers
# between 1 and N.


def get_bit(n):
    ans = 0
    while n > 0:
        ans += n & 1
        n >>= 1
    return ans


def set_bits(n):
    return sum(get_bit(i) for i in range(1, n+1))


if __name__ == '__main__':
    for n in [2, 4, 10, 7, 20]:
        print(n, set_bits(n))
