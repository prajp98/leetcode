class MovingAverage:

    def __init__(self, size: int):
        self.q=deque([])
        self.n=size
        self.sum=0

    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum+=val
        if len(self.q)>self.n:
            self.sum-=self.q.popleft()
        return self.sum/len(self.q)