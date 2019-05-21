# Two nodes in a binary tree can be called cousins if they are on the same
# level of the tree but have different parents. For example, in the following
# diagram 4 and 6 are cousins.

#     1
#    / \
#   2   3
#  / \   \
# 4   5   6

# Given a binary tree and a particular node, find all cousins of that node.


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


def find_cousins(tree, target):
    queue = [tree]
    while queue:
        children = []
        found = False
        for node in queue:
            if node is None:
                continue
            if node.left is target or node.right is target:
                found = True
                continue
            children.append(node.left)
            children.append(node.right)

        if found:
            return [child.value for child in children if child is not None]
        queue = children
    return []


if __name__ == "__main__":
    tree = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
    tree.display()
    print(find_cousins(tree, tree.right))
    print(find_cousins(tree, tree.left.left))
