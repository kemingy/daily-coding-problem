# Given an even number (greater than 2), return two prime numbers whose sum will 
# be equal to the given number.

# A solution will always exist. See Goldbach’s conjecture.

# Example:
# Input: 4
# Output: 2 + 2 = 4

# If there are more than one solution possible, return the lexicographically 
# smaller solution.

from random import randrange

def miller_rabin(n, k=20):
    """
    StackOverflow: https://stackoverflow.com/questions/14613304/rabin-miller-strong-pseudoprime-test-implementation-wont-work
    """
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert n >= 2

    for p in small_primes:
        if n < p * p:
            return True
        if n % p == 0:
            return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True



def smallest_goldbach(n):
    for i in range(2, n // 2 + 1):
        if miller_rabin(i) and miller_rabin(n - i):
            return (i, n - i)

    return None


if __name__ == '__main__':
    for n in [4, 8, 22, 100, 998, 888888888888888]:
        print(n, smallest_goldbach(n))
