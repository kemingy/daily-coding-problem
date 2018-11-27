# Given a binary tree, return all paths from the root to leaves.
# For example, given the tree

#    1
#   / \
#  2   3
#     / \
#    4   5

# it should return [[1, 2], [1, 3, 4], [1, 3, 5]].

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def travel_path(node):
    paths = []

    def travel(node, path):
        path.append(node.value)
        if node.left is None and node.right is None:
            paths.append(path)
            return None

        if node.left:
            travel(node.left, path.copy())
        if node.right:
            travel(node.right, path.copy())

    travel(node, [])

    return paths


if __name__ == '__main__':
    tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    print(travel_path(tree))