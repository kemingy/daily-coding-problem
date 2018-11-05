# Given a mapping of digits to letters (as in a phone number), and a digit 
# string, return all possible letters the number could represent. You can assume
# each valid number in the mapping is a single digit.


def digits2letters(mapping, nums):
    if '0' in nums or '1' in nums:
        print('There is no mapping letters for "0" or "1".')
        return None

    if not nums:
        return []

    ans = mapping[nums[0]]
    for n in nums[1:]:
        ans = [''.join([old, new]) for old in ans for new in mapping[n]]

    return ans


if __name__ == '__main__':
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['u', 'v', 'w'],
        '9': ['x', 'y', 'z']
    }
    print(digits2letters(mapping, '98765'))
    print(digits2letters(mapping, '233'))
    print(digits2letters(mapping, '110'))
