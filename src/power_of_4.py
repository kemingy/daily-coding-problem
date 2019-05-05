# Given a 32-bit positive integer N, determine whether it is a power of four
# in faster than O(log N) time.


def power_of_4(n: int) -> bool:
    return n > 3 and n & (n-1) == 0 and n & 0xaaaaaaaa == 0


if __name__ == "__main__":
    for n in [2, 4, 6, 8, 16, 32, 64, 200, 100]:
        print(n, 'is power of 4:', power_of_4(n))
