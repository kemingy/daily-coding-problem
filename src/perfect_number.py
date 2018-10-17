# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.


class PerfectNumber:
    def __init__(self):
        self.perfect = []

    def get_kth(self, k):
        n = self.perfect[-1] + 1 if self.perfect else 0
        while len(self.perfect) < k:
            if self.is_perfect(n):
                self.perfect.append(n)
            n += 1

        return self.perfect[k - 1]

    def is_perfect(self, n):
        return 10 == sum([int(x) for x in str(n)])



if __name__ == '__main__':
    pn = PerfectNumber()
    for k in [6, 2, 1, 5, 10]:
        print(pn.get_kth(k))

    print(pn.perfect)
