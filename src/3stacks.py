# Implement 3 stacks using a single list:

# class Stack:
#     def __init__(self):
#         self.list = []

#     def pop(self, stack_number):
#         pass

#     def push(self, item, stack_number):
#         pass


class Stack:
    def __init__(self):
        self.list = []
        self.available = {0, 1, 2}
        self.top = [-3, -2, -1]

    def pop(self, stack_number):
        assert stack_number in self.available
        index = self.top[stack_number]
        if index < 0:
            print("No more item in this stack.")
            return None

        item = self.list[index]
        self.list[index] = None
        self.top[stack_number] -= 3
        self.clean()
        return item

    def push(self, item, stack_number):
        assert stack_number in self.available
        index = self.top[stack_number] + 3
        if index >= len(self.list):
            self.list.extend([None] * 3)
        self.list[index] = item
        self.top[stack_number] += 3

    def clean(self):
        if len(self.list) >= 3:
            for item in self.list[:-3]:
                if item != None:
                    return
            for _ in range(3):
                self.list.pop()


if __name__ == "__main__":
    s = Stack()

    nums = list(range(5))
    alphabets = list("abc")
    strings = ["hello", "world"]

    for i, items in enumerate([nums, alphabets, strings]):
        for item in items:
            s.push(item, i)

    print(s.list)
    print(s.top)
    print(s.pop(2))
    print(s.pop(2))
    print(s.pop(1))
    print(s.pop(0))
