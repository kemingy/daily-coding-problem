# Generate a finite, but an arbitrarily large binary tree quickly in O(1).
# That is, generate() should return a tree whose size is unbounded but finite.

from random import random

class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self._left = left
        self._right = right

        self.evaluate_left = False
        self.evaluate_right = False

    @property
    def left(self):
        if not self.evaluate_left:
            if random() < 0.5:
                self._left = Node()
            self.evaluate_left = True

        return self._left

    @property
    def right(self):
        if not self.evaluate_right:
            if random() < 0.5:
                self._right = Node()
            self.evaluate_right = True

        return self._right

    def count(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.count()
        elif self.right is None:
            return 1 + self.left.count()
        return 1 + self.left.count() + self.right.count()


def generate():
    return Node()


if __name__ == '__main__':
    node = generate()
    print(node.count())