# Find the longest substring with k unique characters in a given string.

def longest_substring(text, k):
    if k == 0 or text is None or len(text) == 0:
        return 0

    if len(text) < k:
        return len(text)

    max_length, left = k, 0
    table = dict()

    for i in range(len(text)):
        if text[i] not in table:
            table[text[i]] = 0
        table[text[i]] += 1

        if len(table) > k:
            max_length = max(max_length, i - left)

            while len(table) > k:
                if table[text[left]] <= 1:
                    del table[text[left]]
                else:
                    table[text[left]] -= 1

                left += 1

    max_length = max(max_length, len(text) - left)
    return max_length


if __name__ == '__main__':
    print(longest_substring('abcadcacacaca', 3))
    print(longest_substring('abcadadadadadeef', 3))
