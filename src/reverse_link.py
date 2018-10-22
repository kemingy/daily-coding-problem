# Given the head of a singly linked list, reverse it in-place.

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def reverse_list(node):
    pre, cur, nxt = None, node, node.next
    while nxt:
        cur.next = pre
        pre = cur
        cur = nxt
        nxt = nxt.next

    cur.next = pre
    return cur


def display(node):
    while node and node.next:
        print(node.value, end=' -> ')
        node = node.next

    if node:
        print(node.value)



if __name__ == '__main__':
    h = Node(0, Node(1, Node(2)))
    display(h)
    h = reverse_list(h)
    display(h)
