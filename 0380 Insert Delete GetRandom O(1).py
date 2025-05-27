class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            self.arr[self.dict[val]] = self.arr[-1]
            self.dict[self.arr[-1]] = self.dict[val]
            self.dict.pop(val)
            self.arr.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
