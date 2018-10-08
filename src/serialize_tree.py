# Given the root to a binary tree, implement serialize(root), which serializes 
# the tree into a string, and deserialize(s), which deserializes the string back
# into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    ans = []
    level = [node]
    while level:
        children = []
        for n in level:
            if n:
                children.append(n.left)
                children.append(n.right)
            ans.append(n.val if n else None)

        level = children

    return ans


def deserialize(node, index=0):
    if not node[index:]:
        return None

    root = Node(node[index], deserialize(node, index*2+1), deserialize(node, index*2+2))
    return root


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
