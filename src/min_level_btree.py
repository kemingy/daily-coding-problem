# Given a binary tree, return the level of the tree with minimum sum.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_level_sum(node):
    min_sum = float('inf')
    cur_levle = [node]

    while cur_levle:
        next_level = []
        total = 0
        for n in cur_levle:
            total += n.value
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)

        if total < min_sum:
            min_sum = total
        cur_levle = next_level

    return min_sum


if __name__ == '__main__':
    tree = Node(23, Node(20, Node(12), Node(8)), Node(5, Node(1)))
    print(min_level_sum(tree))