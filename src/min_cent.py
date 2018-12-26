# Find the minimum number of coins required to make n cents.
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢,
# and a 1¢.


CENTS = [1, 5, 10, 25]


def min_cent(n):
    index = len(CENTS) - 1
    coins = []
    while n > 0:
        cent = CENTS[index]
        if n >= cent:
            coins.append(cent)
            n -= cent
        else:
            index -= 1
            if index < 0:
                break

    return coins


if __name__ == "__main__":
    for n in [16, 3, 48, 81, 99]:
        print(n, min_cent(n))
