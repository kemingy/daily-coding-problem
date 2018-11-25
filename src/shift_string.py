# Given two strings A and B, return whether or not A can be shifted some number 
# of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is 
# acb, return false.


def can_shift_to(x, y):
    return y in x * 2


if __name__ == '__main__':
    for x, y in [('abcde', 'cdeab'), ('abc', 'acb')]:
        print(x, y, can_shift_to(x, y))