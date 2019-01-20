# Gray code is a binary code where each successive value differ in only one
# bit, as well as when wrapping around. Gray code is common in hardware so
# that we don't see temporary spurious values during transitions.

# Given a number of bits n, generate a possible gray code for it.

# For example, for n = 2, one gray code would be [00, 01, 11, 10].


def gray_code(n):
    code = "{{:0>{}b}}".format(n)
    for i in range(n ** 2):
        yield format(code.format(i))


if __name__ == "__main__":
    for i in range(1, 5):
        print(list(gray_code(i)))
