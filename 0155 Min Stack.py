class MinStack:
    def __init__(self):
        self.s=[]
        self.mins=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        top=self.mins[-1] if self.mins else val
        self.mins.append(min(val,top))

    def pop(self) -> None:
        self.mins.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mins[-1]