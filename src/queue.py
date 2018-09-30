# Implement a queue using two stacks. Recall that a queue is a FIFO 
# (first-in, first-out) data structure with the following methods: enqueue, 
# which inserts an element into the queue, and dequeue, which removes it.


class Queue:
    def __init__(self):
        self.ins = []
        self.out = []

    def enqueue(self, value):
        self.ins.append(value)

    def dequeue(self):
        if not self.out:
            while self.ins:
                self.out.append(self.ins.pop())

        return self.out.pop()


if __name__ == '__main__':
    q = Queue()
    for i in range(5):
        q.enqueue(i)

    for _ in range(3):
        print(q.dequeue())

    for i in range(5, 10):
        q.enqueue(i)

    for _ in range(7):
        print(q.dequeue())
