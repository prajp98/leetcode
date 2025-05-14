class LogSystem:
    def __init__(self):
        self.times = {}
        self.g = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    def put(self, id, timestamp):
        self.times[id] = timestamp

    def retrieve(self, s, e, gra):
        idx = self.g[gra]
        start = s[:idx]
        end = e[:idx]
        res = []
        for i, time in self.times.items():
            if start <= time[:idx] <= end:
                res.append(i)
        return res