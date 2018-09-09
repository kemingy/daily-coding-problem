# The edit distance between two strings refers to the minimum number of character 
# insertions, deletions, and substitutions required to change one string to the 
# other. For example, the edit distance between “kitten” and “sitting” is three: 
# substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.


def edit_distance(s1, s2):
    # Wagner–Fischer algorithm
    len1, len2 = len(s1), len(s2)
    dp = [[-1 for j in range(len2 + 1)] for i in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i

    for j in range(len2 + 1):
        dp[0][j] = j

    for j in range(1, len2 + 1):
        for i in range(1, len1 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[-1][-1]


if __name__ == '__main__':
    for s1, s2 in [('kitten', 'sitting'), 
                   ('horse', 'ros'), 
                   ('intention', 'execution')]:
        print('Edit distance between "{}" and "{}" is {}.'.format(
                                                s1, s2, edit_distance(s1, s2)))
