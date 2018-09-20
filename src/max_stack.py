# Implement a stack that has the following methods:
# •	push(val), which pushes an element onto the stack 
# •	pop(), which pops off and returns the topmost element of the stack. 
#     If there are no elements in the stack, then it should throw an error 
#     or return null. 
# •	max(), which returns the maximum value in the stack currently. If there 
#     are no elements in the stack, then it should throw an error or return null. 

class MaxStack:
    def __init__(self):
        self.stack = []
        self.cur_max = []

    def push(self, v):
        self.stack.append(v)
        if not self.cur_max:
            self.cur_max.append(v)
        elif self.cur_max[-1] <= v:
            self.cur_max.append(v)

        return True

    def pop(self):
        if not self.stack:
            raise IndexError('There are no elements in the stack.')

        v = self.stack.pop()
        if v == self.cur_max[-1]:
            self.cur_max.pop()

        return v

    def max(self):
        if not self.cur_max:
            raise IndexError('There are no elements in the stack.')

        return self.cur_max[-1]


if __name__ == '__main__':
    ms = MaxStack()
    for v in [2, 4, 8, 5, 9, 9]:
        ms.push(v)

    print(ms.max())
    print(ms.pop())
    print(ms.max())
    print(ms.pop())
    print(ms.max())
