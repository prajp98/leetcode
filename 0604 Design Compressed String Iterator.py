class StringIterator:
    def __init__(self, s: str):
        self.res = s
        self.p = 0
        self.num = 0
        self.ch = ' '

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.num == 0:
            self.ch = self.res[self.p]
            self.p += 1
            self.num = 0
            while self.p < len(self.res) and self.res[self.p].isdigit():
                self.num = self.num * 10 + int(self.res[self.p])
                self.p += 1
        self.num -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.p < len(self.res) or self.num > 0