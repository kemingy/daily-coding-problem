# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the 
# number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 
# 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not 
# allowed.

ALPHABET = [chr(i) for i in range(97, 123)]

def decode_number(nums):
    codes = []

    def helper(nums, message):
        if not nums:
            codes.append(message)

        for i in range(1, len(nums) + 1):
            code = int(nums[:i])
            if code == 0 or code > 26:
                break

            helper(nums[i:], message + [ALPHABET[code - 1]])

    helper(nums, [])
    return codes


if __name__ == '__main__':
    print(decode_number('111'))
