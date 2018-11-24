# Determine whether a doubly linked list is a palindrome. What if it’s singly 
# linked?

# For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def is_palindrome(node):
    values = []
    while node:
        values.append(node.value)
        node = node.next

    string = ''.join([str(v) for v in values])
    return string == string[::-1]



if __name__ == '__main__':
    for link in [
        Node(1, Node(4, Node(3, Node(4, Node(1))))),
        Node(1, Node(4)),
    ]:
        print(is_palindrome(link))