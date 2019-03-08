# A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
# •	if n is even, the next number in the sequence is n / 2
# •	if n is odd, the next number in the sequence is 3n + 1
# It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
# Bonus: What input n <= 1000000 gives the longest sequence?


def collatz(n):
    seq = [n]

    def find_next(n):
        return n // 2 if n & 1 == 0 else 3 * n + 1

    while n != 1:
        n = find_next(n)
        seq.append(n)

    return seq


if __name__ == "__main__":
    longest = []
    for i in range(2, 1000000):
        seq = collatz(i)
        if len(seq) > len(longest):
            longest = seq

    print(longest)
    # >>> 837799: 525
