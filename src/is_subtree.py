# Given two non-empty binary trees s and t, check whether tree t has exactly the
# same structure and node values with a subtree of s. A subtree of s is a tree
# consists of a node in s and all of this node's descendants. The tree s could
# also be considered as a subtree of itself.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def check_descendants(s, t):
    if s is None and t is None:
        return True
    elif s is None or t is None:
        return False

    if s.value != t.value:
        return False

    return check_descendants(s.left, t.left) or check_descendants(s.right, t.right)


def is_subtree(s, t):
    if not s:
        return False

    if s.value == t.value:
        return check_descendants(s, t)

    return is_subtree(s.left, t) or is_subtree(s.right, t)


if __name__ == '__main__':
    s = Node(0, Node(1, Node(2), Node(3, Node(4))), Node(5, None, Node(6)))
    for t in [
        Node(4),
        Node(3, Node(4)),
        Node(2),
        Node(5, Node(6)),
        Node(7),
    ]:
        print(is_subtree(s, t))
