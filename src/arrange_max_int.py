# Given a list of numbers, create an algorithm that arranges them in order to 
# form the largest possible integer. For example, given [10, 7, 76, 415], you 
# should return 77641510.


def arrange(nums):
    return int(''.join(sorted([str(n) for n in nums], reverse=True)))


if __name__ == '__main__':
    for nums in [[10, 7, 76, 415]]:
        print(nums, arrange(nums))