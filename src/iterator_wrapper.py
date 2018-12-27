# Given an iterator with methods next() and hasNext(), create a wrapper
# iterator, PeekableInterface, which also implements peek(). peek shows the
# next element that would be returned on next().

# Here is the interface:

# class PeekableInterface(object):
#     def __init__(self, iterator):
#         pass

#     def peek(self):
#         pass

#     def next(self):
#         pass

#     def hasNext(self):
#         pass


class PeekableInterface:
    def __init__(self, iterator):
        self.iter = iterator
        self.try_peek()

    def peek(self):
        return self.cache

    def try_peek(self):
        try:
            self.cache = next(self.iter)
        except StopIteration:
            self.cache = None

    def next(self):
        tmp = self.cache
        self.try_peek()
        return tmp

    def hasNext(self):
        return True if self.cache else False


if __name__ == "__main__":
    for it in ['hello world', ('are', 'u', 'ok')]:
        pi = PeekableInterface(iter(it))
        while pi.hasNext():
            print(pi.peek(), pi.next())
