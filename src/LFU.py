# Implement an LFU (Least Frequently Used) cache. It should be able to be 
# initialized with a cache size n, and contain the following methods:
# •	set(key, value): sets key to value. If there are already n items in the 
#     cache and we are adding a new item, then it should also remove the least 
#     frequently used item. If there is a tie, then the least recently used key 
#     should be removed. 
# •	get(key): gets the value at key. If no such key exists, return null. 

# Each operation should run in O(1) time.

from collections import OrderedDict

class LFUcache():
    def __init__(self, n):
        assert n > 0
        self.capacity = n
        self.map = {}
        self.count = {}
        self.lists = {1: OrderedDict()}
        self.min = 1

    def set(self, key, value):
        if key in self.map:
            self.map[key] = value
            self.get(key)
            return

        if len(self.map) >= self.capacity:
            lfu = list(self.lists.get(self.min))[0]
            del self.lists.get(self.min)[lfu]
            del self.map[lfu]

        self.map[key] = value
        self.count[key] = 1
        self.min = 1
        self.lists.get(1)[key] = None


    def get(self, key):
        if key not in self.map:
            return None

        count = self.count[key]
        self.count[key] = count + 1
        del self.lists.get(count)[key]

        if count == self.min and len(self.lists.get(count)) == 0:
            self.min += 1

        if self.lists.get(count + 1) is None:
            self.lists[count + 1] = OrderedDict()

        self.lists.get(count + 1)[key] = None

        return self.map[key]


if __name__ == '__main__':
    lfu = LFUcache(2)

    lfu.set(1, 1)
    lfu.set(2, 2)
    print(lfu.get(1))

    lfu.set(3, 3)
    print(lfu.get(2))
    print(lfu.get(3))

    lfu.set(4, 4)
    print(lfu.get(1), lfu.get(3), lfu.get(4))
