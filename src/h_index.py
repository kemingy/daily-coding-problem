# In academia, the h-index is a metric used to calculate the impact of a
# researcher's papers. It is calculated as follows:

# A researcher has index h if at least h of her N papers have h citations each.
# If there are multiple h satisfying this formula, the maximum is chosen.

# For example, suppose N = 5, and the respective citations of each paper are
# [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3
# papers with at least 3 citations.

# Given a list of paper citations of a researcher, calculate their h-index.


from random import randint


def h_index(nums):
    length = len(nums)
    count = [0] * (length+1)
    for n in nums:
        count[min(length, n)] += 1

    h = 0
    for i in range(length, -1, -1):
        h += count[i]
        if h >= i:
            return i
    return 0


if __name__ == '__main__':
    for _ in range(5):
        nums = [randint(0, 15) for _ in range(randint(3, 10))]
        print(h_index(nums), nums)
