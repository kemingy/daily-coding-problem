# Given a 32-bit integer, return the number with its bits reversed.

# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000,
# return 0000 1111 0000 1111 0000 1111 0000 1111.


def reverse_bits(n):
    return int(bits_32(n)[::-1], 2)


def bits_32(n):
    return "{:0>32b}".format(n)


if __name__ == "__main__":
    for n in [0, 233, 888888888]:
        print(bits_32(n), bits_32(reverse_bits(n)))
