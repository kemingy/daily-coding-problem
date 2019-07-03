# Write a program to merge two binary trees. Each node in the new tree should
# hold a value equal to the sum of the values of the corresponding nodes of the
# input trees.

# If only one input tree has a node in a given position, the corresponding node
# in the new tree should match that input node.


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


def merge(x, y, root=None):
    if root is None:
        root = Node(0)
        return merge(x, y, root)
    if x is None and y is None:
        return None
    elif x is None:
        root.value = y.value
        root.left = merge(x, y.left, root.left)
        root.right = merge(x, y.right, root.right)
    elif y is None:
        root.value = x.value
        root.left = merge(x.left, y, root.left)
        root.right = merge(x.right, y, root.right)
    else:
        root.value = x.value + y.value
        root.left = merge(x.left, y.left, root.left)
        root.right = merge(x.right, y.right, root.right)
    return root


if __name__ == '__main__':
    x = Node(2, Node(4, Node(5)), Node(9, None, Node(4, Node(1))))
    y = Node(1, Node(2, Node(3), Node(5)), Node(2))
    x.display()
    print('-' * 40)
    y.display()
    print('-' * 40)
    z = merge(x, y)
    z.display()
