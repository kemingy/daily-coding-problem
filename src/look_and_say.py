# The "look and say" sequence is defined as follows: beginning with the term 1,
# each subsequent term visually describes the digits appearing in the previous
# term. The first few terms are as follows:

# 1
# 11
# 21
# 1211
# 111221

# As an example, the fourth term is 1211, since the third term consists of one
# 2 and one 1.

# Given an integer N, print the Nth term of this sequence.


def look_and_say(n):
    term = '1'
    for _ in range(n):
        term = describe(term)

    return term


def describe(term):
    last = term[0]
    count = 1
    ans = ''
    for i in range(1, len(term)):
        if term[i] == last:
            count += 1
        else:
            ans += '{}{}'.format(count, last)
            count = 1
            last = term[i]

    return ans + '{}{}'.format(count, last)


if __name__ == "__main__":
    for i in range(10):
        print(i, '->', look_and_say(i))
