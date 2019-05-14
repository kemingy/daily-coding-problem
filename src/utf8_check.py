# UTF-8 is a character encoding that maps each symbol to one, two, three,
# or four bytes.

# For example, the Euro sign, €, corresponds to the three bytes
# 11100010 10000010 10101100. The rules for mapping characters are as follows:

# •	For a single-byte character, the first bit must be zero.
# •	For an n-byte character, the first byte starts with n ones and a zero.
#   The other n - 1 bytes all start with 10.

# Visually, this can be represented as follows.

#  Bytes   |           Byte format
# -----------------------------------------------
#    1     | 0xxxxxxx
#    2     | 110xxxxx 10xxxxxx
#    3     | 1110xxxx 10xxxxxx 10xxxxxx
#    4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

# Write a program that takes in an array of integers representing byte values,
# and returns whether it is a valid UTF-8 encoding.


def utf8_check(nums):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] < 128:
            i += 1
            continue
        elif nums[i] < 192:
            if not (i + 1 < n and nums[i+1] < 192):
                return False
            i += 2
            continue
        elif nums[i] < 224:
            if not (i + 2 < n and all([nums[j] < 192 for j in range(i+1, i+3)])):
                return False
            i += 3
            continue
        elif nums[i] < 240:
            if not (i + 3 < n and all([nums[j] < 192 for j in range(i+1, i+4)])):
                return False
            i += 4
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    for nums in [[226, 130, 172, 48], [129, 12, 56, 220]]:
        print(utf8_check(nums), nums)
