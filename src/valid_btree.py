# Determine whether a tree is a valid binary search tree.
# A binary search tree is a tree with two children, left and right, and satisfies 
# the constraint that the key in the left child must be less than or equal to the 
# root and the key in the right child must be greater than or equal to the root.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valid_binary_tree(node):
    if not node:
        return True

    if node.left and node.left.value > node.value:
        return False
    if node.right and node.right.value < node.value:
        return False

    return valid_binary_tree(node.left) and valid_binary_tree(node.right)


if __name__ == '__main__':
    for tree in [
        Node(4, Node(2), Node(5, Node(3, Node(1), Node(6)))),
        Node(1, Node(1), Node(1)),
        Node(3, Node(2, Node(1), Node(5)), Node(2))
    ]:
        print(valid_binary_tree(tree))