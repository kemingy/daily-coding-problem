# Given integers M and N, write a program that counts how many positive integer
# pairs (a, b) satisfy the following conditions:

# •	a + b = M
# •	a XOR b = N


def add_xor_pair(m, n):
    ans = []
    for i in range(1, m):
        if i ^ (m - i) == n:
            ans.append((i, m - i))
    return ans


if __name__ == '__main__':
    for m, n in [(5, 4), (100, 92), (100, 90)]:
        print(add_xor_pair(m, n))
