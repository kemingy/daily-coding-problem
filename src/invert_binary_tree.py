# invert a binary tree

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def display(node):
    if not node:
        return None

    print(node.value)
    display(node.left)
    display(node.right)


def invert(node):
    if not node:
        return None

    node.left, node.right = node.right, node.left
    invert(node.left)
    invert(node.right)


if __name__ == '__main__':
    tree = Node(0, Node(1, Node(2)), Node(3, Node(4), Node(5)))
    display(tree)
    print('after invert')
    invert(tree)
    display(tree)