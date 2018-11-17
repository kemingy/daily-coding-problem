# Given an unsorted array of integers, find the length of the longest consecutive 
# elements sequence.
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element 
# sequence is [1, 2, 3, 4]. Return its length: 4.


def longest_consecutive_sequence(nums):
    ans = 0
    n = set(nums)

    for num in nums:
        if (num - 1) not in n:
            seq = num
            while (seq + 1) in n:
                seq += 1

            ans = max(ans, seq - num + 1)

    return ans


if __name__ == '__main__':
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))