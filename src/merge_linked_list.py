# Given k sorted singly linked lists, write a function to merge all the lists
# into one sorted singly linked list


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def merge(nodes):
    head = node = min_node(nodes)
    while any(nodes):
        node.next = min_node(nodes)
        node = node.next

    return head


def min_node(nodes):
    if not nodes:
        return None

    ans = nodes[0]
    ans_index = 0
    for i, n in enumerate(nodes):
        if not n:
            continue
        if ans is None or n.value < ans.value:
            ans = n
            ans_index = i

    if ans:
        nodes[ans_index] = nodes[ans_index].next
    return ans


def display(node):
    while node and node.next:
        print(node.value, end=' -> ')
        node = node.next

    print(node.value)


if __name__ == '__main__':
    lists = [
        Node(0, Node(4)),
        Node(1, Node(5, Node(6))),
        Node(1, Node(2, Node(3)))
    ]

    for node in lists:
        display(node)

    node = merge(lists)
    display(node)