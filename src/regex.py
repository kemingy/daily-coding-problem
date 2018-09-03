# Implement regular expression matching with the following special characters:
# •	. (period) which matches any single character 
# •	* (asterisk) which matches zero or more of the preceding element 


def regex(pattern, text):
    history = {}
    p_len, t_len = len(pattern), len(text)

    def dp(i, j):
        if (i, j) not in history:
            if i == p_len:
                ans = j == t_len
            else:
                match = j < t_len and pattern[i] in ('.', text[j])
                if i + 1 < p_len and pattern[i + 1] is '*':
                    # match zero or match one
                    ans = dp(i + 2, j) or match and dp(i, j + 1)
                else:
                    ans = match and dp(i + 1, j + 1)

            history[i, j] = ans

        return history[i, j]

    return dp(0, 0)


if __name__ == '__main__':
    for p, t in [('ra.', 'ray'), ('ra.', 'raymond'),
            ('.*at', 'chat'), ('.*at', 'chats'),]:
        print('Pattern: {} - Text: {} - Match ? {}'.format(
            p, t, 'True' if regex(p, t) else 'False'
        ))
