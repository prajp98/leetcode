def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_avg = float('-inf')
    for i in range(len(nums) - k + 1):
        curr_sum = sum(nums[i:i + k])
        max_avg = max(max_avg, curr_sum / k)
    return max_avg

def findMaxAverage(self, nums: List[int], k: int) -> float:
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]

    max_avg = float('-inf')
    for i in range(k, len(prefix)):
        total = prefix[i] - prefix[i - k]
        max_avg = max(max_avg, total / k)
    return max_avg