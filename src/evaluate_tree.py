# Suppose an arithmetic expression is given as a binary tree. Each leaf is an 
# integer and each internal node is one of '+', '−', '∗', or '/'.
# Given the root to such a tree, write a function to evaluate it.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class BinaryTree:
    def __init__(self, values):
        if not values:
            self.root = None
            return

        self.root = Node(values.pop(0))
        parents, children = [self.root], []
        while parents:
            for p in parents:
                for i in range(2):
                    try:
                        val = values.pop(0)
                    except IndexError:
                        break

                    child = Node(val)
                    children.append(child)
                    if i ^ 1:
                        p.left = child
                    else:
                        p.right = child

            parents = children
            children = []

    def display(self):
        def print_node(node):
            if not node:
                print('null')
            else:
                print(node.val)
                print_node(node.left)
                print_node(node.right)

        print_node(self.root)


def evaluate(node):
    if isinstance(node.val, int):
        return node.val

    if node.left and node.right:
        if node.val == '+':
            return evaluate(node.left) + evaluate(node.right)
        elif node.val == '-':
            return evaluate(node.left) - evaluate(node.right)
        elif node.val == '*':
            return evaluate(node.left) * evaluate(node.right)
        elif node.val == '/':
            return evaluate(node.left) // evaluate(node.right)

    raise ValueError('Wrong value of node: {}'.format(node))


if __name__ == '__main__':
    for values in [['*', '+', '+', 3, 2, 4, 5], ['/', '*', '+', 2, 6, 1, 2]]:
        tree = BinaryTree(values)
        # tree.display()
        print(evaluate(tree.root))
