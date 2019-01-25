# Given a list of words, find all pairs of unique indices such that the
# concatenation of the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return
# [(0, 1), (1, 0), (2, 3)].


def palindrome_pair(pairs):
    result = []
    for i, x in enumerate(pairs):
        for j, y in enumerate(pairs):
            if i == j:
                continue
            if is_palindrome(x + y):
                result.append((i, j))

    return result


def is_palindrome(text):
    return text == text[::-1]


if __name__ == "__main__":
    for pairs in [
        ["code", "edoc", "da", "d"],
        ["geekf", "geeks", "or", "keeg", "abc", "bc"],
        ["abc", "xyxcba", "geekst", "or", "keeg", "bc"],
    ]:
        print(pairs)
        print(palindrome_pair(pairs))
