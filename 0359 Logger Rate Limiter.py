class Logger:

    def __init__(self):
        self.m = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.m or timestamp - self.m[message] >= 10:
            self.m[message] = timestamp
            return True
        return False