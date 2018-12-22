# You have a large array with most of the elements as zero.
# Use a more space-efficient data structure, SparseArray, that implements the
# same interface:

# •	init(arr, size): initialize with the original large array and size.
# •	set(i, val): updates index at i with val.
# •	get(i): gets the value at index i.


class SparseArray:
    def __init__(self, arr, size):
        self.array = {}
        self.size = size
        for key in arr:
            self.set(key, arr[key])

    def set(self, i, val):
        if i < 0 or i >= self.size:
            print("Error: index {} is out of size {}.".format(i, self.size))
            return
        self.array[i] = val

    def get(self, i):
        if i < 0 or i >= self.size:
            print("Error: index {} is out of size {}.".format(i, self.size))
            return
        return self.array.get(i, 0)


if __name__ == "__main__":
    sa = SparseArray({233: 1, 1234: 1}, 10000)
    sa.set(0, 1)
    print(sa.get(21))
    print(sa.get(1234))
