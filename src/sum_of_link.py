# Let's represent an integer in a linked list format by having each node 
# represent a digit in the number. The nodes make up the number in reversed 
# order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5

# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked 
# list format.
# For example, given

# 9 -> 9
# 5 -> 2

# return 124 (99 + 25) as:

# 4 -> 2 -> 1


class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def sum_of_link(x, y):
    ans = Node(0)
    cur = ans
    carry = 0
    while x and y:
        add = x.value + y.value + carry
        if add > 9:
            cur.next = Node(add - 10)
            carry = 1
        else:
            cur.next = Node(add)
            carry = 0
        x = x.next
        y = y.next
        cur = cur.next

    while x:
        add = x.value + carry
        if add > 9:
            cur.next = Node(add - 10)
            carry = 1
        else:
            cur.next = Node(add)
            carry = 0
        x = x.next
        cur = cur.next

    while y:
        add = y.value + carry
        if add > 9:
            cur.next = Node(add - 10)
            carry = 1
        else:
            cur.next = Node(add)
            carry = 0
        y = y.next
        cur = cur.next

    if carry == 1:
        cur.next = Node(1)

    return ans.next if ans.next else ans

def display(node):
    while node and node.next:
        print(node.value, end=' -> ')
        node = node.next
    if node:
        print(node.value)


if __name__ == '__main__':
    x = Node(9, Node(9, Node(9)))
    y = Node(5, Node(2))
    display(x)
    print('+')
    display(y)
    print('=')
    display(sum_of_link(x, y))
