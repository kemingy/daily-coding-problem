# Given a binary search tree and a range [a, b] (inclusive), return the sum of
# the elements of the binary search tree within the range.

# For example, given the following tree:

#     5
#    / \
#   3   8
#  / \ / \
# 2  4 6  10

# and the range [4, 9], return 23 (5 + 4 + 6 + 8).


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self, space=0):
        if self.right:
            self.right.display(space=space+4)
        print('{}{}'.format(' ' * space, self.value))
        if self.left:
            self.left.display(space=space+4)


def sum_tree(node, left, right):
    if node is None:
        return 0
    if left <= node.value <= right:
        return node.value + \
            sum_tree(node.left, left, right) + \
            sum_tree(node.right, left, right)
    elif node.value < left:
        return sum_tree(node.right, left, right)
    else:
        return sum_tree(node.left, left, right)


if __name__ == '__main__':
    tree = Node(5, Node(3, Node(2), Node(4)), Node(8, Node(6), Node(10)))
    print(sum_tree(tree, 4, 9))
