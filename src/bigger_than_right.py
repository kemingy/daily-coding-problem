# Given an array of integers, return a new array where each element in the new
# array is the number of smaller elements to the right of that element in the
# original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

# •	There is 1 smaller element to the right of 3
# •	There is 1 smaller element to the right of 4
# •	There are 2 smaller elements to the right of 9
# •	There is 1 smaller element to the right of 6
# •	There are no smaller elements to the right of 1


class Node:
    def __init__(self, value, left=None, right=None, count=0):
        self.value = value
        self.left = left
        self.right = right
        self.count = count


def build_tree(node, n, count=0):
    if node.value < n:
        count = max(count, node.count)
        if node.right:
            return build_tree(node.right, n, count + 1)
        node.right = Node(n, count=count + 1)
        return count + 1
    elif node.value > n:
        node.count += 1
        if node.left:
            return build_tree(node.left, n, count)
        node.left = Node(n, count=count)
        return count
    else:
        return node.count


def count_smaller(nums):
    root = Node(nums[-1])
    count = [0]
    for n in nums[-2::-1]:
        count.append(build_tree(root, n))

    return count[::-1]


if __name__ == "__main__":
    for nums in [
        [3, 4, 9, 6, 1],
        [12, 1, 2, 3, 0, 11, 4],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ]:
        print(nums, end=" -> ")
        print(count_smaller(nums))
