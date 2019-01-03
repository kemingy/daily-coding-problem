# Given the head of a singly linked list, swap every two nodes and return its
# head.

# For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

    def display(self):
        node = self
        while node and node.next:
            print(node.value, end=' -> ')
            node = node.next
        if node:
            print(node.value)

def swap_near_two(node):
    if not node:
        return

    head = Node(None, node)
    pre, cur, nxt = head, node, node.next
    while nxt:
        cur.next = nxt.next
        nxt.next = cur
        pre.next = nxt
        pre = cur
        cur = cur.next
        nxt = cur.next if cur else None

    return head.next

if __name__ == '__main__':
    link = Node(1, Node(2, Node(3, Node(4))))
    link.display()
    link = swap_near_two(link)
    link.display()

    new_link = Node(5, link)
    new_link.display()
    new_link = swap_near_two(new_link)
    new_link.display()
