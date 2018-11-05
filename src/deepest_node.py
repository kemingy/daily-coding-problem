# Given the root of a binary tree, return a deepest node.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def get_deepest_node(node):
    if not node:
        return None

    value = node.value
    parent = [node]
    while parent:
        children = []
        for p in parent:
            if p.left:
                children.append(p.left)
            if p.right:
                children.append(p.right)
            value = p.value

        parent = children

    return value


if __name__ == '__main__':
    tree = Node('a', Node('b', Node('d')), Node('c'))
    print(get_deepest_node(tree))