# Run-length encoding is a fast and simple method of encoding strings. 
# The basic idea is to represent repeated successive characters as a single 
# count and character. For example, the string "AAAABBBCCDAA" would be encoded 
# as "4A3B2C1D2A".

def run_length_encode(text):
    last_char = ''
    count = 0
    ans = ''
    for char in text:
        if last_char == char:
            count += 1
        else:
            if count > 0:
                ans += '{}{}'.format(count, last_char)
            count = 1

        last_char = char

    if count > 0:
        ans += '{}{}'.format(count, last_char)

    return ans


def run_length_decode(text):
    assert len(text) % 2 == 0

    i = 0
    ans = ''
    while i < len(text):
        count, char = text[i], text[i + 1]
        assert count.isdigit()
        ans += char * int(count)
        i += 2

    return ans


if __name__ == '__main__':
    for text in ['AAAABBBCCDAA', 'ACCCADDDS', '']:
        code = run_length_encode(text)
        print('Text: "{}"\t Encode: "{}"\t Decode: "{}"'.format(
            text, code, run_length_decode(code)
        ))
