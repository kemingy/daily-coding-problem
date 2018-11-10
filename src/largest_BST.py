# Given a tree, find the largest tree/subtree that is a BST.
# Given a tree, return the size of the largest tree/subtree that is a BST.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def largest_BST(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    if (node.left and node.left.value >= node.value) or (node.right and node.right.value <= node.value):
        print(node.value, 'not valid')
        return max(largest_BST(node.left), largest_BST(node.right))

    return 1 + max(largest_BST(node.left), largest_BST(node.right))



if __name__ == '__main__':
    tree = Node(5, Node(2, Node(1), Node(4, Node(3))), Node(0, Node(2), Node(10)))
    print(largest_BST(tree))