class ZigzagIterator:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.i = 0
        self.j = 0
        self.turn = 0

    def next(self):
        if not self.hasNext():
            return None
        if self.turn == 0 and self.i < len(self.v1) or self.j >= len(self.v2):
            val = self.v1[self.i]
            self.i += 1
        else:
            val = self.v2[self.j]
            self.j += 1

        self.turn ^= 1
        return val

    def hasNext(self):
        return self.i < len(self.v1) or self.j < len(self.v2)