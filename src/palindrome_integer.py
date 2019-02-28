# Write a program that checks whether an integer is a palindrome. For example,
# 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert
# the integer into a string.


def is_palindrome(num):
    x, y = num, 0
    while x:
        y = y * 10 + x % 10
        x //= 10

    return num == y


if __name__ == "__main__":
    for n in [121, 888, 678]:
        print(f"Is {n} a palindrome?: {is_palindrome(n)}")
