# Given a number in Roman numeral format, convert it to decimal.
# The values of Roman numerals are as follows:
# {
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1
# }
# In addition, note that the Roman numeral system uses subtractive notation for
# numbers such as IV and XL.

# For the input XIV, for instance, you should return 14.


ROMAN = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def roman(nums):
    if not nums:
        return 0
    count = 0
    for i in range(len(nums) - 1):
        count += ROMAN[nums[i]] * (-1 if ROMAN[nums[i]] < ROMAN[nums[i+1]] else 1)

    count += ROMAN[nums[-1]]

    return count


if __name__ == "__main__":
    for n in ["XIV", "XVI", "MDC", "VIII"]:
        print(n, roman(n))
