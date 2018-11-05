# Using a read7() method that returns 7 characters from a file, implement 
# readN(n) which reads n characters.


def read7(sentence):
    return sentence[:7]


def readN(sentence, n):
    start = 0
    ans = ''
    while n > 0:
        if n >= 7:
            ans += read7(sentence[start:])
        else:
            ans += read7(sentence[start:start+n])

        n -= 7
        start += 7

    return ans


if __name__ == '__main__':
    sentence = 'Hello world'
    print(readN(sentence, 10))
    print(read7(sentence))
