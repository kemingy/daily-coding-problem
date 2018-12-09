# Given a string and a set of delimiters, reverse the words in the string while 
# maintaining the relative order of the delimiters. For example, given 
# "hello/world:here", return "here/world:hello"

# Follow-up: Does your solution work for the following cases: 
# "hello/world:here/", "hello//world:here"

import re

def reverse_word(text):
    return re.sub(r'\w+', '{}', text).format(*re.findall(r'\w+', text)[::-1])


if __name__ == '__main__':
    for text in ['hello/world:here', 'hello/world:here/', 'hello//world:here']:
        print(text, end=': ')
        print(reverse_word(text))
