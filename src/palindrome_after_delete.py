# Given a string which we can delete at most k, return whether you can make a
# palindrome.

# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to
# get 'waterretaw'.


def is_palindrome_without_k_char(word, k):
    reverse = word[::-1]
    n = len(word)

    return is_k_palindrome(word, reverse, n, n) <= 2 * k

def is_k_palindrome(x, y, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] if x[i - 1] == y[j - 1] else 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    print(is_palindrome_without_k_char('waterrfetawx', 2))
