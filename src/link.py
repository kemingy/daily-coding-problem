# Given a singly linked list and an integer k, remove the kth last element from 
# the list. k is guaranteed to be smaller than the length of the list.
# The list is very long, so making more than one pass is prohibitively expensive.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkList:
    def __init__(self, values):
        self.length = 0
        self.head = None

        if values:
            current = self.head = Node(values[0])
            self.length += 1
            for v in values[1:]:
                node = Node(v)
                current.next = node
                current = current.next
                self.length += 1

    def last_k(self, k):
        assert k < self.length

        current = self.head
        k = self.length - k
        while k > 0:
            k -= 1
            current = current.next

        return current.value

    def last_k_without_length(self, k):
        current = delay = self.head

        while k > 0:
            k -= 1
            current = current.next

        while current:
            current = current.next
            delay = delay.next

        return delay.value


if __name__ == '__main__':
    link = LinkList(list(range(20)))
    print('Last k-th element: {}'.format(link.last_k(3)))
    print('Last k-th element without knowing length of list: {}'.format(
        link.last_k_without_length(3)))
