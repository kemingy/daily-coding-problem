# Given an integer N, construct all possible binary search trees with N nodes.


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

    def copy(self):
        node = Node(self.value)
        node.left = self.left.copy() if self.left else None
        node.right = self.right.copy() if self.right else None
        return node


def build_binary_search_tree(n):
    if n <= 0:
        return [None]
    elif n == 1:
        return [Node(n)]
    else:
        return [Node(n, left, right)
                for k in range(n)
                for left in build_binary_search_tree(k)
                for right in build_binary_search_tree(n-k-1)]


if __name__ == "__main__":
    for i in range(1, 5):
        trees = build_binary_search_tree(i)
        print('='*80)
        for tree in trees:
            tree.display()
            print('-'*80)
