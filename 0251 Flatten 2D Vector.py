class Vector2D:

    def __init__(self, v):
        self.r = 0
        self.c = 0
        self.vector = v

    def next(self) -> int:
        self.advance_to_next()
        val = self.vector[self.r][self.c]
        self.c += 1
        return val

    def hasNext(self) -> bool:
        self.advance_to_next()
        return self.r < len(self.vector)

    def advance_to_next(self):
        while self.r < len(self.vector) and self.c >= len(self.vector[self.r]):
            self.r += 1
            self.c = 0