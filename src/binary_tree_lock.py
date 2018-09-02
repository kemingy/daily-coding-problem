# Implement locking in a binary tree. A binary tree node can be locked or 
# unlocked only if all of its descendants or ancestors are not locked.

# Design a binary tree node class with the following methods:
# •	is_locked, which returns whether the node is locked 
# •	lock, which attempts to lock the node. If it cannot be locked, then it 
#     should return false. Otherwise, it should lock it and return true. 
# •	unlock, which unlocks the node. If it cannot be unlocked, then it should 
#     return false. Otherwise, it should unlock it and return true. 

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = self.parent = None
        self._is_locked = False
        self.children_lock_count = 0

    @property
    def is_locked(self):
        return self._is_locked

    def lock(self):
        if not self.is_free():
            return False

        self._is_locked = True
        node = self.parent
        while node:
            node.children_lock_count += 1
            node = node.parent

        return True

    def unlock(self):
        if not self.is_free():
            return False

        self._is_locked = False
        node = self.parent
        while node:
            node.children_lock_count -= 1
            node = node.parent

        return True

    def is_free(self):
        if self.children_lock_count > 0:
            return False

        node = self.parent
        while node:
            if node.is_locked:
                return False
            node = node.parent

        return True

    def __repr__(self):
        return 'value: {}'.format(self.value)


class BinaryTree:
    def __init__(self, values):
        self.root = None
        if not values:
            return

        self.root = BinaryTreeNode(values.pop(0))
        parents, children = [self.root], []
        while parents:
            for node in parents:
                # print(node)
                for i in range(2):
                    try:
                        value = values.pop(0)
                    except IndexError:
                        break

                    if value:
                        child = BinaryTreeNode(value)
                        child.parent = node
                        children.append(child)
                        if i ^ 1:
                            node.left = child
                        else:
                            node.right = child

            parents = children
            children = []

    def display(self):
        def print_node(node):
            if not node:
                print('null')
            else:
                print(node.value)
                print_node(node.left)
                print_node(node.right)

        print_node(self.root)


if __name__ == '__main__':
    tree = BinaryTree([0, 1, 2, 3, None, 4, 5, 6])
    # tree.display()

    print('is locked: {}'.format(tree.root.right.left.is_locked))
    print('lock: {}'.format(tree.root.right.left.lock()))
    print('is locked: {}'.format(tree.root.right.left.is_locked))
    print('lock count: {}'.format(tree.root.children_lock_count))
    print('lock: {}'.format(tree.root.right.lock()))
    print('unlock: {}'.format(tree.root.right.left.unlock()))
    print('lock: {}'.format(tree.root.right.lock()))