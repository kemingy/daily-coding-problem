# Implement an LRU (Least Recently Used) cache. It should be able to be 
# initialized with a cache size n, and contain the following methods:
# •	set(key, value): sets key to value. If there are already n items in the 
#     cache and we are adding a new item, then it should also remove the least 
#     recently used item. 
# •	get(key): gets the value at key. If no such key exists, return null. 

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = self.next = None

    def __repr__(self):
        return 'Node({}:{})'.format(self.key, self.value)


class LRUcache:
    def __init__(self, n):
        self.capacity = n
        self.count = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}

    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.update(node)

        node = Node(key, value)
        self.map[key] = node
        self.add(node)
        self.count += 1

        if self.count > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.map[lru.key]
            self.count -= 1

    def remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before

    def add(self, node):
        after_head = self.head.next
        self.head.next = node
        node.next = after_head
        node.prev = self.head
        after_head.prev = node

    def update(self, node):
        self.remove(node)
        self.add(node)

    def get(self, key):
        node = self.map.get(key)
        if node is None:
            return None

        self.update(node)
        return node.value

    def display(self):
        node = self.head.next
        print('>>>>>>>>>>>>>>')
        while node != self.tail:
            print(node)
            node = node.next

        print('<<<<<<<<<<<<<<')


if __name__ == '__main__':
    lru = LRUcache(5)
    for k, v in zip('abcde', range(5)):
        lru.set(k, v)

    lru.display()
    print(lru.get('f'))
    print(lru.get('a'))
    print(lru.get('c'))
    lru.display()
    lru.set('m', 88)
    lru.display()
