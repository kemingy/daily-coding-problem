# A unival tree (which stands for "universal value") is a tree where all nodes 
# under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_tree(node):
    is_unival_node = {}

    def is_unival(node):
        if node is None:
            return False

        if node in is_unival_node:
            return is_unival_node[node]

        if node.left == node.right == None:
            is_unival_node[node] = True
            return True
        elif node.left and node.right and node.left.val == node.right.val:
            return is_unival(node.left) and is_unival(node.right)
        else:
            is_unival_node[node] = False
            return False

    count = 0
    level = [node]
    while level:
        children = []
        for n in level:
            if is_unival(n):
                count += 1
            if n is not None:
                children.append(n.left)
                children.append(n.right)

        level = children

    return count


if __name__ == '__main__':
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_unival_tree(node))
