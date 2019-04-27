# Recall that a full binary tree is one in which each node is either a leaf
# node, or has two children. Given a binary tree, convert it to a full one by
# removing nodes with only one child.

# For example, given the following tree:
#          0
#       /     \
#     1         2
#   /            \
# 3                 4
#   \             /   \
#     5          6     7
# You should convert it to:
#      0
#   /     \
# 5         4
#         /   \
#        6     7


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


def to_full_b_tree(node):
    if node.left and node.right:
        to_full_b_tree(node.left)
        to_full_b_tree(node.right)
        return node

    if node.left is None and node.right is None:
        return node

    if node.left:
        node.value = node.left.value
        node.right = node.left.right
        node.left = node.left.left
        return to_full_b_tree(node)

    node.value = node.right.value
    node.left = node.right.left
    node.right = node.right.right
    return to_full_b_tree(node)


if __name__ == '__main__':
    tree = Node(0,
                Node(1, Node(3, None, Node(5))),
                Node(2, None, Node(4, Node(6), Node(7)))
                )
    tree.display()
    to_full_b_tree(tree)
    print('-' * 80)
    tree.display()

