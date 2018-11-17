# Given a binary tree of integers, find the maximum path sum between two nodes. 
# The path must go through at least one node, and does not need to go through 
# the root.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_path_sum(node, is_root=False):
    if node is None:
        return 0

    paths = [
        node.value,
        node.value + max_path_sum(node.left),
        node.value + max_path_sum(node.right),
    ]

    if is_root:
        paths.append(node.value + max_path_sum(node.left) + max_path_sum(node.right))
    return max(paths)


if __name__ == '__main__':
    for tree in [
        Node(1, Node(2), Node(3)),
        Node(10, Node(2, Node(20), Node(1)), Node(10, right=Node(-5, Node(3), Node(4)))),
        Node(2, Node(-5, Node(3), Node(3)), Node(6, Node(-2), Node(3))),
        Node(2, Node(-5, Node(8), Node(3)), Node(6, Node(-2), Node(3))),
    ]:
        print(max_path_sum(tree, True))