# Implement a 2D iterator class. It will be initialized with an array of arrays,
# and should implement the following methods:

# •	next(): returns the next element in the array of arrays. If there are no
#           more elements, raise an exception.
# •	has_next(): returns whether or not the iterator still has elements left.

# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
# repeatedly should output 1, 2, 3, 4, 5, 6.

# Do not use flatten or otherwise clone the arrays. Some of the arrays can be
# empty.


class NestArray:
    def __init__(self, arrays):
        self.arrays = arrays
        self.i = 0
        self.j = 0

    def next(self):
        if self.has_next():
            n = self.arrays[self.i][self.j]
            self.j += 1
            return n
        raise StopIteration("End of arrays.")

    def has_next(self):
        if self.i >= len(self.arrays):
            return False
        if self.j >= len(self.arrays[self.i]):
            self.j = 0
            self.i += 1
            return self.has_next()
        return True


if __name__ == "__main__":
    na = NestArray([[1, 2], [3], [], [4, 5, 6]])
    while True:
        try:
            print(na.next())
        except StopIteration:
            break
