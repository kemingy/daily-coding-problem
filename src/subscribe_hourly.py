# You are given an array of length 24, where each element represents the number
# of new subscribers during the corresponding hour. Implement a data structure
# that efficiently supports the following:

# •	update(hour: int, value: int): Increment the element at index hour by value.
# •	query(start: int, end: int): Retrieve the number of subscribers that have
#   signed up between start and end (inclusive).

# You can assume that all values get cleared at the end of the day, and that
# you will not be asked for start and end values that wrap around midnight.


class SubscribeHourly:
    def __init__(self):
        self.num = [0] * 24

    def update(self, hour: int, value: int):
        assert 0 <= hour < 24
        assert value > 0
        self.num[hour] += value

    def query(self, start: int, end: int) -> int:
        assert 0 <= start < 24
        assert 0 <= end < 24
        return sum(self.num[start:end+1])


if __name__ == '__main__':
    sh = SubscribeHourly()
    print(sh.query(12, 23))
    sh.update(14, 22)
    sh.update(2, 34)
    print(sh.query(0, 12))
