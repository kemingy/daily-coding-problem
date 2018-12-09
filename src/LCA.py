# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree. Assume that each node in the tree also has a pointer to its parent.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes v and w as the lowest node in T that has both v 
# and w as descendants (where we allow a node to be a descendant of itself).”


class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def set_children(self, left=None, right=None):
        self.left = left
        self.right = right
        if left:
            left.parent = self
        if right:
            right.parent = self


def lowest_common_ancestor(x, y):
    parents_x, parents_y = set(), set()

    while not (parents_x & parents_y):
        if x:
            parents_x.add(x)
            x = x.parent
        if y:
            parents_y.add(y)
            y = y.parent

        if x is None and y is None:
            break

    return (parents_x & parents_y).pop().value


if __name__ == '__main__':
    nodes = [Node(i) for i in range(7)]
    tree = nodes[0]
    tree.set_children(nodes[1], nodes[5])
    nodes[1].set_children(nodes[2], nodes[3])
    nodes[3].set_children(nodes[4])
    nodes[5].set_children(None, nodes[6])

    print(lowest_common_ancestor(nodes[4], nodes[6]))
    print(lowest_common_ancestor(nodes[2], nodes[4]))
    print(lowest_common_ancestor(nodes[5], nodes[6]))
