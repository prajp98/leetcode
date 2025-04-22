def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_avg = float('-inf')
    for i in range(len(nums) - k + 1):
        curr_sum = sum(nums[i:i + k])
        max_avg = max(max_avg, curr_sum / k)
    return max_avg