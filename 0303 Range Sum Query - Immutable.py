class NumArray:

    def __init__(self, nums: List[int]):
        self.sums=[0]*len(nums)
        self.sums[0]=nums[0]
        for i in range(1,len(nums)):
            self.sums[i]=self.sums[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right]-self.sums[left-1] if left>0 else self.sums[right]