class TwoSum:

    def __init__(self):
        self.nums = {}

    def add(self, number: int) -> None:
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value: int) -> bool:
        for num in self.nums.keys():
            comp = value - num
            if num != comple:
                if comp in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True
        return False