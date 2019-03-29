# Given a string with repeated characters, rearrange the string so that no two 
# adjacent characters are the same. If this is not possible, return None.

# For example, given "aaabbc", you could return "ababac". Given "aaab", 
# return None.


def rearrange(text):
    text = list(text)
    n = len(text)
    for i in range(n - 1):
        if text[i] == text[i+1]:
            found = False
            for j in range(i+1, n):
                if text[j] != text[i]:
                    text[i+1], text[j] = text[j], text[i+1]
                    found= True
            if not found:
                return None
    return ''.join(text)


if __name__ == '__main__':
    for s in ['aaabbc', 'aaab', 'wewiiisd']:
        print(rearrange(s))