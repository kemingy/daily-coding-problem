# Implement a bit array.
# A bit array is a space efficient array that holds a value of 1 or 0 at each
# index.

# •	init(size): initialize the array with size
# •	set(i, val): updates index at i with val where val is either 1 or 0.
# •	get(i): gets the value at index i.


class BitArray:
    def __init__(self, size):
        self.size = size
        self.bits = 1 << size

    def set(self, i, val):
        if i >= self.size:
            raise IndexError("Index {} out of size {}.".format(i, self.size))

        if val != 0 and val != 1:
            raise ValueError("Value must be 0 or 1, not {}".format(val))

        if val == 0:
            if self.get(i):
                self.bits ^= 1 << i
        else:
            self.bits |= 1 << i

    def get(self, i):
        if i >= self.size:
            raise IndexError("Index {} out of size {}.".format(i, self.size))

        return 1 if self.bits & 1 << i else 0


if __name__ == "__main__":
    ba = BitArray(100)
    ba.set(23, 1)
    ba.set(23, 0)
    ba.set(42, 1)
    print(ba.get(42))
    print(ba.get(23))
    ba.set(100, 1)
