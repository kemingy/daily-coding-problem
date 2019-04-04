# A tree is symmetric if its data and shape remain unchanged when it is
# reflected about the root node. The following tree is an example:
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
# Given a k-ary tree, determine whether it is symmetric.


class Node:
    def __init__(self, value, child=None):
        self.value = value
        if child is None:
            self.child = []
        else:
            self.child = child


def symmetric(node):
    if not node.child:
        return True

    def is_the_same(x, y):
        if x.value != y.value:
            return False
        elif len(x.child) != len(y.child):
            return False
        else:
            return all([is_the_same(x.child[i], y.child[i]) for i in range(len(x.child))])

    n = len(node.child)
    return all([is_the_same(node.child[i], node.child[n-1-i]) for i in range(n//2)])


if __name__ == '__main__':
    for root in [
        Node(4, [Node(3, [Node(9)]), Node(5), Node(3, [Node(9)])]),
        Node(2, [Node(1, [Node(2)]), Node(1, [Node(0)])]),
        Node(1)
    ]:
        print(symmetric(root))
