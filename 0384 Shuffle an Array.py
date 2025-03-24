def __init__(self, nums: List[int]):
    self.array = list(nums)
    self.original = list(nums)


def reset(self) -> List[int]:
    self.array = list(self.original)
    return self.array


def shuffle(self) -> List[int]:
    n = len(self.array)
    for i in range(n):
        j = random.randint(i, n - 1)
        self.array[i], self.array[j] = self.array[j], self.array[i]
    return self.array