# Given a string s and an integer k, break up the string into multiple texts 
# such that each text has a length of k or less. You must break it up so that 
# words don't break across lines. If there's no way to break the text up, then 
# return null.
# You can assume that there are no spaces at the ends of the string and that 
# there is exactly one space between each word.


def break_line(words, k):
    ans = [[]]
    for word in words:
        line = ans[-1]
        if len(word) > k:
            return None
        if sum(map(len, line)) + len(word) + len(line) <= k:
            line.append(word)
        else:
            ans.append([word])

    return ans


if __name__ == '__main__':
    for text, k in [
            ('the quick brown fox jumps over the lazy dog', 10),
            ('the quick brown fox jumps over the lazy dog', 15),
            ('she is beautiful.', 7),
        ]:
        broken = break_line(text.split(' '), k)
        if broken:
            for line in broken:
                print('"{}"'.format(' '.join(line)))
            print('|{}|'.format('-' * (k + 2)))
        else:
            print('"{}" cannot be break.'.format(text))
