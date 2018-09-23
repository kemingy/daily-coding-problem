# Given a string, find the longest palindromic contiguous substring. If there 
# are more than one with the maximum length, return any one.


def longest_palindromic_substring(word):
    if word == word[::-1]:
        return word

    length = 1
    start = 0
    for i in range(len(word)):
        left, right = i - length, i + 1

        if left >= 1:
            tmp = word[left-1:right]
            if tmp == tmp[::-1]:
                length += 2
                start = left - 1

        if left >= 0:
            tmp = word[left:right]
            if tmp == tmp[::-1]:
                length += 1
                start = left

    return word[start:start+length]


if __name__ == '__main__':
    for word in ['aabcdcb', 'bananas', 'google', 'a', 'abbacccad']:
        print('Logest palindromic substring of {:10} is {}'.format(
            word, longest_palindromic_substring(word)
        ))
