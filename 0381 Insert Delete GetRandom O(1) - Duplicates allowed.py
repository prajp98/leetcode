class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.indices[val]:
            return False
        i = self.indices[val].pop()
        last = self.nums[-1]

        self.nums[i] = last
        self.indices[last].add(i)
        self.indices[last].discard(len(self.nums) - 1)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)