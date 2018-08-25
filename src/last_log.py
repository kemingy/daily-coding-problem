# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#     * record(order_id): adds the order_id to the log
#     * get_last(i): gets the ith last element from the log. i is guaranteed to
#       be smaller or equal to N

from collections import namedtuple

Log = namedtuple('Log', ['id', 'msg'])

class RecordLog:
    def __init__(self, limit):
        self.log = [Log(-1, '')] * limit
        self.current_index = 0

    def record(self, order_id, msg=''):
        self.log[self.current_index] = Log(order_id, msg)
        self.current_index += 1
        if self.current_index >= len(self.log):
            self.current_index = 0

    def get_last(self, i):
        assert i <= len(self.log)

        start_index = self.current_index - i
        if start_index >= 0:
            return self.log[start_index:self.current_index]
        return self.log[start_index:] + self.log[:self.current_index]


if __name__ == '__main__':
    record_log = RecordLog(15)

    for i in range(20):
        record_log.record(i)

    print(record_log.get_last(0))
    print(record_log.get_last(1))
    print(record_log.get_last(5))
    print(record_log.get_last(10))
    print(record_log.get_last(20))
