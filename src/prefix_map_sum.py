# Implement a PrefixMapSum class with the following methods:
# •	insert(key: str, value: int): Set a given key's value in the map.
# If the key already exists, overwrite the value.
# •	sum(prefix: str): Return the sum of all values of keys that begin with
#   a given prefix.
# For example, you should be able to run the following code:
# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3

# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5


class Char:
    def __init__(self, char, value=0):
        self.char = char
        self.value = value
        self.next = {}

class PrefixMapSum:
    def __init__(self):
        self.premap = {}

    def insert(self, key, value):
        premap = self.premap
        for char in key:
            if char not in premap:
                premap[char] = Char(char)
            premap[char].value += value
            premap = premap[char].next

    def sum(self, prefix):
        premap = self.premap
        value = 0
        for char in prefix:
            if char not in premap:
                return value
            value = premap[char].value
            premap = premap[char].next
        return value


if __name__ == '__main__':
    mapsum = PrefixMapSum()
    mapsum.insert('columnar', 3)
    assert mapsum.sum('col') == 3
    mapsum.insert('column', 2)
    assert mapsum.sum('col') == 5
