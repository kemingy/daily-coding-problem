# Given the head to a singly linked list, where each node also has a “random”
# pointer that points to anywhere in the linked list, deep clone the list.

class Node:
    def __init__(self, value, nxt=None, random=None):
        self.value = value
        self.next = nxt
        self.random = random


def display(node):
    while node and node.next:
        print(node.value, node.random.value)
        node = node.next
    print(node.value, node.random.value)


def deep_copy(node):
    if not node:
        return None

    head = Node(node.value)
    origin = node
    backup = head
    while origin.next:
        origin = origin.next
        backup.next = Node(origin.value)
        backup = backup.next

    origin = node
    backup = head
    while origin:
        backup.random = origin.random
        backup = backup.next
        origin = origin.next

    return head


if __name__ == '__main__':
    nodes = []
    for i in range(1, 6):
        nodes.append(Node(i))
        if i > 1:
            nodes[i - 2].next = nodes[i - 1]

    nodes[0].random = nodes[2]
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[4]
    nodes[3].random = nodes[2]
    nodes[4].random = nodes[1]

    display(nodes[0])
    print('-' * 50)

    backup = deep_copy(nodes[0])
    display(backup)
