# Print the nodes in a binary tree level-wise. For example, the following should 
# print 1, 2, 3, 4, 5.

#   1
#  / \
# 2   3
#    / \
#   4   5

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_traverse(node):
    if node is None:
        return None

    candidates = [node]
    children = []

    while candidates:
        for cand in candidates:
            yield cand.value
            if cand.left:
                children.append(cand.left)
            if cand.right:
                children.append(cand.right)

        candidates = children
        children = []


if __name__ == '__main__':
    tree = Node(1, Node(2), Node(3, Node(4), Node(5)))
    print(list(level_traverse(tree)))