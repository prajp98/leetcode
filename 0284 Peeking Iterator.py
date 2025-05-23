class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.nex = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.nex

    def next(self):
        value = self.nex
        self.nex = self.iterator.next() if self.iterator.hasNext() else None
        return value

    def hasNext(self):
        return self.nex != None