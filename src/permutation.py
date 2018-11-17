# Given a number in the form of a list of digits, return all possible 
# permutations.


def generate_permutations(nums, res=None, pos=0):
    if res is None:
        res = []
    if len(nums) == pos:
        # `list` here means generate new list instead of use the same pointer
        res.append(list(nums))
        return

    for i in range(pos, len(nums)):
        nums[pos], nums[i] = nums[i], nums[pos]
        generate_permutations(nums, res, pos + 1)
        nums[pos], nums[i] = nums[i], nums[pos]

    return res


if __name__ == '__main__':
    for nums in [[], [0], [1, 2, 3]]:
        print(nums, end=' -> ')
        print(generate_permutations(nums))
