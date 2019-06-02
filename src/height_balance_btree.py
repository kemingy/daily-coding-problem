# Given a sorted array, convert it into a height-balanced binary search tree.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self, space=0):
        if self.right:
            self.right.display(space=space+4)
        print('{}{}'.format(' ' * space, self.value))
        if self.left:
            self.left.display(space=space+4)


def build_height_balance_btree(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = Node(nums[mid])
    root.left = build_height_balance_btree(nums[:mid])
    root.right = build_height_balance_btree(nums[mid+1:])
    return root


if __name__ == "__main__":
    for nums in [[-10, -3, 0, 5, 9], [2, 3, 5, 8, 19, 20]]:
        tree = build_height_balance_btree(nums)
        tree.display()
        print('-'*80)
