# Given pre-order and in-order traversals of a binary tree, write a function 
# to reconstruct the tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def reconstruct(preorder, inorder):
    if inorder:
        mid = inorder.index(preorder.pop(0))
        root = Node(inorder[mid])
        root.left = reconstruct(preorder, inorder[:mid])
        root.right = reconstruct(preorder, inorder[mid+1:])
        return root


def display_tree(root, prefix=''):
    stack = [root]
    while stack:
        new_stack = []
        for node in stack:
            if node is '|':
                print(node, end=' ')
            else:
                print(node.val, end=' ')
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
                new_stack.append('|')
        print()
        stack = new_stack


if __name__ == '__main__':
    for preorder, inorder in [
        (['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']),
        ([1, 4, 2, 3], [2, 4, 1, 3])
    ]:
        tree = reconstruct(preorder, inorder)
        display_tree(tree)