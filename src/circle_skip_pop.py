# There are N prisoners standing in a circle, waiting to be executed.

# The executions are carried out starting with the kth person, and removing
# every successive kth person going clockwise until there is no one left.

# Given N and k, write an algorithm to determine where a prisoner should stand
# in order to be the last survivor.

# For example, if N = 5 and k = 2, the order of executions would be
# [2, 4, 1, 5, 3], so you should return 3.

# Bonus: Find an O(log N) solution if k = 2.


def last_one(n, k, offset=0):
    j = 0
    for i in range(2, n+1):
        j = (j + k) % i
    return (j + offset) % n + 1


if __name__ == '__main__':
    for (n, k) in [(2, 1), (5, 2), (100, 7)]:
        print(last_one(n, k))
