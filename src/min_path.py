# Given a binary tree, find a minimum path sum from root to a leaf.
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_path(node):
    path_values = []

    def search_path(node, path=0):
        path += node.value
        if node.left is None and node.right is None:
            path_values.append(path)
            return

        if node.left:
            search_path(node.left, path)
        if node.right:
            search_path(node.right, path)

    search_path(node)
    return min(path_values)


if __name__ == "__main__":
    tree = Node(10, Node(5, right=Node(2)), Node(5, right=Node(1, Node(-1))))
    print(min_path(tree))
