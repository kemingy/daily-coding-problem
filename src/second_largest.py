# Given the root to a binary search tree, find the second largest node 
# in the tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        def helper(root, value):
            if value > root.value:
                if root.right:
                    helper(root.right, value)
                else:
                    root.right = Node(value)
            elif value < root.value:
                if root.left:
                    helper(root.left, value)
                else:
                    root.left = Node(value)
            else:
                print('value already in this tree.')

        helper(self.root, value)

    def find_second_largest(self):
        node = last = self.root
        
        while node.right:
            last = node
            node = node.right

        ans = node.left or last
        return ans.value

if __name__ == '__main__':
    for values in [[3, 4, 1, 2], [5, 6, 3, 2, 1, 4], [4, 2, 1, 3, 6, 5]]:
        bt = BinaryTree()
        for v in values:
            bt.add_node(v)

        print('"{}" second largest node is {}'.format(values, bt.find_second_largest()))
