# Given two singly linked lists that intersect at some point, find the 
# intersecting node. The lists are non-cyclical.

class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, values):
        if not values:
            self.head = None

        self.head = LinkNode(values[0])
        current = self.head

        for v in values[1:]:
            current.next = LinkNode(v)
            current = current.next

        current.next = None

    def display(self):
        p = self.head
        print('LinkList values:', end=' ')
        while p:
            print(p.value, end=' ')
            p = p.next

        print()

    @property
    def length(self):
        count = 0
        p = self.head
        while p:
            p = p.next
            count += 1

        return count


def intersect_point(x, y):
    len_x, len_y = x.length, y.length
    p_x, p_y = x.head, y.head

    if len_x > len_y:
        p_x = p_x.next
        len_x -= 1

    if len_y > len_x:
        p_y = p_y.next
        len_y -= 1

    while p_x != p_y:
        p_x = p_x.next
        p_y = p_y.next

    return p_x.value if p_x else None


if __name__ == '__main__':
    x = LinkList([1, 3, 5])
    y = LinkList([2, 4])
    intersect = LinkList([7, 8, 9])

    for link in [x, y]:
        p = link.head
        while p.next:
            p = p.next

        p.next = intersect.head
        link.display()

    print('Intersect value: {}'.format(intersect_point(x, y)))
