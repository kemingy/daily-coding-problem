# Implement a data structure which carries out the following operations
# without resizing the underlying array:

# •	add(value): Add a value to the set of values.
# •	check(value): Check whether a value is in the set.

# The check method may return occasional false positives (in other words,
# incorrectly identifying an element as part of the set), but should always
# correctly identify a true element.

from hashlib import md5, sha1, blake2b


class BloomFiliter:
    def __init__(self, length=2<<5):
        self.bits = [0] * length
        self.length = length
        self.funcs = [md5, sha1, blake2b]

    def hash(self, value):
        byte = str(value).encode()
        return [int(func(byte).hexdigest(), 16) % self.length
                for func in self.funcs]

    def add(self, value):
        for index in self.hash(value):
            self.bits[index] = 1

    def check(self, value):
        bits = self.hash(value)

        for index in self.hash(value):
            if self.bits[index] != 1:
                return False
        return True


if __name__ == "__main__":
    bf = BloomFiliter()
    for num in [1, 3, 0, 7, 11, 255, 65535, 8]:
        bf.add(num)

    for num in [3, 0, 18, 233]:
        print(f'{num} in the filter: {bf.check(num)}')
