# Given a word W and a string S, find all starting indices in S which are 
# anagrams of W.

# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


def anagram_substring(w, s):
    indices = []
    for pattern in (w, w[::-1]):
        i = s.find(pattern)
        while i >= 0:
            indices.append(i)
            i = s.find(pattern, i + 1)

    return indices


if __name__ == '__main__':
    print(anagram_substring('ab', 'abxaba'))