# Given a string and a set of characters, return the shortest substring 
# containing all the characters in the set.
# For example, given the string "figehaeci" and the set of characters {a, e, i}, 
# you should return "aeci".


def shortest_substring(text, chars):
    start, end = 0, 0
    contain = dict()
    ans = text

    start, end = 0, 1
    for i, t in enumerate(text):
        if t in chars:
            contain[t] = contain.get(t, 0) + 1

        end = i + 1
        while len(contain) == len(chars) and start < end:
            if end - start < len(ans):
                ans = text[start:end]

            if text[start] in chars:
                contain[text[start]] -= 1
                if contain[text[start]] == 0:
                    del contain[text[start]]

            start += 1

    return ans


if __name__ == '__main__':
    for text, chars in [
        ('figehaeci', {'a', 'e', 'i'}),
        ('abcdeeefffaaaacd', {'a', 'c', 'e'})
    ]:
        print(shortest_substring(text, chars))
