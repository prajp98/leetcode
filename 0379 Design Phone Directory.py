class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.l = deque(range(maxNumbers))
        self.s = set(range(maxNumbers))

    def get(self) -> int:
        if not self.l:
            return -1
        num = self.l.popleft()
        self.s.remove(num)
        return num

    def check(self, number: int) -> bool:
        return number in self.s

    def release(self, number: int) -> None:
        if number not in self.s:
            self.l.append(number)
            self.s.add(number)