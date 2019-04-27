# In Ancient Greece, it was common to write text with the first line going left
# to right, the second line going right to left, and continuing to go back and
# forth. This style was called "boustrophedon".

# Given a binary tree, write an algorithm to print the nodes in boustrophedon
# order.

# For example, given the following tree:
#        1
#     /     \
#   2         3
#  / \       / \
# 4   5     6   7
# You should return [1, 3, 2, 4, 5, 6, 7].


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def boustrophedon(node):
    queue = [node]
    reverse = True
    while queue:
        next_layer = []
        for n in queue:
            if n is None:
                continue
            yield n.value
            if reverse:
                next_layer.append(n.left)
                next_layer.append(n.right)
            else:
                next_layer.append(n.right)
                next_layer.append(n.left)

        queue = next_layer[::-1]
        reverse = True if not reverse else False


if __name__ == '__main__':
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    print(list(boustrophedon(tree)))
