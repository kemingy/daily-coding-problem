# Given the root of a binary search tree, and a target K, return two nodes in 
# the tree whose sum equals K.

# For example, given the following tree and K of 20

#     10
#    /   \
#  5      15
#        /  \
#      11    15

# Return the nodes 5 and 15.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum2tree(k, node):
    inorder, reinorder = [], []
    in_done, re_done = False, False
    in_cur = re_cur = node
    in_value, re_value = None, None

    while True:
        while not in_done:
            if in_cur:
                inorder.append(in_cur)
                in_cur = in_cur.left
            else:
                if not inorder:
                    in_done = True
                else:
                    in_cur = inorder.pop()
                    in_value = in_cur.value
                    in_cur = in_cur.right
                    in_done = True

        while not re_done:
            if re_cur:
                reinorder.append(re_cur)
                re_cur = re_cur.right
            else:
                if not reinorder:
                    re_done = True
                else:
                    re_cur = reinorder.pop()
                    re_value = re_cur.value
                    re_cur = re_cur.left
                    re_done = True

        if in_value != re_value and in_value + re_value == k:
            print('Pair found: {} + {} = {}'.format(in_value, re_value, k))
            return True
        elif in_value + re_value < k:
            in_done = False
        elif in_value + re_value > k:
            re_done = False

        if in_value >= re_value:
            print('Not found for {}.'.format(k))
            return False



if __name__ == '__main__':
    tree = Node(10, Node(5), Node(15, Node(11), Node(15)))
    sum2tree(20, tree)
    sum2tree(16, tree)
    sum2tree(26, tree)
    sum2tree(31, tree)
    sum2tree(15, tree)
