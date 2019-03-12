# Given an integer n, return the length of the longest consecutive run of 1s in
# its binary representation.

# For example, given 156, you should return 3.


def longest_binary_consecutive(n):
    count = 0
    longest = 0
    while n > 0:
        if n & 1:
            count += 1
        else:
            longest = max(longest, count)
            count = 0
        n >>= 1

    return max(longest, count)


if __name__ == "__main__":
    for n in [156, 233, 1, 0, 0xFFFF00EF]:
        print(n, longest_binary_consecutive(n))
